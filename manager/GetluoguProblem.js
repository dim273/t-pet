const rp = require('request-promise');
const cheerio = require('cheerio');
const sanitizeFilename = require('sanitize-filename');

const baseUrl = 'https://www.luogu.com.cn/problem/';

/**
 * 获取题目详情并转换为Markdown
 * @param {string} problemId 题目ID（如P1996）
 * @returns {Promise<{id: string, title: string, content: string}>} 题目信息
 */
async function fetchProblem(problemId) {
  try {
    const url = `${baseUrl}${problemId}`;
    const html = await rp(url);
    const $ = cheerio.load(html);

    // 提取题目内容
    const articleHtml = $('article').html();
    const title = $('h1').first().text().trim();

    // HTML转Markdown的正则替换规则
    const replacements = [
      { regex: /<h1>(.*?)<\/h1>\s*/g, replacement: '# $1\n' },
      { regex: /<h2>(.*?)<\/h2>\s*/g, replacement: '## $1\n' },
      { regex: /<h3>(.*?)<\/h3>\s*/g, replacement: '### $1\n' },
      { regex: /<h4>(.*?)<\/h4>\s*/g, replacement: '#### $1\n' },
      { regex: /<pre><code>(.*?)<\/code><\/pre>\s*/gs, replacement: '```\n$1\n```\n' },
      { regex: /<code>(.*?)<\/code>\s*/g, replacement: '`$1`\n' },
      { regex: /<div>(.*?)<\/div>\s*/gs, replacement: '$1\n' },
      { regex: /<br>\s*/g, replacement: '\n' },
      { regex: /<p>(.*?)<\/p>\s*/gs, replacement: '$1\n\n' },
      { regex: /<strong>(.*?)<\/strong>/g, replacement: '**$1**' },
      { regex: /<em>(.*?)<\/em>/g, replacement: '*$1*' }
    ];

    // 执行替换
    let content = articleHtml;
    replacements.forEach(({ regex, replacement }) => {
      content = content.replace(regex, replacement);
    });

    console.log("成功");

    return {
      id: problemId,
      title: title,
      content: content.trim()
    };
  } catch (error) {
    console.error(`获取题目${problemId}失败:`, error);
    throw error;
  }
}

module.exports = { fetchProblem };