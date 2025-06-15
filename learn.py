from aiogram import types
from loader import dp

@dp.message_handler(commands=["learn"])
async def learn_info(msg: types.Message):
    await msg.answer("📘 This bot lets you convert text to voice using Novita AI.\nTry using /voice followed by your message!")
