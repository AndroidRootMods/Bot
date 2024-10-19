import requests

TOKEN = '2142016826:AAEUw-uI7Uf3lj2DkK2nPjfUICq93dVsnLM'
URL = f'https://api.telegram.org/bot{TOKEN}/'

def send_message(chat_id, text):
    requests.post(URL + 'sendMessage', data={'chat_id': chat_id, 'text': text})

# استبدل CHAT_ID بمعرف الدردشة الخاص بك
send_message('@ElsayedKhaterBot', 'Hello from my bot!')
