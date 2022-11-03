import { CachedData } from "../types/types";
import stateJson from "../assets/state.json";
import { copyFile, writeFile } from "fs/promises";
import { join } from "path";
import { constants, existsSync, mkdirSync, stat } from "fs";
import { year } from "../config/env";

// const state: CachedData = stateRaw;
const state: CachedData = stateJson;

export function initDay(day: string) {
  state.problems[year] = state.problems[year] || {};
  state.problems[year][`day${day}`] = {
    part1: {
      solvedAt: null,
      guessedAnswers: [],
    },
    part2: {
      solvedAt: null,
      guessedAnswers: [],
    },
  };

  updateJSON();
}

async function updateJSON() {
  return writeFile(
    join(__dirname, "../assets/state.json"),
    JSON.stringify(state),
    "utf-8"
  );
}

export async function createFolder(path: string): Promise<void> {
  if (!existsSync(path)) {
    mkdirSync(path, { recursive: true });
  }
}

export function fileWriter(path: string) {
  return (filename: string, body: any) =>
    writeFile(path + filename, body, "utf-8");
}

export async function copyBoilerplateFiles(problemFolder: string) {
  const boilerplateFolder = join(__dirname, "../assets/boilerplate/");
  try {
    await copyFile(
      boilerplateFolder + "p1.py",
      problemFolder + "p1.py",
      constants.COPYFILE_EXCL
    );
  } catch (_err) {}
  try {
    await copyFile(
      boilerplateFolder + "p2.py",
      problemFolder + "p2.py",
      constants.COPYFILE_EXCL
    );
  } catch (_err) {}
  try {
    await copyFile(
      boilerplateFolder + "shared.py",
      problemFolder + "shared.py",
      constants.COPYFILE_EXCL
    );
  } catch (_err) {}
  try {
    await copyFile(
      boilerplateFolder + "dataset-short.txt",
      problemFolder + "dataset-short.txt",
      constants.COPYFILE_EXCL
    );
  } catch (_err) {}
}
