"use client";

import AppShell from "@/components/AppShell";
import Header from "@/components/Header";
import ChatWindow from "@/components/ChatWindow";

export default function Home() {
  return (
    <AppShell>
      <Header />
      <ChatWindow />
    </AppShell>
  );
}

