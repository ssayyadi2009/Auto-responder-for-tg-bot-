from flask import Flask, request
import requests
import os

app = Flask(__name__)
BOT_TOKEN = os.getenv("BOT_TOKEN")

WELCOME_MESSAGE = "سلام\nخوبی؟\nچخبر؟\nچیکارا می‌کنی؟"

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    if not data:
        return "no data", 400

    message = data.get("message")
    if message and "chat" in message:
        chat_id = message["chat"]["id"]
        send_message(chat_id, WELCOME_MESSAGE)
    return "ok", 200

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error sending message: {e}")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)