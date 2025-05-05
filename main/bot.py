from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🐆 Bem-vindo ao Bot da FURIA, torcedor!\n\n"
        "Comandos disponíveis:\n"
        "/jogo_ao_vivo - Ver status do jogo atual\n"
        "/ranking - Top 5 jogadores da FURIA\n"
        "/torcida - Solte o grito da torcida!"
    )

# Comando /jogo_ao_vivo (mock)
async def jogo_ao_vivo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 Jogo AO VIVO: FURIA x NAVI\n"
        "Mapa: Mirage\n"
        "Placar: FURIA 12 x 9 NAVI\n"
        "Tempo restante: 1:24 (2º half)"
    )

# Comando /ranking (mock)
async def ranking(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ranking_text = "🏆 Top 5 Jogadores da FURIA:\n\n"
    jogadores = ["1. KSCERATO", "2. yuurih", "3. chelo", "4. FalleN", "5. arT"]
    await update.message.reply_text(ranking_text + "\n".join(jogadores))

# Comando /torcida
async def torcida(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 VAAAMO FURIAAAAA! 🔥\n💥💛💪🐆")

# Inicialização do bot
if __name__ == "__main__":
    import os

    TOKEN = "***"  # Substitua pelo seu token do BotFather

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("jogo_ao_vivo", jogo_ao_vivo))
    app.add_handler(CommandHandler("ranking", ranking))
    app.add_handler(CommandHandler("torcida", torcida))

    print("🤖 Bot da FURIA está rodando...")
    app.run_polling()
