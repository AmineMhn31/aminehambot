import subprocess
import os
import logging
import asyncio
import httpx
import re
from io import BytesIO
import aiohttp
from telegram import Update, InputFile
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import server
import requests
from stay_alive import keep_alive

# Paste Token Here if you don't wanna put it in an env. variable for some reason
TOKEN_INSECURE = "7474041486:AAFLRJZacez8OyYCn5bxta_itkiHiTZ07MU"

if os.name == 'posix':
    TOKEN = subprocess.run(["printenv", "HAMSTER_BOT_TOKEN"], text=True, capture_output=True).stdout.strip()
elif os.name == 'nt':
    TOKEN = subprocess.run(["echo", "%HAMSTER_BOT_TOKEN%"], text=True, capture_output=True, shell=True).stdout.strip()
    TOKEN = "" if TOKEN == "%HAMSTER_BOT_TOKEN%" else TOKEN


AUTHORIZED_USERS = []
EXCLUSIVE = False

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.WARN
)

# ========================COMBO==========================================
async def fetch_image(url: str) -> BytesIO:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        image_data = BytesIO(response.content)
        return image_data

async def combo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="https://raw.githubusercontent.com/AmineMhn31/aminehambot/main/combo29.png")
        return

    url = context.args[0]
    try:
        image_data = await fetch_image(url)
        img = Image.open(image_data)
        img_format = img.format  # Get the image format to retain the original extension

        with BytesIO() as output:
            img.save(output, format=img_format)
            output.seek(0)
            await context.bot.send_photo(chat_id=update.effective_chat.id, photo=InputFile(output, filename=f"image.{img_format.lower()}"))

        await context.bot.send_message(chat_id=update.effective_chat.id, text="Here is the image you requested.")

    except Exception as e:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Failed to retrieve image: {e}")

# ========================Mini Game==========================================
async def fetch_image(url: str) -> BytesIO:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        image_data = BytesIO(response.content)
        return image_data

async def minigg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="https://raw.githubusercontent.com/AmineMhn31/aminehambot/main/minigame.png")
        return

    url = context.args[0]
    try:
        image_data = await fetch_image(url)
        img = Image.open(image_data)
        img_format = img.format  # Get the image format to retain the original extension

        with BytesIO() as output:
            img.save(output, format=img_format)
            output.seek(0)
            await context.bot.send_photo(chat_id=update.effective_chat.id, photo=InputFile(output, filename=f"image.{img_format.lower()}"))

        await context.bot.send_message(chat_id=update.effective_chat.id, text="Here is the image you requested.")

    except Exception as e:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Failed to retrieve image: {e}")

# ========================CIPHER==========================================
async def cipher(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="🐹")

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=
        "🔢Today's Cipher Code \(FIGHTY\) 29/08/2024📅:\n\*F:  🔘🔘➖🔘\*\n\*I:  🔘🔘\*\n\*G:  ➖➖🔘\*\n\*H:  🔘🔘🔘🔘\*\n\*T:  ➖\*\n\*Y:  ➖🔘➖➖\*\n✅CLAIM 1000000💰\.",
        parse_mode='MARKDOWNV2'
    )


    # ==================================================================

# ========================NEWS==========================================
async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Should make this a Database probably
    # with open('user_ids','a') as file:
    #     file.write(f"{update.effective_chat.first_name} : {update.effective_chat.id}\n")

    await context.bot.send_message(chat_id=update.effective_chat.id, text="🐹")

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="""
    🐹 السادة الرؤساء التنفيذيون،

    🤩🪂💸 احجزوا موعدًا لحدثي TGE و AirDrop الخاصين بلعبة Hamster Kombat — 26 سبتمبر\! 💸🪂🤩 \!
    """,
        parse_mode='MARKDOWNV2'
    )

    # ==================================================================

async def salam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Should make this a Database probably
    # with open(f'{os.path.dirname(__file__)}/user_ids','a') as file:
    #     file.write(f"{datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')} {update.effective_chat.first_name}, {update.effective_chat.username}, {update.effective_chat.id}\n")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="🐹")
    
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=(
            "🤖The Commands are⚙️\:\n"
            "👋🏻 🔹 /salam\n"
            "📰 🔹 /news\n"
            "🖼️ 🔹 /combo\n"
            "🔐 🔹 /cipher\n"
            "🎲 🔹 /minigg\n"
            "🚴 🔹 /bike\n"
            "🧊 🔹 /cube\n"
            "🚂 🔹 /train\n"
            "🧩 🔹 /merge\n"
            "💃 🔹 /twerk\n"
            "🔮 🔹 /poly\n"
            "🏎️ 🔹 /mud\n"
            "🚜 🔹 /trim\n"
            "☕️ 🔹 /cafe\n"
            "🎮 🔹 /all\n"
            "These will generate 4 keys for their respective games\\."
        ),
        parse_mode='MARKDOWNV2'
    )


    
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="🤖You can also set how many keys are generated\. For example, */cube 8* will generate *EIGHT* keys for the cube game🤖\.",
        parse_mode='MARKDOWNV2'
        )
    await context.bot.send_message(chat_id=update.effective_chat.id,
       text=" ⚠️REMARK⚠️ : 🔰 BOT 100% SAFE ✅",
       parse_mode='MARKDOWNV2')
    await context.bot.send_message(chat_id=update.effective_chat.id,
       text="🇩🇿 🇩🇿 POWERED BY 🇩🇿 🇩🇿",
       parse_mode='MARKDOWNV2')


