import path from "path";
import { year } from "../config/env";
import { htmlToMarkdown } from "../services/convert";
import { extractAnswerStatus, extractPartTwo } from "../services/html";
import {
  fileWriter,
  getPartOfDayToSubmit,
  markCorrectGuess,
  upsertGuess,
} from "../services/io";
import { get, post } from "../services/requests";
import { runPython } from "../services/spawn";
import { MaybeString, Problem } from "../types/types";

export async function submitAnswerController(day: MaybeString) {
  if (!day || isNaN(parseInt(day))) {
    console.log("\nArgument Error\nEnter day number to submit");
    return;
  }

  const part = getPartOfDayToSubmit(day);
  if (!part) {
    console.log("\nBoth parts already submitted");
    return;
  }

  const { data, isCorrect: hasRunWithoutError } = await runPython(
    { day, part },
    true
  );

  if (!hasRunWithoutError) {
    console.log("\nProgram Crashed. Aborting Submission.");
  }

  const lines = data.replaceAll("\r", "").split("\n");
  const answer = lines.at(-1) || lines.at(-2) || "parse error";

  const isUniqueAnswer = upsertGuess(answer, { day, part });
  if (!isUniqueAnswer) {
    console.log("\nThis answer has been guessed before\nNot submitting");
    return;
  }

  const res = await post(`https://adventofcode.com/${year}/day/${day}/answer`, {
    answer,
    level: part,
  });

  const status = extractAnswerStatus(res);

  console.log("\n" + status);

  if (!status.includes("That's the right answer")) return;

  markCorrectGuess({ day, part });

  if (part === "2") return;

  const fullPageHtml = await get(`https://adventofcode.com/${year}/day/${day}`);
  const problemFolder = path.join(
    __dirname,
    `../../problems/${year}/day${day}/`
  );
  const saveFile = fileWriter(problemFolder);

  const secondQuestionHtml = extractPartTwo(fullPageHtml);
  const secondQuestionMd = htmlToMarkdown(secondQuestionHtml);
  saveFile("q2.md", secondQuestionMd);

  console.log("\nQuestion 2 Downloaded!\n");
}
