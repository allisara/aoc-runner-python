import { submitAnswerController } from "./controllers/answer";
import { downloadController } from "./controllers/download";
import { testAnswerController } from "./controllers/test-answer";
import { MaybeString } from "./types/types";

const args = process.argv.slice(2);
const controller = args[0] as MaybeString;
const arg = args[1] as MaybeString;

if (controller === "download") {
  downloadController(arg);
}

if (controller === "answer") {
  submitAnswerController(arg);
}

if (controller == "test") {
  testAnswerController(true, arg);
}

if (controller === "test-full") {
  testAnswerController(false, arg);
}

// async function testGet() {
// const res = await get("https://adventofcode.com/2021/day/18");
// console.log(res);
// const vals = await post("https://adventofcode.com/2021/day/18/answer", {
//   level: 1,
//   answer: "wrong answer",
// });
// console.log(vals);
// }

// testGet();

// const nodeHtmlMarkdown = new NodeHtmlMarkdown();

// axios.get("https://adventofcode.com/2021/day/17").then(async (res) => {
//   const $ = cheerio.load(res.data);
//   const question = $(".day-desc").html();

//   const md = nodeHtmlMarkdown.translate(question);
//   await writeFile(path.join(__dirname, "test.md"), md, "utf-8");
// });
