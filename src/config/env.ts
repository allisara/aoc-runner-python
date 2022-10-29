import * as dotenv from "dotenv";

dotenv.config();

if (!process.env.year || !process.env.token) {
  throw new Error(
    "\n\n------------\n.env FILE NOT FOUND\nCOPY .env.example TO .env AND ADD TOKEN\n---------------"
  );
}

if (process.env.token.length < 128) {
  throw new Error(
    "------------\nTOKEN INVALID\nCOPY FROM AOC SITE COOKIE\n-------------"
  );
}

export const year = process.env.year;
export const token = process.env.token;
