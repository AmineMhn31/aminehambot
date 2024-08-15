import os
import logging
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import server
from stay_alive import keep_alive

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.CRITICAL
)

# Get token from environment variable or use the insecure fallback
TOKEN = os.getenv("HAMSTER_BOT_TOKEN", "7474041486:AAFLRJZacez8OyYCn5bxta_itkiHiTZ07MU").strip()
if not TOKEN:
    TOKEN = TOKEN_INSECURE

if not TOKEN:
    logging.critical("No bot token found! Exiting...")
    exit(1)

AUTHORIZED_USERS = []
EXCLUSIVE = False

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="🐹")

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=(
            "🔢Today's Cipher Code 14/08/2024📅:\n"
            "*T ➖*\n"
            "*A ➖🔘*\n"
            "*S 🔘🔘🔘*\n"
            "*K ➖🔘➖*\n"
            "*S 🔘🔘🔘*\n"
            "✅CLAIM 1000000💰\\."
        ),
        parse_mode='MARKDOWNV2'
    )
    
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=(
            "THE COMMANDES ARE:\n"
            "*/bike*\n"
            "*/clone*\n"
            "*/cube*\n"
            "*/train*\n"
            "*/merge*\n"
            "*/all*\n"
            "These will generate 4 keys for their respective games\\."
        ),
        parse_mode='MARKDOWNV2'
    )

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=(
            "You can also set how many keys are generated\\. For example, "
            "*/cube 8* will generate *EIGHT* keys for the cube game\\."
        ),
        parse_mode='MARKDOWNV2'
    )

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="⚠️REMARK⚠️: 🔰 BOT 100% SAFE ✅",
        parse_mode='MARKDOWNV2'
    )
    
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="🇩🇿 🇩🇿 POWERED BY 🇩🇿 🇩🇿",
        parse_mode='MARKDOWNV2'
    )

# Define other command handlers (bike, clone, cube, train, merge, all) similarly
# ...

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    server.logger.info("Server is running. Awaiting users...")

    start_handler = CommandHandler('start', start, run_async=True)
    application.add_handler(start_handler)
    
    bike_handler = CommandHandler('bike', bike, run_async=True)
    application.add_handler(bike_handler)

    clone_handler = CommandHandler('clone', clone, run_async=True)
    application.add_handler(clone_handler)

    cube_handler = CommandHandler('cube', cube, run_async=True)
    application.add_handler(cube_handler)

    train_handler = CommandHandler('train', train, run_async=True)
    application.add_handler(train_handler)

    merge_handler = CommandHandler('merge', merge, run_async=True)
    application.add_handler(merge_handler)
    
    all_handler = CommandHandler('all', all, run_async=True)
    application.add_handler(all_handler)

    application.run_polling()
