import { MaybeString, Problem } from "../types/types";

export function parseDayPart(str: string): Problem | undefined {
  // input example => d12p2

  if (!str) {
    return;
  }

  const [day, part] = str.slice(1).split("p");
  return { day, part };
}
