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
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, Application
import server
import requests
from stay_alive import keep_alive
from dotenv import load_dotenv


# Paste Token Here if you don't wanna put it in an env. variable for some reason
#TOKEN_INSECURE = ""

load_dotenv()

TOKEN_INSECURE = os.getenv("MY_BOT_TOKEN")

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


# ========================hamsterCOMBO==========================================

# Function to fetch an image from a given URL and return it as a BytesIO object
async def fetch_image(url: str) -> BytesIO:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return BytesIO(response.content)

# Main function that handles the /hamstercombo command
async def hamstercombo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    # Send the image first
    image_url = "https://cointicker.com/wp-content/uploads/2024/09/GXRm96gXYAEW186.jpg"
    await context.bot.send_photo(chat_id=chat_id, photo=image_url)

    # Then send the Hamster Combo Secret message
    secret_message = (
        "🐹 *Hamster Combo: 12.09.2024* 🐹\n\n"
        "Join us here: [🐹 Hamster Kombat Bot](https://t.me/hamster_kombaT_bot/start?startapp=kentId2136515572)"
    )
    await context.bot.send_message(chat_id=chat_id, text=secret_message, parse_mode="Markdown")  # Using basic Markdown

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
    image_url = "https://imagedelivery.net/4-5JC1r3VHAXpnrwWHBHRQ/cf16bfed-31e6-4a0b-f6c0-ac2909129f00/public"
    await context.bot.send_photo(chat_id=chat_id, photo=image_url)

    # Then send the TomarketDaily Secret message
    secret_message = (
        "🍅 *TomarketDaily Secret* \n\n"
        "1️⃣ x2 Tap CATS 🐈\n"
        "2️⃣ x2 Tap TREE 🌲\n"
        "Join us here: [🍅 Tomarket Bot](https://t.me/Tomarket_ai_bot/app?startapp=0000RUJ4)"
    )
    await context.bot.send_message(chat_id=chat_id, text=secret_message, parse_mode="Markdown")

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


# ========================================MAJORCOMBO==============================================================

# Function to fetch an image from a given URL and return it as a BytesIO object
async def fetch_image(url: str) -> BytesIO:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return BytesIO(response.content)

# Main function that handles the /tomarketcombo command
async def majorcombo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    # Send the image first
    image_url = "https://cointicker.com/wp-content/uploads/2024/09/GXPJIQnW0AAYwn5.jpg"
    await context.bot.send_photo(chat_id=chat_id, photo=image_url)

    # Then send the TomarketDaily Secret message
    secret_message = (
        "⭐️ * Major Combo: 12.09.2024* ⭐️\n\n"
        "✅ Get 5000 stars with Major Durov Puzzle ✅\n"
        "Join us here: [⭐️ MajorStarsBot](https://t.me/major/start?startapp=2136515572)"
    )
    await context.bot.send_message(chat_id=chat_id, text=secret_message, parse_mode="Markdown")

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
            
# ========================rocky rabbit COMBO==========================================

# Function to fetch an image from a given URL and return it as a BytesIO object
async def fetch_image(url: str) -> BytesIO:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return BytesIO(response.content)

# Main function that handles the /tomarketcombo command
async def rockyrabbitcombo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    # Send the image first
    image_url = "https://cointicker.com/wp-content/uploads/2024/09/image-192-1024x596.png"
    await context.bot.send_photo(chat_id=chat_id, photo=image_url)

    # Then send the TomarketDaily Secret message
    secret_message = (
        "🐰 * Rocky Rabbit Combo: 12.09.2024* 🐇\n\n"
        "Join us here: [🐰 Rocky Rabbit Bot](https://t.me/rocky_rabbit_bot/play?startapp=frId2136515572)"
        
    )
    await context.bot.send_message(chat_id=chat_id, text=secret_message, parse_mode="Markdown")

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



# ========================rocky rabbit EGGS==========================================

# Function to fetch an image from a given URL and return it as a BytesIO object
async def fetch_image(url: str) -> BytesIO:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return BytesIO(response.content)

