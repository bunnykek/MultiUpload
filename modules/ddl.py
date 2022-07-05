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

    try:
        filename = requests.get(ddl).headers.get("Content-Disposition").split("filename=")[1].replace('"', '')
        print(filename, flush=True)
    except:
        filename = ddl.split('/')[-1]
    if not os.path.exists(os.path.join('Downloads', filename)):
        subprocess.run(["curl", "-L", ddl, "-o", "Downloads/{}".format(filename)])
    upload("Downloads/{}".format(filename), serviceID, message, progressMessage)
