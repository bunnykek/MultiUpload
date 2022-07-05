import asyncio
from pyrogram import Client


#get your api_id and api_hash from https://my.telegram.org/apps
api_id = 12345  # your api_id
api_hash = "0123456789abcdef0123456789abcdef" # your api_hash


async def main():
    async with Client("my_account", api_id, api_hash) as app:
        await app.send_message("me", "Greetings from **Pyrogram**!")


asyncio.run(main())