# Main function that handles the /tomarketcombo command
async def rockyrabbiteggs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    # Send the image first
    image_url = "https://cointicker.com/wp-content/uploads/2024/09/image-183-1024x410.png"
    await context.bot.send_photo(chat_id=chat_id, photo=image_url)

    # Then send the TomarketDaily Secret message
    secret_message = (
        "🐰 * Rocky Rabbit Eggs: 12.09.2024* 🐇\n\n"
        "Join us here: [🐰 Rocky Rabbit Bot](https://t.me/rocky_rabbit_bot/play?startapp=frId2136515572)"
        
    )
    await context.bot.send_message(chat_id=chat_id, text=secret_message, parse_mode="Markdown")

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
            
#==============================rocky rabbit enigma========================

# Function to fetch an image from a given URL and return it as a BytesIO object
async def fetch_image(url: str) -> BytesIO:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return BytesIO(response.content)

# Main function that handles the /tomarketcombo command
async def rockyrabbitenigma(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    # Send the image first
    image_url = "https://cointicker.com/wp-content/uploads/2024/09/image-198-1024x1005.png"
    await context.bot.send_photo(chat_id=chat_id, photo=image_url)

    # Then send the TomarketDaily Secret message
    secret_message = (
        "🐰 * Rocky Rabbit ENIGMA: 12.09.2024* 🐇\n\n"
        "Join us here: [🐰 Rocky Rabbit Bot](https://t.me/rocky_rabbit_bot/play?startapp=frId2136515572)"
        
    )
    await context.bot.send_message(chat_id=chat_id, text=secret_message, parse_mode="Markdown")

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

# ========================================BLUM CODE==============================================================

# Function to fetch an image from a given URL and return it as a BytesIO object
async def fetch_image(url: str) -> BytesIO:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return BytesIO(response.content)

# Main function that handles the /tomarketcombo command
async def blumcode(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    # Send the image first
    image_url = "https://coinmozo.com/wp-content/uploads/2024/09/BITCOIN-LAUCH-DATE-94-1024x597.jpg"
    await context.bot.send_photo(chat_id=chat_id, photo=image_url)

    # Then send the TomarketDaily Secret message
    secret_message = (
        "🏴‍☠️ *BLUM Daily Video code* \n\n"
        "▶️ BLUM Forkes Explained? – Code: GO GET ✅\n"
        "▶️ How to analyze crypto? – Code: VALUE ✅\n"
        "Join us here: [🏴‍☠️ BLUM Bot](https://t.me/BlumCryptoBot/app?startapp=ref_nGMDVNruDY)"
    )
    await context.bot.send_message(chat_id=chat_id, text=secret_message, parse_mode="Markdown")

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
        await context.bot.send_message(chat_id=update.effective_chat.id, text="https://hamster-combo.com/wp-content/uploads/2024/09/11111111-online-video-cutter.com_.mp4")
        return

    url = context.args[0]
    try:
        video_data = await fetch_video(url)

# Then send the Hamster Combo Secret message
    secret_message = (
        "🐹 *Guide Daily Mini Game in Hamster Kombat* 🐹\n\n"
        "Join us here: [🐹 Hamster Kombat Bot](https://t.me/hamster_kombaT_bot/start?startapp=kentId2136515572)"
    )
    await context.bot.send_message(chat_id=chat_id, text=secret_message, parse_mode="Markdown")  # Using basic Markdown
        
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
            "🔢Today's Cipher Code \\(INSPIRE\\) 12/09/2024📅:\n"
            "*I:  🔘🔘*\n"
            "*N:  ➖🔘*\n"
            "*S:  🔘🔘🔘*\n"
            "*P:  🔘➖➖🔘*\n"
            "*I:  🔘🔘*\n"
            "*R:  🔘➖🔘*\n"
            "*E:  🔘*\n"
            "✅ Activate cipher here: [🐹 Hamster Kombat Bot](https://t.me/hamster_kombaT_bot/start?startapp=kentId2136515572)"
        ),
        parse_mode='MARKDOWN'
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
    

#================================================NEWS=========================================================

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        # First news: Hamster on Bybit
        image_url_hamster = 'https://coinchapter.com/wp-content/uploads/2024/09/Screenshot_2024-09-03-20-27-01-144_com.android.chrome.png'
        
        hamster_caption = (
            "💥 *$HMSTR على BYBIT* 💥\n\n"
            "😎 يا له من يوم رائع! يسعدنا أن نعلن أن *$HMSTR* ستكون متاحة على بورصة العملات المشفرة *BYBIT*!\n\n"
            "😉 إليك رمز الإحالة لأفضل الرؤساء التنفيذيين: *BYBITHAMSTER*\n\n"
            "🧡 ترقبوا الجديد!\n\n"
            "#TheCryptoArk #BybitListing"
        )

        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=image_url_hamster,
            caption=hamster_caption,
            parse_mode='Markdown'
        )

        # Second news: Tomarket Community Update
