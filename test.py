import urllib.request

url = "https://b512-34-124-144-102.ngrok-free.app/generate"

import json

import urllib.request
import urllib.error
import os

# FastAPIのURLを取得
fastapi_url = url
# FastAPIのエンドポイントにPOSTリクエストを送信
message = "あなたの名前は何ですか？"
request_payload = {
            "prompt": message,
            "max_new_tokens": 512,
            "do_sample": True,
            "temperature": 0.7,
            "top_p": 0.9
        }
req = urllib.request.Request(fastapi_url, data=json.dumps(request_payload).encode('utf-8'), headers={'Content-Type': 'application/json'}, method='POST')

# レスポンスを取得
try:
    with urllib.request.urlopen(req) as response:
        if response.getcode() != 200:
            raise Exception(f"FastAPI request failed with status code: {response.getcode()}")
        response_body = json.loads(response.read())
        print("FastAPI response:", json.dumps(response_body, default=str))
except urllib.error.HTTPError as e:
    print(f"HTTPError: {e.code} - {e.reason}")
#                 "Access-Control-Allow-Origin": "*",
#                 "Access-Control-Allow-Headers": "Content-Type",
