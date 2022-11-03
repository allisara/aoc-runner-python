import { MaybeString } from "../types/types";
import { extractPartOne, extractPartTwo } from "../services/html";
import { year } from "../config/env";
import path from "path";
import { get } from "../services/requests";
import { htmlToMarkdown } from "../services/convert";
import { existsSync } from "fs";
import {
  copyBoilerplateFiles,
  createFolder,
  fileWriter,
  initDay,
} from "../services/io";

export async function downloadController(day: MaybeString) {
  if (!day) {
    console.log("ERROR: DAY NUMBER REQUIRED");
    return;
  }

  const fullPageHtml = await get(`https://adventofcode.com/${year}/day/${day}`);
  const problemFolder = path.join(
    __dirname,
    `../../problems/${year}/day${day}/`
  );
  const saveFile = fileWriter(problemFolder);

  createFolder(problemFolder);
  initDay(day);

  const firstQuestionHtml = extractPartOne(fullPageHtml);
  const firstQuestionMd = htmlToMarkdown(firstQuestionHtml);

  if (!existsSync(problemFolder + "dataset.txt")) {
    const dataSet = await get(
      `https://adventofcode.com/${year}/day/${day}/input`
    );
    await saveFile("dataset.txt", dataSet);
  }

  await saveFile("q1.md", firstQuestionMd);
  await copyBoilerplateFiles(problemFolder);

  console.log(`PROBLEM SET FOR ${year} - Day ${day} DOWNLOADED`);
}
