import { Problem } from "../types/types";

export function parseDayPart(str?: string): Problem | undefined {
  // input example => d12p2

  if (!str) {
    return;
  }

  const [day, part] = str.slice(1).split("d") as [string, "1" | "2"];
  return { day, part };
}
