export interface CachedData {
  [year: string]: {
    [questionNum: string]: {
      guessedAnswers: string[];
      questionData: string;
    };
  };
}