async def game_handler(
    update: Update, 
    context: ContextTypes.DEFAULT_TYPE,
    chosen_game: int, 
    all: bool, 
    delay = 0
    ):
    if EXCLUSIVE and not update.effective_chat.id in AUTHORIZED_USERS:
        await context.bot.send_message(
            chat_id=update.effective_chat.id, 
            text="Clone this bot from the [github](https://github.com/AmineMhn31/aminehambot) repo and follow the instructions to create your own bot\.",
            parse_mode='MARKDOWNV2'
        )
        with open(f'{os.path.dirname(__file__)}/unauthorized','a') as file:
            unauthorized_message = f"Unauthorized User: {update.effective_chat.first_name} - {update.effective_chat.username}: {update.effective_chat.id}"
            server.logger.warning(unauthorized_message)
            file.write(f"{datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')} {unauthorized_message}\n")
        return

    # delay for the /all command
    await asyncio.sleep(delay)
    server.logger.info(f"Delay for {delay} seconds")


    server.logger.info(f"Generating for client: {update.effective_chat.first_name} - {update.effective_chat.username}: {update.effective_chat.id}")
    if not all:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="🐹")
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"⌛️Generating⏳\.\.\.", parse_mode='MARKDOWNV2')
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"⏱️🙆‍♂ This will only take a moment 🙆‍♂⏱️\.\.\.", parse_mode='MARKDOWNV2')

    
    no_of_keys = int(context.args[0]) if context.args else 4
    keys = await server.run(chosen_game=chosen_game, no_of_keys=no_of_keys)
    generated_keys = [f"`{key}`" for key in keys]
    formatted_keys = '\n'.join(generated_keys)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"{formatted_keys}", parse_mode='MARKDOWNV2')
    server.logger.info("Message sent to the client.")

async def bike(update: Update, context: ContextTypes.DEFAULT_TYPE, all = False):
    await game_handler(update, context, chosen_game=1, all=all)

async def cube(update: Update, context: ContextTypes.DEFAULT_TYPE, all = False):
    await game_handler(update, context, chosen_game=2, all=all)

async def train(update: Update, context: ContextTypes.DEFAULT_TYPE, all = False):
    await game_handler(update, context, chosen_game=3, all=all)

async def merge(update: Update, context: ContextTypes.DEFAULT_TYPE, all = False):
    await game_handler(update, context, chosen_game=4, all=all)

async def twerk(update: Update, context: ContextTypes.DEFAULT_TYPE, all = False):
    await game_handler(update, context, chosen_game=5, all=all)

async def poly(update: Update, context: ContextTypes.DEFAULT_TYPE, all = False):
    await game_handler(update, context, chosen_game=6, all=all)

async def mud(update: Update, context: ContextTypes.DEFAULT_TYPE, all = False):
    await game_handler(update, context, chosen_game=7, all=all)

async def trim(update: Update, context: ContextTypes.DEFAULT_TYPE, all = False):
    await game_handler(update, context, chosen_game=8, all=all)

async def cafe(update: Update, context: ContextTypes.DEFAULT_TYPE, all = False):
    await game_handler(update, context, chosen_game=9, all=all)

async def all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if EXCLUSIVE and not update.effective_chat.id in AUTHORIZED_USERS:
        return

    server.logger.info(f"Generating ALL GAMES for client: {update.effective_chat.first_name} - {update.effective_chat.username}: {update.effective_chat.id}")

    await context.bot.send_message(chat_id=update.effective_chat.id, text="🐹")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"⌛️ Currently generating for all games ⏳\.\.\.", parse_mode='MARKDOWNV2')
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"⏰Come Back in about 5\-10 minutes⏰\.", parse_mode='MARKDOWNV2')

    # Wait a certain number of seconds between each game
    tasks = [game_handler(update, context, i + 1, True, i * 30) for i in range(10)]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN or TOKEN_INSECURE).build()
    server.logger.info("Server is running. Awaiting users...")

    application.add_handler(CommandHandler('salam', salam, block=False))
    application.add_handler(CommandHandler('news', news, block=False))
    application.add_handler(CommandHandler('combo', combo, block=False))
    application.add_handler(CommandHandler('cipher', cipher, block=False))
    application.add_handler(CommandHandler('minigg', minigg, block=False))
    application.add_handler(CommandHandler('bike', bike, block=False))
    application.add_handler(CommandHandler('cube', cube, block=False))
    application.add_handler(CommandHandler('train', train, block=False))
    application.add_handler(CommandHandler('merge', merge, block=False))
    application.add_handler(CommandHandler('twerk', twerk, block=False))
    application.add_handler(CommandHandler('poly', poly, block=False))
    application.add_handler(CommandHandler('mud', mud, block=False))
    application.add_handler(CommandHandler('trim', trim, block=False))
    application.add_handler(CommandHandler('cafe', cafe, block=False))
    application.add_handler(CommandHandler('all', all, block=False))


    application.run_polling()
