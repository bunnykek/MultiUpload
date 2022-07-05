
import os
import shutil
import subprocess


def CacheSize(msg):
    print("Getting cache size", flush=True)
    output = subprocess.check_output(['du','-sh', 'Downloads']).split()[0].decode('utf-8')
    msg.reply_text("Cache size: " + output)

def clearCache(msg):
    print("Clearing cache", flush=True)
    #delete all files in Downloads folder using linux command
    shutil.rmtree('Downloads')
    os.makedirs('Downloads')
    #subprocess.call(['rm','-rf','Downloads/*'])
    msg.reply_text("Cache cleared")
    CacheSize(msg)
