"use client";

import { ChatMessage as Message } from "@/types/chat";
import clsx from "clsx";
import ReactMarkdown from "react-markdown";


export default function ChatMessage({ message }: { message: Message }) {
  const isUser = message.role === "user";

  return (
    <div
      className={clsx(
        "flex w-full mb-2",
        isUser ? "justify-end" : "justify-start"
      )}
    >
      <div
        className={clsx(
          "max-w-[75%] whitespace-pre-wrap rounded-lg px-4 py-2 text-sm leading-relaxed shadow-sm",
          isUser
            ? "bg-green-500 text-white rounded-br-none"
            : "bg-white text-neutral-900 rounded-bl-none"
        )}
      >
        <ReactMarkdown
            components={{
                table: ({ children }) => (
                <table className="mt-2 w-full border-collapse border border-neutral-300 text-xs">
                    {children}
                </table>
                ),
                th: ({ children }) => (
                <th className="border border-neutral-300 bg-neutral-100 px-2 py-1 text-left">
                    {children}
                </th>
                ),
                td: ({ children }) => (
                <td className="border border-neutral-300 px-2 py-1">
                    {children}
                </td>
                ),
                code: ({ children }) => (
                <code className="rounded bg-neutral-100 px-1 py-0.5 text-xs">
                    {children}
                </code>
                ),
            }}
            >
            {message.content}
        </ReactMarkdown>

      </div>
    </div>
  );
}
