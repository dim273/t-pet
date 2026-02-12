const fs = require("fs");
const path = require("path");
const TurndownService = require("turndown");
const { JSDOM } = require("jsdom");

const LEETCODE_GRAPHQL = "https://leetcode.cn/graphql";

// turndown：HTML -> Markdown 转换器
const turndownService = new TurndownService({
  codeBlockStyle: "fenced",
  headingStyle: "atx",
});

// 保留 <pre><code> 代码块
turndownService.addRule("preCodeBlock", {
  filter: function (node) {
    return node.nodeName === "PRE";
  },
  replacement: function (content, node) {
    return "\n```text\n" + node.textContent.trim() + "\n```\n";
  },
});

// 删除无用标签
turndownService.remove(["style", "script"]);

async function fetchLeetCodeProblem(slug) {
  try {
    const query = `
        query questionData($titleSlug: String!) {
          question(titleSlug: $titleSlug) {
            questionId
            title
            translatedTitle
            difficulty
            content
            translatedContent
            exampleTestcases
            topicTags {
              name
              translatedName
            }
          }
        }
        `;

    const body = {
      query,
      variables: { titleSlug: slug },
    };

    const res = await fetch(LEETCODE_GRAPHQL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
      },
      body: JSON.stringify(body),
    });

    const data = await res.json();

    if (!data.data || !data.data.question) {
      console.log("没有获取到题目，slug 可能错误:", slug);
      return;
    }

    const q = data.data.question;

    // 中文优先
    const title = q.translatedTitle || q.title;
    const contentHtml = q.translatedContent || q.content;

    console.log(`获取成功: ${q.questionId} - ${title}`);

    // HTML -> Markdown
    const contentMd = htmlToMarkdown(contentHtml);

    // 解析题面中的示例（输入输出）
    const examples = extractExamples(contentHtml);

    // 标签中文
    const tags = q.topicTags
      .map(t => t.translatedName || t.name)
      .join(", ");

    const markdown = buildMarkdown({
      id: q.questionId,
      title,
      difficulty: translateDifficulty(q.difficulty),
      tags,
      contentMd,
      examples,
    });

    // 保存目录
    const saveDir = path.join(__dirname, "..", "res", "Problem");
    if (!fs.existsSync(saveDir)) {
      fs.mkdirSync(saveDir, { recursive: true });
    }

    const safeTitle = title.replace(/[\\/:*?"<>|]/g, "_");
    const filename = path.join(saveDir, '94.md');

    fs.writeFileSync(filename, markdown, "utf-8");
    console.log("保存成功:", filename);

  } catch (err) {
    console.error("抓取失败:", err);
  }
}

// HTML -> Markdown（使用 turndown）
function htmlToMarkdown(html) {
  if (!html) return "";
  const md = turndownService.turndown(html);
  return md.replace(/\n{3,}/g, "\n\n").trim();
}

// 提取示例输入输出（从题面 HTML 里抓 <pre>）
function extractExamples(html) {
  const dom = new JSDOM(html);
  const document = dom.window.document;

  const pres = [...document.querySelectorAll("pre")];
  const examples = [];

  for (let pre of pres) {
    const text = pre.textContent.trim();

    // LeetCode CN 示例通常长这样：
    // 输入：xxx
    // 输出：yyy
    // 解释：zzz
    if (text.includes("输入") && text.includes("输出")) {
      examples.push(text);
    }
  }

  return examples;
}

function translateDifficulty(diff) {
  if (diff === "Easy") return "简单";
  if (diff === "Medium") return "中等";
  if (diff === "Hard") return "困难";
  return diff;
}

function buildMarkdown({ id, title, difficulty, tags, contentMd }) {
  return `# ${title}

## 题目描述

${contentMd}
`;
}

// 直接运行
if (require.main === module) {
  const slugs = [
    "01-matrix"         // 两数之和
  ];

  slugs.forEach(slug => fetchLeetCodeProblem(slug));
}

module.exports = { fetchLeetCodeProblem };
