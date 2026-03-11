import os
import sys
import json
import urllib.request
import urllib.error
import re
import subprocess
import time

# 配置
API_CONFIG_FILE = "aiConfig.json"
PROBLEM_DIR = os.path.join("res", "Problem")
JUDGE_DATA_DIR = os.path.join("res", "JudgeData")

def load_api_config():
    if not os.path.exists(API_CONFIG_FILE):
        print(f"Error: {API_CONFIG_FILE} not found.")
        sys.exit(1)
    try:
        with open(API_CONFIG_FILE, "r", encoding="utf-8") as f:
            config = json.load(f)
            return config.get("openrouter", {})
    except Exception as e:
        print(f"Error loading config: {e}")
        sys.exit(1)

def get_problem_content(problem_id):
    filename = f"{problem_id}.md"
    path = os.path.join(PROBLEM_DIR, filename)
    if not os.path.exists(path):
        # Try to find file case-insensitively if possible, but for now strict match
        # print(f"Warning: Problem file {path} not found.")
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"Error reading problem file: {e}")
        return None

def call_llm(api_config, prompt):
    api_key = api_config.get("apiKey")
    model = api_config.get("model", "stepfun/step-3.5-flash:free")
    
    if not api_key:
        print("Error: API Key not found in config.")
        sys.exit(1)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": api_config.get("referer", "https://github.com/t-pet"),
        "X-Title": api_config.get("title", "T-Pet AI Assistant"), 
        "User-Agent": "Mozilla/5.0"
    }

    data = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    try:
        req = urllib.request.Request(
            "https://openrouter.ai/api/v1/chat/completions",
            data=json.dumps(data).encode("utf-8"),
            headers=headers,
            method="POST"
        )
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode("utf-8"))
            return result["choices"][0]["message"]["content"]
    except urllib.error.HTTPError as e:
        print(f"API Error: {e.code} - {e.reason}")
        try:
            print(e.read().decode("utf-8"))
        except:
            pass
        return None
    except Exception as e:
        print(f"Request Error: {e}")
        return None

