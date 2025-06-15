from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes
from handlers import help_handler, voice_handler, balance_handler, deposit_handler, referral_handler, proof_handler, plans_handler
from config import BOT_TOKEN

menu_buttons = [
    ["Voice Convert", "Balance"],
    ["Plans", "Deposit Money 💰"],
    ["Referral", "Upload payment Ss"]
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = ReplyKeyboardMarkup(menu_buttons, resize_keyboard=True)
    await update.message.reply_text(
        "🎙 Welcome to *ChoseYou Bot*! Select an option below:",
        parse_mode="Markdown",
        reply_markup=keyboard
    )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_handler))
    app.add_handler(CommandHandler("balance", balance_handler))
    app.add_handler(CommandHandler("plans", plans_handler.plans_handler))  # Plan button
    app.add_handler(CallbackQueryHandler(plans_handler.plan_button_callback))  # Plan callback
    app.add_handler(CommandHandler("deposit", deposit_handler))
    app.add_handler(CommandHandler("referral", referral_handler))

    app.add_handler(MessageHandler(filters.VOICE, voice_handler))
    app.add_handler(MessageHandler(filters.PHOTO, proof_handler))

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()