import { MaybeString, Problem } from "../types/types";
import { parseDayPart } from "../utils/parse";

export function testAnswerController(
  useSmallTestSet: boolean,
  problem: MaybeString
) {
  const selectedProblem = problem ? parseDayPart(problem) : "";
}
