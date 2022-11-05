import * as dotenv from "dotenv";

dotenv.config();
{
}

if (!process.env.YEAR || !process.env.TOKEN || !process.env.PYTHON_COMMAND) {
  throw new Error(
    "\n\n------------\n.env FILE NOT FOUND\nCOPY .env.example TO .env AND ADD TOKEN\n---------------"
  );
}

if (process.env.TOKEN.length < 128) {
  throw new Error(
    "------------\nTOKEN INVALID\nCOPY FROM AOC SITE COOKIE\n-------------"
  );
}

export const year = process.env.YEAR;
export const token = process.env.TOKEN;
export const pythonCommand = process.env.PYTHON_COMMAND;
