from flask import Flask, escape, request

from app.bot import bot_blueprint

app = Flask(__name__)
app.register_blueprint(bot_blueprint, url_prefix='/bot')


@app.route('/health')
def health():
    return 'Hello, this service is running!'