#async def tomarket_news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #try:
        # Image URL for Tomarket Community Update
        image_url_tomarket = 'https://cointicker.com/wp-content/uploads/2024/08/image-368-1024x576.png'
        
        # Caption for the Tomarket Community Update, formatted with MarkdownV2
        tomarket_caption = (
            "💥🍅 *Dear Tomarket Community* 🍅💥\n\n"
            "نحن ممتنون جدًا لحماسك ودعمك بينما نصل إلى معالم جديدة معًا\\.\n"
            "يسعدنا مشاركة بعض التحديثات المهمة معك\\.\n\n"
            "*كما ذكرنا، تم الانتهاء من اللقطة: 2 سبتمبر، 23:59 HRS \\(GMT\\+8\\)*\n\n"
            "لقد أكملنا أول لقطة رئيسية لدينا، وتم منح *نجوم Tomarket* الخاصة بك بناءً على مشاركتك في هذه الأنشطة الرئيسية:\n\n"
            "1️⃣\\. نتائج لعبة Drop\n"
            "2️⃣\\. تسجيل الدخول اليومي\n"
            "3️⃣\\. تكرار زراعة \\$TOMATO\n"
            "4️⃣\\. رمز الغموض اليومي\n"
            "5️⃣\\. إكمال المهام\n"
            "6️⃣\\. الإحالات\n\n"
            "كلما فعلت هذه الأشياء أكثر، زادت مكافآتك! "
            "ستستمر هذه الأنشطة في التأثير على *نجوم Tomarket* والمكافآت الخاصة بك حتى بعد اللقطة\\.\n\n"
            "*مقدمة عن نظام المستويات*\n\n"
            "نحن متحمسون لإطلاق *نظام المستويات*، والذي سيحدد كمية الإنزال الجوي\\. "
            "إذا كان بإمكانك رؤية مستواك، فأنت مؤهل للإنزال الجوي\\.\n\n"
            "تم استخدام *نجوم Tomarket* السابقة لديك تلقائيًا للارتقاء إلى المستوى الأعلى\\.\n\n"
            "يتيح لك هذا النظام الارتقاء إلى المستوى الأعلى من خلال التفاعل مع المنصة، "
            "مما يمنحك الفرصة لتجاوز الآخرين وكسب المزيد من الإنزالات الجوية! "
            "سيكون *نظام المستويات* نشطًا حتى TGE، لذا استغل هذه الفترة لتأمين مكانك الأول والحصول على أعلى تخصيص\\.\n\n"
            "لقد سأل العديد منكم عن *Wallet Connect*—لا داعي للقلق حتى الآن\\. "
            "لا يزال لديك الوقت لربط محفظتك للحصول على الجوائز والإنزالات الجوية القادمة\\.\n\n"
            "Tomarket 🍅\n\n"
            "#tomarket #tomato"
        )

        # Sending the photo with the caption
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=image_url_tomarket,
            caption=tomarket_caption,
            parse_mode='MarkdownV2'
        )

    except Exception as e:
        # Logging any errors that occur
        logger.error(f"Error in tomarket_news command: {e}")
        # Sending an error message to the user
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Sorry, there was an error processing your request.",
            parse_mode='MarkdownV2'
        )


