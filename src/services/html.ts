import { load } from "cheerio";

export function extractPartOne(html: string): string {
  const $ = load(html);
  return $(".day-desc").html() || "";
}

export function extractPartTwo(html: string): string {
  const $ = load(html);
  return $(".day-desc:nth-of-type(2)").html() || "";
}

export function extractAnswerStatus(html: string): string {
  const $ = load(html);
  return $("main > article > p").text() || "";
}
