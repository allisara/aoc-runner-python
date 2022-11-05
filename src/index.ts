import { submitAnswerController } from "./controllers/answer";
import { downloadController } from "./controllers/download";
import { MaybeString } from "./types/types";
import {
  testAnswerController,
  testFullAnswerController,
} from "./controllers/test-answer";

const commands = {
  download: downloadController,
  answer: submitAnswerController,
  test: testAnswerController,
  "test-full": testFullAnswerController,
};

const [command, arg] = process.argv.slice(2) as [
  keyof typeof commands,
  MaybeString
];

commands[command](arg);
