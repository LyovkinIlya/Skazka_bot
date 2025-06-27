from aiogram import Router, F
from aiogram.types import Message, FSInputFile

import qrcode
import cv2

detector = cv2.QRCodeDetector()

# импорт клавиатуры

qr = Router()

@qr.message(F.text)
async def create(message: Message):
    img = qrcode.make(message.text)
    img.save('create_code.jpg')
    img_code = FSInputFile('create_code.jpg')
    await message.answer_photo(photo=img_code)

@qr.message(F.photo)
async def read(message: Message):
    await message.bot.download(message.photo[-1], destination='read_code.jpg')
    img = cv2.imread('read_code.jpg')
    data, bbox, straight_qrcode = detector.detectAndDecode(img)
    await message.answer(data)