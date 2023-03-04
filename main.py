from flask import Flask, request
import telegram

app = Flask(__name__)

TOKEN = 'token'
CHAT_ID = 'id'

bot = telegram.Bot(token=TOKEN)

@app.route('/send', methods=['POST'])
def submit_form():

    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    text = f'{name} ({email}): {message}'

    bot.send_message(chat_id=CHAT_ID, text=text)

    return 'Done'

if __name__ == '__main__':
    app.run()