from aiogram import Router, F
from aiogram.types import Message

import pandas as pd

rt = Router()

def form(val):
    s = str(val)
    if len(s) <= 3:
        return f"{s},00"
    elif len(s) <= 6:
        return f"{s[-6:-3]}'{s[-3:]},00"
    elif len(s) <= 9:
        return f"{s[:-6]}'{s[-6:-3]}'{s[-3:]},00"

def result(name_inst, lst_col, dataframe, indx):
    res = ''
    for inst in dataframe['Unnamed: 0']:
        if inst == name_inst:
            for col in dataframe.columns:
                if col in lst_col:
                    res += f'{col}: {dataframe[col][indx]}\n'
            res += f'Итог: {dataframe[dataframe.columns[-2]][indx]}'
            return res

@rt.message(F.document)
async def report(message: Message):
    await message.bot.download(message.document, destination='Итоговый по оплатам на кассах.xlsx')
    df = pd.read_excel('Итоговый по оплатам на кассах.xlsx', skiprows=5)
    heads_h = ['Наличные', 'Безналичные', 'Онлайн оплата']
    heads_s = ['Наличные', 'Безналичные', 'Сайт', 'Vendotek', 'Вендинг']
    h_index = [i for i in df.index if df['Unnamed: 0'][i] == 'HIMKI всего'][0]
    s_index = [i for i in df.index if df['Unnamed: 0'][i] == 'SKAZKA всего'][0]
    await message.answer(f'<дата>\n'
                         f'Гостей <кол-во> ч\n'
                         f'{result('SKAZKA всего', heads_s, df, s_index)}\n'
                         f'\nХимки\n'
                         f'{result('HIMKI всего', heads_h, df, h_index)}')