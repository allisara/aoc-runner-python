type DateUTCSeconds = string | null;

export interface CachedData {
  [year: string]: {
    [questionNum: string]: {
      blockedUntil: DateUTCSeconds;
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
}

export interface PostPayload {
  level: 1 | 2;
  answer: string;
}
