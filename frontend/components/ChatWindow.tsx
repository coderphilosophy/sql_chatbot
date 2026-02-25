"use client";

import { useState, useEffect, useRef } from "react";
import { nanoid } from "nanoid";
import { ChatMessage as Message } from "@/types/chat";
import ChatMessage from "./ChatMessage";
import ChatInput from "./ChatInput";
import { askBackend } from "@/lib/api";

export default function ChatWindow() {
  const bottomRef = useRef<HTMLDivElement | null>(null);

  const [messages, setMessages] = useState<Message[]>([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  const send = async (text: string) => {
    const userMsg: Message = {
      id: nanoid(),
      role: "user",
      content: text,
    };

    setMessages((m) => [...m, userMsg]);
    setLoading(true);

    try {
      const reply = await askBackend(text);

      const botMsg: Message = {
        id: nanoid(),
        role: "assistant",
        content: reply,
      };

      setMessages((m) => [...m, botMsg]);
    } catch {
      setMessages((m) => [
        ...m,
        {
          id: nanoid(),
          role: "assistant",
          content: "⚠️ Something went wrong. Please try again.",
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <div className="flex-1 overflow-y-auto bg-[#efeae2] px-4 py-6">
        {messages.map((m) => (
          <ChatMessage key={m.id} message={m} />
        ))}

        {loading && (
          <div className="flex items-center gap-2 text-sm text-neutral-500">
            <span className="h-2 w-2 animate-bounce rounded-full bg-neutral-400" />
            <span className="h-2 w-2 animate-bounce rounded-full bg-neutral-400 [animation-delay:0.15s]" />
            <span className="h-2 w-2 animate-bounce rounded-full bg-neutral-400 [animation-delay:0.3s]" />
          </div>
        )}

        {/* 👇 Scroll anchor MUST be inside scroll container */}
        <div ref={bottomRef} />
      </div>

      <ChatInput onSend={send} disabled={loading} />
    </>
  );
}
