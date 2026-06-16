from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "8624726972:AAHa89X4pWrLaD7c-GI3OUjmx7FuSL-5pQQ"

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    try:
        requests.post(url, json={"chat_id": chat_id, "text": text})
    except Exception as e:
        print(f"خطا: {e}")

@app.route('/webhook', methods=['POST'])
def webhook():
    update = request.get_json()
    if update and 'message' in update:
        chat_id = update['message']['chat']['id']
        text = update['message'].get('text', '')
        if text == '/start':
            send_message(chat_id, "سلام! ربات روشن شد.")
        else:
            send_message(chat_id, f"تو گفتی: {text}")
    return "ok", 200

@app.route('/')
def home():
    return "ربات روشن است", 200
    
