import { runPython } from "../services/spawn";
import { MaybeString, Problem } from "../types/types";
import { parseDayPart } from "../utils/parse";

export function testFullAnswerController(problem: MaybeString) {
  return testAnswerController(problem, true);
}

export async function testAnswerController(
  problem: MaybeString,
  testFullDataset = false
) {
  const dayPart = parseDayPart(problem);
  if (!dayPart) {
    console.log(
      "Day/Part # not entered\n'npm run test d#p#' to test a specific problem"
    );
    return;
  }

  const { data, isCorrect } = await runPython(dayPart, testFullDataset);
  // console.log({ data, isCorrect });
}
