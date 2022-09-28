import os
import re
from pyrogram import Client
from pyrogram.types import Message
from modules.upload import upload

tgUrlRx = re.compile("https://t\.me/c/(\d+)/(\d+)")

# def progress(current, total, progressMessage: Message, fileName: str):
#     if int(current * 100 / total) % 10 == 0:
#         try:
#             progressMessage.edit_text(f"Downloading: `{fileName}`\nProgress: `{current * 100 / total:.1f}%`")
#         except:
#             pass
#         print(f"{current * 100 / total:.1f}%", flush=True)

def tgDownload(client:Client, msg: Message, serviceID: int, progressMessage: Message):
    print("processing TG", flush=True)
    result = tgUrlRx.search(msg.text)
    if result:
        chatid = '-100'+result.group(1)
        mid = result.group(2)
        print("chatid", chatid)
        message = client.get_messages(chatid, int(mid))
    else:
        message = msg.reply_to_message
    print("Got the message object!")
    mediaType = message.media.value
    if mediaType == 'video':
        media = message.video
        mime = message.video.mime_type
    elif mediaType == 'audio':
        media = message.audio
        mime = message.audio.mime_type
    elif mediaType == 'document':
        media = message.document
        mime = message.document.mime_type
        print(mime)
    else:
        print("This media type is not supported", flush=True)
        raise Exception("This media type is not supported")
    
    fileName = media.file_name
    size = media.file_size
    print(fileName, size, flush=True)
    
    file_path = os.path.join(os.getcwd(), 'Downloads', fileName)
    if not os.path.exists(file_path):
        progressMessage.edit(f"Downloading: `{fileName}`")
        message.download(file_path) #, progress=progress, progress_args=(progressMessage,fileName))
    upload(file_path, serviceID, msg, progressMessage)
    #os.remove(fileName)
    print("done", flush=True)




