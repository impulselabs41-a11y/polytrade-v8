export default function Home() {
  return (
    <div className="p-8 max-w-7xl mx-auto">
      <h1 className="text-5xl font-bold text-emerald-400 mb-2">polytrade-v8</h1>
      <p className="text-zinc-400 text-xl mb-8">6-Layer Polymarket Paper Trading Bot</p>
      
      <div className="grid grid-cols-3 gap-6">
        <div className="bg-zinc-900 p-6 rounded-2xl">
          <h2 className="text-emerald-400 text-sm font-mono">STATUS</h2>
          <p className="text-4xl font-bold text-white mt-2">PAPER MODE</p>
          <p className="text-zinc-400">Real trading disabled</p>
        </div>
        
        <div className="bg-zinc-900 p-6 rounded-2xl">
          <h2 className="text-emerald-400 text-sm font-mono">SCANNER</h2>
          <a href="/scanner" className="block mt-4 text-xl hover:text-emerald-300">
            → Open Live Market Scanner
          </a>
        </div>
        
        <div className="bg-zinc-900 p-6 rounded-2xl">
          <h2 className="text-emerald-400 text-sm font-mono">PORTFOLIO</h2>
          <a href="/portfolio" className="block mt-4 text-xl hover:text-emerald-300">
            → View Paper Portfolio
          </a>
        </div>
      </div>

      <div className="mt-12 text-center text-zinc-500 text-sm">
        Backend running at <span className="font-mono">http://localhost:8000</span><br />
        Scanner starts automatically in background
      </div>
    </div>
  );
}
