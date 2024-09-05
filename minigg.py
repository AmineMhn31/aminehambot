import httpx
from io import BytesIO
from telegram import Update, InputFile
from telegram.ext import ContextTypes

# ========================hamsterCOMBO==========================================

async def fetch_image(url: str) -> BytesIO:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        image_data = BytesIO(response.content)
        return image_data

async def hamstercombo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="https://cointicker.com/wp-content/uploads/2024/09/image-72-1024x466.png")
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
    image_url = "https://imagedelivery.net/4-5JC1r3VHAXpnrwWHBHRQ/cf16bfed-31e6-4a0b-f6c0-ac2909129f00/public"
    await context.bot.send_photo(chat_id=chat_id, photo=image_url)

    # Then send the TomarketDaily Secret message
    secret_message = (
        "🍅 *TomarketDaily Secret* \n\n"
        "1️⃣ x1 Tap hamster 🐹\n"
        "2️⃣ x3 Tap Tomato Head 🍅\n"
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

# ========================rocky rabbit COMBO==========================================

async def fetch_image(url: str) -> BytesIO:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        image_data = BytesIO(response.content)
        return image_data

async def rockyrabbitcombo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="https://cointicker.com/wp-content/uploads/2024/09/image-50-1024x615.png")
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


#==============================rocky rabbit enigma========================

async def fetch_image(url: str) -> BytesIO:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        image_data = BytesIO(response.content)
        return image_data

async def rockyrabbitenigma(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="https://cointicker.com/wp-content/uploads/2024/09/image-59-1024x1006.png")
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

# ===============================MINIGG===================================

async def fetch_video(url: str) -> BytesIO:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        video_data = BytesIO(response.content)
        return video_data

async def minigg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="https://hamster-combo.com/wp-content/uploads/2024/09/video_2024-09-03_23-19-58-online-video-cutter.com_.mp4")
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
            "🔢Today's Cipher Code \\(OFFCHAIN\\) 04/09/2024📅:\n"
            "*O:  ➖➖➖*\n"
            "*F:  🔘🔘➖🔘*\n"
            "*F:  🔘🔘➖🔘*\n"
            "*C:  ➖🔘➖🔘*\n"
            "*H:  🔘🔘🔘🔘*\n"
            "*A:  🔘➖*\n"
            "*I:  🔘🔘*\n"
            "*N:  ➖🔘*\n"
            "✅CLAIM 1000000💰\."
        ),
        parse_mode='MARKDOWNV2'
    )
