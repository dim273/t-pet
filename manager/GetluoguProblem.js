//const rp = require('request-promise');
//const cheerio = require('cheerio');
//const fs = require('fs');
//const path = require('path');

const baseUrl = 'https://www.luogu.com.cn/problem/';

const fetchPage = async (problemId) => {
    try {
        const url = `${baseUrl}${problemId}`;
        const html = await rp(url);
        const $ = cheerio.load(html);
        const articleHtml = $('article').html();
        const h1 = $('h1').first().text().trim(); // 获取第一个 <h1> 标签的内容作为文件名

        // 定义正则表达式来匹配不同的 HTML 标签
        const h1Regex = /<h1>(.*?)<\/h1>\s*/g;
        const h2Regex = /<h2>(.*?)<\/h2>\s*/g;
        const h3Regex = /<h3>(.*?)<\/h3>\s*/g;
        const h4Regex = /<h4>(.*?)<\/h4>\s*/g;
        const preCodeRegex = /<pre><code>(.*?)<\/code><\/pre>\s*/gs;
        const codeRegex = /<code>(.*?)<\/code>\s*/g;
        const divRegex = /<div>(.*?)<\/div>\s*/gs;
        const brRegex = /<br>\s*/g;
        const sectionRegex = /<section[^>]*>|<\/section>/g;

        // 将匹配到的标签替换为 Markdown 对应的格式
        const markdown = articleHtml
            .replace(h1Regex, '# $1\n')
            .replace(h2Regex, '## $1\n')
            .replace(h3Regex, '### $1\n')
            .replace(h4Regex, '#### $1\n')
            .replace(preCodeRegex, '```\n$1\n```\n')
            .replace(codeRegex, '`$1`\n')
            .replace(divRegex, '$1\n')
            .replace(brRegex, '\n')
            .replace(sectionRegex, '')
            .replace(/^[ \t]+/gm, '');

        const saveDir = path.join(__dirname, '..', 'res/Problem');
        // 写入 Markdown 文件，使用 example 标签的内容作为文件名
        const filename = path.join(saveDir, '139.md');
        fs.writeFileSync(filename, markdown.trim());
    } catch (error) {
        console.error(`题目获取出错 ${problemId}:`, error);
    }
};

// 如果直接运行此文件，则执行默认的问题ID列表
if (require.main === module) {
    const problemIds = [
        'P3953'
    ];

    // 批量下载
    problemIds.forEach((problemId) => {
        fetchPage(problemId);
    });
}

module.exports = { fetchPage };