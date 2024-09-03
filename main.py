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
TOKEN_INSECURE = "7474041486:AAGRj90HoAdC5IF7wx35gYi2qKi2Z9T_1Rw"

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


# ======================== Airdrop Command ==========================
# Define the list of confirmed airdrops

airdrops = [
    {"name": "🍅 Tomarket App", "date": "📅2 September 2024📅", "link": "https://t.me/Tomarket_ai_bot/app?startapp=0000RUJ4"},
    {"name": "🐹 Hamster Kombat", "date": "📅26 September 2024📅", "link": "https://t.me/hamster_kombaT_bot/start?startapp=kentId2136515572"},
    {"name": "🐰 Rocky Rabbit", "date": "📅23 September 2024📅", "link": "https://t.me/rocky_rabbit_bot/play?startapp=frId2136515572"},
    {"name": "🤯 MemeFi App", "date": "📅9 October 2024📅", "link": "https://t.me/memefi_coin_bot/main?startapp=r_15a4e9bdba"},
    {"name": "🌝 TapCoins App", "date": "📅Early September 2024📅", "link": "https://t.me/tapcoinsbot/app?startapp=ref_3EpEkX"},
    {"name": "🚀 X Empire App", "date": "📅end September – mid October 2024📅", "link": "https://t.me/empirebot/game?startapp=hero2136515572"},
    # Add more airdrops as needed
]

# Command handler for /airdrop
async def Airdrops(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = "📣📅🪂 *Confirmed Airdrops Telegram Games Mini Apps September 2024* 🪂📅📣\n\n"
    for airdrop in airdrops:
        message += f"🔹 *{airdrop['name']}*\n"
        message += f"   📅 *Date:* {airdrop['date']}\n"
        message += f"   🌐 [Link]({airdrop['link']})\n\n"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode='MarkdownV2')

# ==================================================================

# ======================== Airdrop Game Command ==========================
# Define the list of games

games = [
    {"name": "😼 CatsGangBot", "link": "https://t.me/catsgang_bot/join?startapp=FB0J8GnDdMO9mZ_cYVS17"},
    {"name": "🐹 Hamster Kombat Bot", "link": "https://t.me/hamster_kombaT_bot/start?startapp=kentId2136515572"},
    {"name": "🚀 MuskEmpireBot", "link": "https://t.me/empirebot/game?startapp=hero2136515572"},
    {"name": "🍅 Tomarket App", "link": "https://t.me/Tomarket_ai_bot/app?startapp=0000RUJ4"},
    {"name": "🐂 Battle Bulls", "link": "https://t.me/battle_games_com_bot/start?startapp=frndId2136515572"},
    {"name": "⭐️ MajorStarsBot", "link": "https://t.me/major/start?startapp=2136515572"},
    {"name": "🤑 BlumCryptoBot", "link": "https://t.me/BlumCryptoBot/app?startapp=ref_nGMDVNruDY"},
    {"name": "⚽️ 1WinToken", "link": "http://t.me/token1win_bot/start?startapp=refId2136515572"},
    {"name": "🤖 TapSwapBot", "link": "https://t.me/tapswap_mirror_1_bot?start=r_2136515572"},
    {"name": "🏎️ OKX Racer", "link": "https://t.me/OKX_official_bot/OKX_Racer?startapp=linkCode_114315151"},
]

# Command handler for /airdropgame
async def miniggapps(update, context):
    message = "🎮 *Available Games for Airdrop* 🎮\n\n"
    for game in games:
        message += f"🔹 [{game['name']}]({game['link']})\n"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode='MarkdownV2')
    
# ===============================================================================================================

# ========================COMBO==========================================
async def fetch_image(url: str) -> BytesIO:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        image_data = BytesIO(response.content)
        return image_data

async def hamstercombo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="https://cointicker.com/wp-content/uploads/2024/09/image-33-1024x537.png")
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


# ========================================tomarketCOMBO==============================================================

# Function to fetch an image from a given URL and return it as a BytesIO object
async def fetch_image(url: str) -> BytesIO:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return BytesIO(response.content)

# Main function that handles the /tomarketcombo command
async def tomarketcombo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    # Send the image first
    image_url = "https://static.bittime.com/cms-static/upload/Tomarket_Daily_Secret_Combo_29_Agustus_Mainkan_Gamenya_e18cd08205.webp"
    await context.bot.send_photo(chat_id=chat_id, photo=image_url)

    # Then send the TomarketDaily Secret message
    secret_message = (
        "🍅 *TomarketDaily Secret* \n\n"
        "1️⃣ x1 Tap tree 🌲\n"
        "2️⃣ x2 Tap Tomato Head 🍅\n"
    )
    await context.bot.send_message(chat_id=chat_id, text=secret_message, parse_mode="MarkdownV2")

    # Check if an image URL is provided in the command arguments
    if context.args:
        url = context.args[0]
        try:
            # Fetch and send the requested image
            image_data = await fetch_image(url)
            img = Image.open(image_data)
            img_format = img.format  # Retain the original image format

            with BytesIO() as output:
                img.save(output, format=img_format)
                output.seek(0)
                await context.bot.send_photo(chat_id=chat_id, photo=InputFile(output, filename=f"image.{img_format.lower()}"))

            await context.bot.send_message(chat_id=chat_id, text="Here is the image you requested.")

        except Exception as e:
            await context.bot.send_message(chat_id=chat_id, text=f"Failed to retrieve image: {e}")

# ===============================MINIGG===================================

