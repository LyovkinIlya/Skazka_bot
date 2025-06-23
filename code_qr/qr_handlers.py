from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

import qrcode
import cv2

from run import bot

detector = cv2.QRCodeDetector()

# импорт клавиатуры

qr = Router()

# class QRCode(StatesGroup):
#     code = State()
#
# @qr.message(Command('code_qr'))
# async def code_qr(message: Message, state: FSMContext):
#     await state.set_state(QRCode.code)
#     await message.answer('Пришлите строку 32 символов, чтобы сгенерировать QRCode\n'
#                         'Или изображение, чтобы его раскодировать')

@qr.message(F.text)
async def create(message: Message):
    img = await qrcode.make(message.text)
    img.save('code.jpg')
    img_code = FSInputFile('code.jpg')
    await message.answer_photo(photo=img_code)

@qr.message(F.photo)
async def read(message: Message):
    photo = message.photo[-1]
    photo_file = await bot.get_file(photo.file_id)



    data, bbox, straight_qrcode = detector.detectAndDecode(cv2.imread('code.jpg'))
    await message.answer(data)
