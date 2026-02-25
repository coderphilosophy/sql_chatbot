export default function Header() {
  return (
    <header className="flex items-center gap-3 border-b bg-[#f7f8fa] px-4 py-3">
      <div className="flex h-9 w-9 items-center justify-center rounded-full bg-green-500 text-white font-semibold">
        AI
      </div>

      <div>
        <h1 className="text-sm font-medium text-neutral-500">
          AI SQL Assistant
        </h1>
        <p className="text-xs text-neutral-500">
          Ask questions about your database
        </p>
      </div>
    </header>
  );
}