# ==================================================================


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
            "⭐️ 🔹 /majorcombo\n"
            "🍅 🆕 🔹 /tomarketcombo\n"
            "🐰 🆕 🔹 /rockyrabbitcombo\n"
            "🐣 🆕 🔹 /rockyrabbiteggs\n"
            "🐰 🔐 🔹 /rockyrabbitenigma\n"
            "🏴‍☠️ 🆕 🔹 /blumcode\n"
            "🔐 🔹 /cipher\n"
            "🎲 🔹 /minigg\n"
            "🧊 🔹 /cube\n"
            "🚂 🔹 /train\n"
            "🧩 🔹 /merge\n"
            "💃 🔹 /twerk\n"
            "🔮 🔹 /poly\n"
            "🚜 🔹 /trim\n"
            "🍀 🔹 /zoo\n"
            "⚔️ 🆕 🔹 /fluff\n"
            "🃏 🆕 🔹 /tile\n"
            "🛖 🆕 🔹 /stone\n"
            "🐧 🆕 🔹 /bounce\n"
   #         "☕️ ❌ 🔹 /cafe\n"
   #         "🔫 ❌ 🔹 /gang\n"
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

#async def cafe(update: Update, context: ContextTypes.DEFAULT_TYPE, all = False):
 #   await game_handler(update, context, chosen_game=7, all=all)

async def zoo(update: Update, context: ContextTypes.DEFAULT_TYPE, all = False):
    await game_handler(update, context, chosen_game=8, all=all)

#async def gang(update: Update, context: ContextTypes.DEFAULT_TYPE, all = False):
 #   await game_handler(update, context, chosen_game=9, all=all)

async def fluff(update: Update, context: ContextTypes.DEFAULT_TYPE, all = False):
    await game_handler(update, context, chosen_game=10, all=all)

async def tile(update: Update, context: ContextTypes.DEFAULT_TYPE, all = False):
    await game_handler(update, context, chosen_game=11, all=all)

async def stone(update: Update, context: ContextTypes.DEFAULT_TYPE, all = False):
    await game_handler(update, context, chosen_game=12, all=all)

async def bounce(update: Update, context: ContextTypes.DEFAULT_TYPE, all = False):
    await game_handler(update, context, chosen_game=13, all=all)

async def all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if EXCLUSIVE and not update.effective_chat.id in AUTHORIZED_USERS:
        return

    server.logger.info(f"Generating ALL GAMES for client: {update.effective_chat.first_name} - {update.effective_chat.username}: {update.effective_chat.id}")

    await context.bot.send_message(chat_id=update.effective_chat.id, text="🐹")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"⌛️ Currently generating for all games ⏳\.\.\.", parse_mode='MARKDOWNV2')
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"⏰Come Back in about 5\-10 minutes⏰\.", parse_mode='MARKDOWNV2')

    # Send message to the group
    
    # Wait a certain number of seconds between each game
    
    tasks = [game_handler(update, context, i + 1, True, i * 30) for i in range(len(server.GAMES))]
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
    application.add_handler(CommandHandler('majorcombo', majorcombo, block=False))
    application.add_handler(CommandHandler('tomarketcombo', tomarketcombo, block=False))
    application.add_handler(CommandHandler('rockyrabbitcombo', rockyrabbitcombo, block=False))
    application.add_handler(CommandHandler('rockyrabbiteggs', rockyrabbiteggs, block=False))
    application.add_handler(CommandHandler('rockyrabbitenigma', rockyrabbitenigma, block=False))
    application.add_handler(CommandHandler('blumcode', blumcode, block=False))
    application.add_handler(CommandHandler('cipher', cipher, block=False))
    application.add_handler(CommandHandler('minigg', minigg, block=False))
    application.add_handler(CommandHandler('cube', cube, block=False))
    application.add_handler(CommandHandler('train', train, block=False))
    application.add_handler(CommandHandler('merge', merge, block=False))
    application.add_handler(CommandHandler('twerk', twerk, block=False))
    application.add_handler(CommandHandler('poly', poly, block=False))
    application.add_handler(CommandHandler('trim', trim, block=False))
#    application.add_handler(CommandHandler('cafe', cafe, block=False))
    application.add_handler(CommandHandler('zoo', zoo, block=False))
#    application.add_handler(CommandHandler('gang', gang, block=False))
    application.add_handler(CommandHandler('fluff', fluff, block=False))
    application.add_handler(CommandHandler('tile', tile, block=False))
    application.add_handler(CommandHandler('stone', stone, block=False))
    application.add_handler(CommandHandler('bounce', bounce, block=False))
    application.add_handler(CommandHandler('all', all, block=False))


    application.run_polling()
