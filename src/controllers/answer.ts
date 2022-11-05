import { year } from "../config/env";
import { extractAnswerStatus } from "../services/html";
import {
  getPartOfDayToSubmit,
  markCorrectGuess,
  upsertGuess,
} from "../services/io";
import { post } from "../services/requests";
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

  const answer = data.replaceAll("\n", "").replaceAll("\r", "");

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

  if (status.includes("That's the right answer")) {
    markCorrectGuess({ day, part });
  }
}
