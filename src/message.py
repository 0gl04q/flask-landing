import telebot

from pydantic import BaseModel
from src.config import settings


class UserMessage(BaseModel):
    name: str
    email: str
    subject: str
    message: str


def create_message(msg: UserMessage) -> str:
    message = (
        f"<b>Имя:</b> {msg.name}\n"
        f"<b>Email:</b> {msg.email}\n"
        f"<b>Тема:</b> {msg.subject}\n"
        f"<b>Сообщение:</b> {msg.message}"
    )
    return message


def send_message(msg: UserMessage):
    message = create_message(msg)
    bot = telebot.TeleBot(settings.TG_BOT_TOKEN, parse_mode="HTML")
    bot.send_message(settings.TG_CHAT_ID, message)
