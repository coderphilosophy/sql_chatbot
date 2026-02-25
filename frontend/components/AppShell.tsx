export default function AppShell({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="flex min-h-screen w-full items-center justify-center bg-[#f0f2f5]">
      <div className="flex h-[90vh] w-full max-w-3xl flex-col rounded-lg bg-white shadow-md">
        {children}
      </div>
    </div>
  );
}
