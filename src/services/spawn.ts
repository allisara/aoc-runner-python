import { spawn } from "child_process";
import { join } from "path";
import { pythonCommand, year } from "../config/env";
import { Problem } from "../types/types";

export async function runPython(problem: Problem, useFullDataset: boolean) {
  const pyFile = join(
    __dirname,
    `../../problems/${year}/day${problem.day}/p${problem.part}.py`
  );

  let env = process.env;
  if (useFullDataset) {
    env.USE_FULL = "true";
  }

  const child = spawn(pythonCommand, [pyFile], { env });

  let data = "";
  for await (const chunk of child.stdout) {
    data += chunk;
  }
  let error = "";
  for await (const chunk of child.stderr) {
    error += chunk;
  }
  const exitCode = await new Promise((resolve, reject) => {
    console.log(error);
    console.log(data);
    child.on("close", resolve);
  });

  if (exitCode) {
    return { data, isCorrect: false };
  }
  return { data, isCorrect: true };
}
