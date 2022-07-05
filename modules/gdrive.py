import json
import re
from pyrogram.types import Message
from modules.upload import upload
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

import os

SCOPES = ['https://www.googleapis.com/auth/drive']
gdriveIDRe = re.compile('([-\w]{25,})')

try:
    creds = Credentials.from_authorized_user_info(json.loads(os.getenv('token_json')), SCOPES)
    service = build('drive', 'v3', credentials=creds)
except:
    print("token_json ENV error!", flush=True)
    raise Exception("token_json ENV error!")


def gdriveDownload(message: Message, serviceID: int, progressMessage: Message):
    fileid = gdriveIDRe.search(message.text).group(1)

    request = service.files().get_media(fileId=fileid)

    metadata = service.files().get(fileId=fileid, fields='name, size, mimeType',
                                    supportsAllDrives=True).execute()
    print(metadata, flush=True)
    #check if file exists in python
    download_path = os.path.join('Downloads', metadata['name'])
    if not os.path.exists(download_path):
        fh = open(download_path, "wb")
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            progressMessage.edit_text(f"**{metadata['name']}**\n`Downloading... {int(status.progress() * 100)}%`")
            print(f"Download %d%%." % int(status.progress() * 100))
        progressMessage.edit_text(f"Downloaded **{metadata['name']}**")
        fh.close()
        print("Downloaded", flush=True)
    upload(download_path, serviceID, message, progressMessage)
    #os.remove(metadata['name'])
        

    