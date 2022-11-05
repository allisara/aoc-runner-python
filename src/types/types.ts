type DateUTCSeconds = string | null;

export type MaybeString = string | undefined;

export interface CachedData {
  meta: {
    blockedUntil: DateUTCSeconds;
    currentProblem: string;
  };
  problems: {
    [year: string]: {
      [day: string]: {
        part1: {
          solvedAt: DateUTCSeconds;
          guessedAnswers: string[];
        };
        part2: {
          solvedAt: DateUTCSeconds;
          guessedAnswers: string[];
        };
      };
    };
  };
}

export interface PostPayload {
  level: "1" | "2";
  answer: string;
}

export interface Problem {
  day: string;
  part: "1" | "2";
}