def extract_code_block(response, lang="python"):
    # Try to find specific language code block
    match = re.search(f"```{lang}(.*?)```", response, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    
    # Try generic code block
    match = re.search(r"```(.*?)```", response, re.DOTALL)
    if match:
        return match.group(1).strip()
        
    return response.strip()

def process_problem(problem_id, user_cpp_input):
    api_config = load_api_config()
    problem_desc = get_problem_content(problem_id)
    
    if not problem_desc:
        print(f"Skipping Problem {problem_id}: Description file not found.")
        return False

    print(f"\nProcessing Problem {problem_id}...")

    # Step 1: Generate Standard C++ Solution (if input is partial) AND Python Generator script
    # We ask for both in one go or separate? 
    # User said: "拿着题目的md文件和我输入的参考代码去询问大模型（可分多次），并生成python脚本以及标准的cpp文件"
    # To be safe and accurate, let's do it in two steps or a combined structured prompt.
    # Given the complexity, let's first ensure we have a working complete C++ code.

    print("  -> Generating/Completing Standard C++ Code...")
    cpp_prompt = f"""
你是一个算法竞赛专家。
请根据以下题目描述和用户提供的参考代码（可能是不完整的 C++ 代码片段，例如仅包含 Solution 类），编写一个**完整的、可直接编译运行的 Standard C++ 解决方案 (`std.cpp`)**。

**题目描述**：
{problem_desc}

**用户参考代码**：
```cpp
{user_cpp_input}
```

**要求**：
1. 如果用户提供的是 `class Solution`，请补充 `main` 函数，处理输入输出（读取标准输入，调用 Solution 方法，输出结果到标准输出）。
2. 如果用户提供的是完整代码，请检查并确保其可以通过标准输入输出进行测试（去除 LeetCode 特有的注释或结构，转为 ACM 模式）。
3. **只输出 C++ 代码块**，不要包含 markdown 标记以外的文字。
4. 包含必要的头文件。
"""
    
    cpp_response = call_llm(api_config, cpp_prompt)
    if not cpp_response:
        print("  -> Failed to generate C++ code.")
        return False
    
    std_cpp_code = extract_code_block(cpp_response, "cpp")
    # print(std_cpp_code)
    time.sleep(10)
    print("  -> Generating Python Data Generator Script...")
    gen_prompt = f"""
你是一个算法竞赛数据生成专家。
请根据以下题目描述和标准的 C++ 标程，编写一个 Python 脚本 `gen.py`，用于生成 20 组测试数据。

**题目描述**：
{problem_desc}

**标准 C++ 标程**：
```cpp
{std_cpp_code}
```

**任务要求**：
1. **理解数据范围**：仔细分析题目和代码中的数据范围（如 N 的大小，整数范围等），确保生成的数据合法且具有一定强度（包含边界情况、最大数据量）。
2. **生成逻辑**：
   - 使用 `random` 库生成数据。
   - 必须生成 20 组数据，文件名分别为 `tests/1.in` 到 `tests/20.in`。
   - 确保 `tests` 目录存在，如果不存在则创建。
   - 数据难度应递增，后几组数据应达到题目规定的最大规模，用于卡掉复杂度较高的算法。
3. **生成输出**：
   - 脚本必须包含编译同目录下 `std.cpp` 的逻辑（如果 `std.exe` 不存在）。
   - **关键**：使用 `subprocess.run` 或 `os.system` 执行编译命令：`g++ std.cpp -o std -O2`。
   - 脚本必须运行 `std.exe`，利用重定向生成 `.out` 文件。
   - 兼容 Windows 系统（使用 `std.exe`）。
4. **输出格式**：
   - **只输出 Python 代码块**。

**Python 脚本结构参考**：
```python
import os
import random
import subprocess

def generate_case(index):
    # ... return input_string ...
    pass

def main():
    if not os.path.exists("tests"):
        os.makedirs("tests")
    
    # Compile
    if not os.path.exists("std.exe"):
        subprocess.run(["g++", "std.cpp", "-o", "std", "-O2"], check=True)
    
    for i in range(1, 21):
        input_data = generate_case(i)
        in_file = os.path.join("tests", f"{{i}}.in")
        out_file = os.path.join("tests", f"{{i}}.out")
        
        with open(in_file, "w") as f:
            f.write(input_data)
            
        # Run std.exe
        # Using shell=True for redirection support on Windows
        os.system(f"std.exe < {{in_file}} > {{out_file}}")
        print(f"Generated Case {{i}}")

if __name__ == "__main__":
    main()
```
"""

    gen_response = call_llm(api_config, gen_prompt)
    if not gen_response:
        print("  -> Failed to generate Python script.")
        return False

    gen_py_code = extract_code_block(gen_response, "python")

    # Save files
    p_dir = os.path.join(JUDGE_DATA_DIR, f"P{problem_id}")
    if not os.path.exists(p_dir):
        os.makedirs(p_dir)
    
    std_path = os.path.join(p_dir, "std.cpp")
    with open(std_path, "w", encoding="utf-8") as f:
        f.write(std_cpp_code)
    
    gen_path = os.path.join(p_dir, "gen.py")
    with open(gen_path, "w", encoding="utf-8") as f:
        f.write(gen_py_code)

    print(f"  -> Successfully created {std_path} and {gen_path}")
    return True

def get_multiline_input():
    print("请输入参考代码（输入 'END' 结束，或者按 Ctrl+Z/Ctrl+D）：")
    lines = []
    while True:
        try:
            line = input()
            if line.strip() == "END":
                break
            lines.append(line)
        except EOFError:
            break
    return "\n".join(lines)

def main():
    start_id = 67
    end_id = 132

    print(f"Starting Auto Data Generation Workflow from P{start_id} to P{end_id}")
    
    for pid in range(start_id, end_id + 1):
        # Check if problem exists
        if not get_problem_content(pid):
            # print(f"Skipping P{pid} (Markdown file not found)")
            continue

        while True:
            print(f"\n==========================================")
            print(f"当前题目编号: P{pid}")
            print(f"==========================================")
            
            # Wait for user input
            user_code = get_multiline_input()
            
            if not user_code.strip():
                print("Input empty, skipping this problem.")
                break

            success = process_problem(pid, user_code)
            if success:
                print(f"P{pid} 完成。")
                break
            else:
                print(f"P{pid} 处理失败，请重新输入代码重试。")

if __name__ == "__main__":
    main()
