export async function askBackend(question: string) {
  const res = await fetch(
    process.env.NEXT_PUBLIC_API_URL + "/chat",
    {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: question }),
    }
  );

  if (!res.ok) {
    throw new Error("Backend error");
  }

  const data = await res.json();
  return data.answer;
}
