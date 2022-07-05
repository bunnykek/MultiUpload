import os
from pyrogram.types import Message
from modules.upload import upload

def progress(current, total, progressMessage: Message, fileName: str):
    if int(current * 100 / total) % 10 == 0:
        try:
            progressMessage.edit_text(f"Downloading: `{fileName}`\nProgress: `{current * 100 / total:.1f}%`")
        except:
            pass
        print(f"{current * 100 / total:.1f}%", flush=True)

def tgDownload(msg: Message, serviceID: int, progressMessage: Message):
    print("processing TG", flush=True)
    message = msg.reply_to_message
    #print(message)
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
        message.download(file_path, progress=progress, progress_args=(progressMessage,fileName))
    upload(file_path, serviceID, msg, progressMessage)
    #os.remove(fileName)
    print("done", flush=True)