async def fetch_video(url: str) -> BytesIO:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        video_data = BytesIO(response.content)
        return video_data

async def minigg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="https://hamster-combo.com/wp-content/uploads/2024/09/img_8930-online-video-cutter.com-1.mp4")
        return

    url = context.args[0]
    try:
        video_data = await fetch_video(url)

        # Assuming the video is in MP4 format
        await context.bot.send_video(chat_id=update.effective_chat.id, video=InputFile(video_data, filename="video.mp4"))

        await context.bot.send_message(chat_id=update.effective_chat.id, text="Here is the video you requested.")

    except Exception as e:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Failed to retrieve video: {e}")

# ========================CIPHER==========================================
async def cipher(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="🐹")

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=(
            "🔢Today's Cipher Code \\(WITHDRAW\\) 02/09/2024📅:\n"
            "*W:  🔘➖➖*\n"
            "*I:  🔘🔘*\n"
            "*T:  ➖*\n"
            "*H:  🔘🔘🔘🔘*\n"
            "*D:  ➖🔘🔘*\n"
            "*R:  🔘➖🔘*\n"
            "*A:  🔘➖*\n"
            "*W:  🔘➖➖*\n"
            "✅CLAIM 1000000💰\."
        ),
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
            "🪂 🔹 /airdrops\n"
            "🕹 🔹 /miniggapps\n"
            "🐹 🔹 /hamstercombo\n"
            "🍅 🆕 🔹 /tomarketcombo\n"
            "🔐 🔹 /cipher\n"
            "🎲 🔹 /minigg\n"
            "🧊 🔹 /cube\n"
            "🚂 🔹 /train\n"
            "🧩 🔹 /merge\n"
            "💃 🔹 /twerk\n"
            "🔮 🔹 /poly\n"
            "🚜 🔹 /trim\n"
            "🍀 🆕 🔹 /zoo\n"
            "☕️ ❌ 🔹 /cafe\n"
            "🔫 ❌ 🔹 /gang\n"
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

async def cube(update: Update, context: ContextTypes.DEFAULT_TYPE, all = False):
    await game_handler(update, context, chosen_game=1, all=all)

async def train(update: Update, context: ContextTypes.DEFAULT_TYPE, all = False):
    await game_handler(update, context, chosen_game=2, all=all)

async def merge(update: Update, context: ContextTypes.DEFAULT_TYPE, all = False):
    await game_handler(update, context, chosen_game=3, all=all)

async def twerk(update: Update, context: ContextTypes.DEFAULT_TYPE, all = False):
    await game_handler(update, context, chosen_game=4, all=all)

async def poly(update: Update, context: ContextTypes.DEFAULT_TYPE, all = False):
    await game_handler(update, context, chosen_game=5, all=all)

async def trim(update: Update, context: ContextTypes.DEFAULT_TYPE, all = False):
    await game_handler(update, context, chosen_game=6, all=all)

async def cafe(update: Update, context: ContextTypes.DEFAULT_TYPE, all = False):
    await game_handler(update, context, chosen_game=7, all=all)

async def zoo(update: Update, context: ContextTypes.DEFAULT_TYPE, all = False):
    await game_handler(update, context, chosen_game=8, all=all)

async def gang(update: Update, context: ContextTypes.DEFAULT_TYPE, all = False):
    await game_handler(update, context, chosen_game=9, all=all)

async def all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if EXCLUSIVE and not update.effective_chat.id in AUTHORIZED_USERS:
        return

    server.logger.info(f"Generating ALL GAMES for client: {update.effective_chat.first_name} - {update.effective_chat.username}: {update.effective_chat.id}")

    await context.bot.send_message(chat_id=update.effective_chat.id, text="🐹")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"⌛️ Currently generating for all games ⏳\.\.\.", parse_mode='MARKDOWNV2')
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"⏰Come Back in about 5\-10 minutes⏰\.", parse_mode='MARKDOWNV2')

    # Send message to the group
    
    # Wait a certain number of seconds between each game
    tasks = [game_handler(update, context, i + 1, True, i * 30) for i in range(9)]
    await asyncio.gather(*tasks)
 # ============================================================================================

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN or TOKEN_INSECURE).build()
    server.logger.info("Server is running. Awaiting users...")

    application.add_handler(CommandHandler('salam', salam, block=False))
    application.add_handler(CommandHandler('news', news, block=False))
    application.add_handler(CommandHandler('Airdrops', Airdrops, block=False))
    application.add_handler(CommandHandler('miniggapps', miniggapps, block=False))
    application.add_handler(CommandHandler('hamstercombo', hamstercombo, block=False))
    application.add_handler(CommandHandler('tomarketcombo', tomarketcombo, block=False))
    application.add_handler(CommandHandler('cipher', cipher, block=False))
    application.add_handler(CommandHandler('minigg', minigg, block=False))
    application.add_handler(CommandHandler('cube', cube, block=False))
    application.add_handler(CommandHandler('train', train, block=False))
    application.add_handler(CommandHandler('merge', merge, block=False))
    application.add_handler(CommandHandler('twerk', twerk, block=False))
    application.add_handler(CommandHandler('poly', poly, block=False))
    application.add_handler(CommandHandler('trim', trim, block=False))
    application.add_handler(CommandHandler('cafe', cafe, block=False))
    application.add_handler(CommandHandler('zoo', zoo, block=False))
    application.add_handler(CommandHandler('gang', gang, block=False))
    application.add_handler(CommandHandler('all', all, block=False))


    application.run_polling()
