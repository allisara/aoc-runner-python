import axios from "axios";
import * as cheerio from "cheerio";
import { writeFile } from "fs/promises";
import { NodeHtmlMarkdown } from "node-html-markdown";
import path from "path";
import { year } from "../env";
console.log(year);

const args = process.argv.slice(2);
console.log(args);

const nodeHtmlMarkdown = new NodeHtmlMarkdown();

axios.get("https://adventofcode.com/2021/day/18").then(async (res) => {
  const $ = cheerio.load(res.data);
  const question = $(".day-desc").html();

  const md = nodeHtmlMarkdown.translate(question);
  await writeFile(path.join(__dirname, "test.md"), md, "utf-8");
});
