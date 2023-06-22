# MultiUpload
Upload your files to 10+ free hosting services.
#### Supported hosts:
```
+----+-------------+--------+
| #  |     Host    |  Limit |
+====+=============+========+
| 1  | anonfiles   | 20 GB  |
+----+-------------+--------+
| 2  | Catbox      | 200 MB |
+----+-------------+--------+
| 3  | file.io     | 2 GB   |
+----+-------------+--------+
| 4  | Filemail    | 5 GB   |
+----+-------------+--------+
| 5  | Gofile      | unlim  |
+----+-------------+--------+
| 6  | KrakenFiles | 1 GB   |
+----+-------------+--------+
| 7  | LetsUpload  | 10 GB  |
+----+-------------+--------+
| 8  | MegaUp      | 5 GB   |
+----+-------------+--------+
| 9  | MixDrop     | unlim  |
+----+-------------+--------+
| 10 | pixeldrain  | 10 GB  |
+----+-------------+--------+
| 11 | Racaty      | 10 GB  |
+----+-------------+--------+
| 12 | transfer.sh | unlim  |
+----+-------------+--------+
| 13 | Uguu        | 128 MB |
+----+-------------+--------+
| 14 | WeTransfer  | 2 GB   |
+----+-------------+--------+
| 15 | workupload  | 2 GB   |
+----+-------------+--------+
| 16 | zippyshare  | 500 MB |
+----+-------------+--------+
```
#### Setup procedure:

- Follow [this guide](https://www.iperiusbackup.net/en/how-to-enable-google-drive-api-and-get-client-credentials/), but at the last step instead of selecting application as `web application` use `desktop app`   

<img src="https://user-images.githubusercontent.com/67633271/177330592-c686e8f6-2e16-4461-9e50-f84effd66969.png" width="500"/>    

- Download the json and save it as `credentials.json`.    
- `git clone https://github.com/bunnykek/MultiUpload`     
- Navigate into the `TokenGeneration` directory and follow the [readme.txt](https://github.com/bunnykek/MultiUpload/blob/main/TokenGeneration/readme.txt) for further procedure.
- Deploy to heroku 
#### Heroku Deploy
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/bunnykek/MultiUpload)
#### VPS Deploy
- `pip install -r requirements.txt`
- Create a `.env` file with the following variables,
```
authorized_list = "[111111111]"
bot_token = "12344556:AAAAAAABBBBBBBBBCCCCCCC"
api_id = "123455"
api_hash = "aaaabbbbbaaaaaddddddd"
default_host_id = "12"
token_json = '{"token": "XXXXXXXXXXXXXXXXXX", "refresh_token": "YYYYYYYYYYYYYYYYYY", "token_uri": "ZZZZZZZZZZZZZZZZZZ", "client_id": "XXXXXXXXXXXXXXXxx", "client_secret": "ZZZZZZZZZZZZZZZZZ", "scopes": ["https://www.googleapis.com/auth/drive.readonly"], "expiry": "2023-06-22T21:35:06.155593Z"}'
```
- `py bot.py`
#### Bot commands:
- `/help` - Helps
- `/stats` - Shows the total downloaded cache size.
- `/clear` - Wipes the whole cache.
#### Credits
- [go-upload](https://github.com/Sorrow446/go-upload) by @Sorrow446
##### Make sure to star my projects if you enjoy. Thanks
