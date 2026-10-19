import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Apna Bot Token yahan dalna hai
BOT_TOKEN =8819282839:AAE12JFWZYUfrx2GOt83EtPRmjJa5rOPOrk

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Main mybot24 hun. 24 ghante online hun ✅")

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Aapne kaha: {update.message.text}")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
    print("Bot chal raha hai...")
    app.run_polling()

if __name__ == "__main__":
    main()
