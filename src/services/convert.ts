import { NodeHtmlMarkdown } from "node-html-markdown";

const nodeHtmlMarkdown = new NodeHtmlMarkdown();
export function htmlToMarkdown(html: string): string {
  return nodeHtmlMarkdown.translate(html);
}
