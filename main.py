import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ChatJoinRequestHandler, ContextTypes

TOKEN = os.getenv("TOKEN")

FIRST_CHANNEL = "https://t.me/+c8LLtYfFtYJkN2I8"
SECOND_CHANNEL = "https://t.me/+ep52Zo7DFK4yMzdk"

async def join_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.chat_join_request.from_user

    # Envoi du message privé automatique avec 2 liens
    await context.bot.send_message(
        chat_id=user.id,
        text=(
            "🚨 ALERTE GROSSE CONFIANCE 🚨\n\n"
            "🔥 Voici mes 2 meilleurs canaux du moment :\n\n"
            f"1️⃣ Canal bonus : {FIRST_CHANNEL}\n"
            f"2️⃣ Canal Montante : {SECOND_CHANNEL}\n\n"
            "📲 Rejoins les 2 pour ne rien manquer."
        )
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(ChatJoinRequestHandler(join_request))

print("Bot 2 liens lancé ✅")
app.run_polling()
