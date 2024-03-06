#!/usr/bin/python3

import requests
import os
import sys
from datetime import datetime

API_KEY = os.environ["IMMICH_API_KEY"]               # replace with a valid api key
API_BASE_URL = os.environ["IMMICH_API_BASE_URL"]  # replace as needed

def upload(file):
    stats = os.stat(file)

    headers = {
        'Accept': 'application/json',
        'x-api-key': API_KEY
    }

    data = {
        'deviceAssetId': f'{file}-{stats.st_mtime}',
        'deviceId': 'python',
        'fileCreatedAt': datetime.fromtimestamp(stats.st_mtime),
        'fileModifiedAt': datetime.fromtimestamp(stats.st_mtime),
        'isFavorite': 'false',
    }

    files = {
        'assetData': open(file, 'rb')
    }

    response = requests.post(
        f'{API_BASE_URL}/asset/upload', headers=headers, data=data, files=files)

    print(response.json())
    # {'id': 'ef96f635-61c7-4639-9e60-61a11c4bbfba', 'duplicate': False}


f = open(sys.argv[1], "r")
files = f.readlines() 

for filename in files:
    fullpath = sys.argv[2] + "/" + filename.strip()
    if filename.strip().endswith(".mp4"):
        upload(fullpath)
        os.remove(fullpath)