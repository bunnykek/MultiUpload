import os
import requests
import requests
from modules.upload import upload
import subprocess
import re


URLRx = re.compile(r"(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])")

def ddlDownload(message, serviceID, progressMessage):
    print("ddlDownload", flush=True)
    ddl = URLRx.search(message.text).group(0)
    filename = os.path.basename(ddl).split("?")[0]
    print(f"Downloading {filename}", flush=True)
    filePath = os.path.join("Downloads", filename)
    if not os.path.exists(filePath):
        subprocess.run(["curl", "-L", ddl, "-o", filePath])
    upload(filePath, serviceID, message, progressMessage)
