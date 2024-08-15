import subprocess
import os
import logging
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

from stay_alive import keep_alive

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.CRITICAL
)
logger = logging.getLogger(__name__)

# Keep the server alive
keep_alive()

# Token management based on the OS environment
TOKEN_INSECURE = "YOUR_BOT_TOKEN_HERE"
if os.name == 'posix':
    TOKEN = subprocess.run(["printenv", "HAMSTER_BOT_TOKEN"],
                           text=True,
                           capture_output=True).stdout.strip()
elif os.name == 'nt':
    TOKEN = subprocess.run(["echo", "%HAMSTER_BOT_TOKEN%"],
                           text=True,
                           capture_output=True,
                           shell=True).stdout.strip()
    TOKEN = "" if TOKEN == "%HAMSTER_BOT_TOKEN%" else TOKEN

AUTHORIZED_USERS = []
EXCLUSIVE = False

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="🐹")
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="🔢Today's Cipher Code 13/08/2024📅:\n*I 🔘🔘*\n*N ➖🔘*\n*C ➖🔘➖🔘*\n*O ➖➖➖*\n*M ➖➖*\n*E 🔘* \n✅CLAIM 1000000💰\.",
        parse_mode='MARKDOWNV2'
    )
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="THE COMMANDS ARE:\n*/bike*\n*/clone*\n*/cube*\n*/train*\n*/merge*\n*/all*\nThese will generate 4 keys for their respective games\.",
        parse_mode='MARKDOWNV2'
    )
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="You can also set how many keys are generated. For example, */cube 8* will generate *EIGHT* keys for the cube game\.",
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

async def generate_keys(update: Update, context: ContextTypes.DEFAULT_TYPE, game_id: int):
    if EXCLUSIVE and not update.effective_chat.id in AUTHORIZED_USERS:
        return

    logger.info(f"Generating keys for game {game_id} for client: {update.effective_chat.id}")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="🐹")
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"⌛️Generating⏳...",
                                   parse_mode='MARKDOWNV2')
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"⏱️🙆‍♂ This will only take a moment 🙆‍♂⏱️...",
        parse_mode='MARKDOWNV2'
    )

    no_of_keys = int(context.args[0]) if context.args else 4
    keys = await server.run(chosen_game=game_id, no_of_keys=no_of_keys)
    generated_keys = [f"`{key}`" for key in keys]
    formatted_keys = '\n'.join(generated_keys)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"{formatted_keys}",
                                   parse_mode='MARKDOWNV2')
    logger.info("Message sent to the client.")

async def bike(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await generate_keys(update, context, game_id=1)

async def clone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await generate_keys(update, context, game_id=2)

async def cube(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await generate_keys(update, context, game_id=3)

async def train(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await generate_keys(update, context, game_id=4)

async def merge(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await generate_keys(update, context, game_id=5)

async def all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if EXCLUSIVE and not update.effective_chat.id in AUTHORIZED_USERS:
        return

    logger.info(f"Generating keys for All Games for client: {update.effective_chat.id}")

    await context.bot.send_message(chat_id=update.effective_chat.id, text="🐹")
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Currently generating for all games...",
        parse_mode='MARKDOWNV2'
    )
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"Come Back in about 5-10 minutes.",
                                   parse_mode='MARKDOWNV2')

    no_of_keys = int(context.args[0]) if context.args else 4
    for i in range(4):
        await generate_keys(update, context, game_id=i + 1)

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN or TOKEN_INSECURE).build()
    logger.info("Server is running. Awaiting users...")

    application.add_handler(CommandHandler('start', start, block=False))
    application.add_handler(CommandHandler('bike', bike, block=False))
    application.add_handler(CommandHandler('clone', clone, block=False))
    application.add_handler(CommandHandler('cube', cube, block=False))
    application.add_handler(CommandHandler('train', train, block=False))
    application.add_handler(CommandHandler('merge', merge, block=False))
    application.add_handler(CommandHandler('all', all, block=False))

    application.run_polling()
