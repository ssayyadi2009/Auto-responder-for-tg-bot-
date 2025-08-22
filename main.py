from flask import Flask, request
import requests
import os

app = Flask(__name__)
BOT_TOKEN = os.getenv("BOT_TOKEN")

WELCOME_MESSAGE = "سلام\nخوبی؟\nچخبر؟\nچیکارا می‌کنی؟"

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    chat_id = data["message"]["chat"]["id"]
    send_message(chat_id, WELCOME_MESSAGE)
    return "ok"

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)

if __name__ == "__main__":
    app.run()