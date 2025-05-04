import "./App.css";

function App() {
  return (
    <div className="min-h-screen bg-black text-white flex flex-col items-center justify-center px-4">
      <header className="text-center mb-10">
        <h1 className="text-4xl md:text-6xl font-bold text-yellow-400 mb-4">
          🐆 Bot da FURIA no Telegram
        </h1>
        <p className="text-lg md:text-xl text-gray-300">
          Torça, acompanhe os jogos e interaja com o time em tempo real!
        </p>
      </header>

      <div className="bg-zinc-900 rounded-2xl p-6 max-w-md shadow-lg">
        <h2 className="text-xl font-semibold mb-4">Funcionalidades:</h2>
        <ul className="list-disc list-inside space-y-2 text-gray-200">
          <li>Status ao vivo dos jogos</li>
          <li>Ranking dos jogadores</li>
          <li>Grito de torcida interativo</li>
          <li>Conteúdo especial para fãs</li>
        </ul>

        <a
          href="https://t.me/FURIOSO_fan_bot"
          target="_blank"
          rel="noopener noreferrer"
          className="mt-6 block text-center bg-yellow-400 text-black py-3 rounded-xl font-bold hover:bg-yellow-300 transition"
        >
          Abrir Bot no Telegram
        </a>
      </div>

      <footer className="mt-10 text-sm text-gray-500">
        Projeto fictício para fãs da FURIA - Desenvolvido por Lucas Augusto
      </footer>
    </div>
  );
}

export default App;
