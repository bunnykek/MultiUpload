FROM ubuntu:20.04
COPY . .
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get -y install python3-pip curl
RUN pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib pycryptodomex pillow pyrogram tgcrypto pycryptodomex python-dotenv
RUN chmod +x start.sh
