import requests
import telegram
from telegram.error import TimedOut
from telegram import Bot
from jinja2 import Template


# set max retries
MAX_RETRIES = 3


class Messenger:
    def __init__(self, token, chat_id):
        self.bot_token = token
        self.chat_id = chat_id
        self.bot = Bot(self.bot_token)

    def send_simple_text(self, bot_message):
        send_text = 'https://api.telegram.org/bot' + self.bot_token + \
            '/sendMessage?chat_id=' + self.chat_id + \
            '&parse_mode=Markdown&text=' + bot_message

        response = requests.get(send_text)

        return response.json()

    def send_html(self, info_json, template_str):
        template_input = open(template_str, 'r').read()
        template = Template(template_input)

        # format the text using a jinja
        text = template.render(info_json, information=info_json)

        for i in range(MAX_RETRIES):
            try:
                self.bot.send_message(chat_id=self.chat_id,
                                      text=text,
                                      parse_mode=telegram.ParseMode.HTML)
                break
            except TimedOut:
                pass
