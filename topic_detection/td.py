import requests
import json

# URL = "https://api.sandbox.deepgram.com/nlu?model=general-polaris&summarize=true&topics=true&semantic_tags=true"
URL = "https://api.beta.deepgram.com/v1/listen?detect_topics=true&punctuate=true&tier=enhanced"

HEADERS = {
    "Content-Type": "audio/wav",
    "Authorization": "Token 769c62d0ef6545ef59892c73cad3aaf026e82bb7"
}

with open("audio/The Rise Of Solar Power.wav", "rb") as f:
    data = f.read()

res = requests.post(url=URL, headers=HEADERS, data=data)
with open ("topic_detection/dg_detected.json", "w") as f:
    json.dump(json.loads(res.text), f)