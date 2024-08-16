import asyncio
import os
import sys
import httpx
import random
import time
import uuid
import datetime
from loguru import logger


# Disable logging for httpx
httpx_log = logger.bind(name="httpx").level("WARNING")
logger.remove()
logger.add(sink=sys.stdout,
           format="<white>{time:YYYY-MM-DD HH:mm:ss}</white>"
           " | <level>{level: <8}</level>"
           " | <cyan><b>{line}</b></cyan>"
           " - <white><b>{message}</b></white>")
logger = logger.opt(colors=True)

GAMES = {
    1: {
        'name': 'Riding Extreme 3D',
        'appToken': 'd28721be-fd2d-4b45-869e-9f253b554e50',
        'promoId': '43e35910-c168-4634-ad4f-52fd764a843f',
    },
    2: {
        'name': 'My Clone Army',
        'appToken': '74ee0b5b-775e-4bee-974f-63e7f4d5bacb',
        'promoId': 'da115c0b-9c09-462a-951a-4e84f6ac5358',
    },
    3: {
        'name': 'Cube Master 3D',
        'appToken': '88191761-51a1-4c34-82bb-c946fe485772',
        'promoId': 'b6cb19e3-319a-4b9f-bf4f-091f2a90c75d',
    },
    4: {
        'name': 'Train Racing Games',
        'appToken': 'a15208fd-2c26-4b47-a46b-b093a567e92b',
        'promoId': '8e7cb7d7-050b-42b5-a4f2-fba83f926cf4',
    },
    5: {
        'name': 'Merge Master',
        'appToken': 'a5e54d2a-0748-49d6-ae0f-41a1f571682e',
        'promoId': 'd86d7f18-15f0-44ea-a545-1627a87c40e6',
    }
}

async def play_the_game(appToken, promoId, no_of_keys):
    url = "https://api.gamepromo.io"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {appToken}'
    }
    keys = []
    async with httpx.AsyncClient() as client:
        for _ in range(no_of_keys):
            key = str(uuid.uuid4()).replace('-', '')[:10]
            response = await client.post(url, json={
                'promoId': promoId,
                'key': key
            }, headers=headers)
            if response.status_code == 200:
                keys.append(key)
            else:
                logger.error(f"Failed to generate key: {response.text}")
    return keys

async def run(chosen_game, no_of_keys):
    game = GAMES.get(chosen_game)
    if not game:
        raise ValueError("Invalid game selected")
    return await play_the_game(game['appToken'], game['promoId'], no_of_keys)

if __name__ == '__main__':
    keep_alive()
    logger.info("Server is running...")
