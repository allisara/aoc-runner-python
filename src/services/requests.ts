import { token } from "../config/env";
import { PostPayload } from "../types/types";

/**
 * Accepts url and returns get request with token from env attached
 * @param url
 * @returns
 */
export const get = async (url: string): Promise<string> => {
  const result = await fetch(url, {
    headers: new Headers({
      "content-type": "application/json",
      cookie: `session=${token};`,
    }),
  });

  const data = await result.text();
  return data;
};

export const post = async (url: string, body: PostPayload): Promise<string> => {
  const result = await fetch(url, {
    method: "POST",
    body: `level=${body.level}&answer=${body.answer}`,
    headers: new Headers({
      "content-type": "application/x-www-form-urlencoded",
      cookie: `session=${token};`,
    }),
  });

  const data = await result.text();
  return data;
};
