import * as cheerio from "cheerio";
import { writeFile } from "fs/promises";
import { NodeHtmlMarkdown } from "node-html-markdown";
import path from "path";
import { get, post } from "./services/requests";

const args = process.argv.slice(2);
console.log(args);

async function testGet() {
  const vals = await post("https://adventofcode.com/2021/day/18/answer", {
    level: 1,
    answer: "wrong answer",
  });
  console.log(vals);
}

testGet();

// const nodeHtmlMarkdown = new NodeHtmlMarkdown();

// axios.get("https://adventofcode.com/2021/day/17").then(async (res) => {
//   const $ = cheerio.load(res.data);
//   const question = $(".day-desc").html();

//   const md = nodeHtmlMarkdown.translate(question);
//   await writeFile(path.join(__dirname, "test.md"), md, "utf-8");
// });
