from aiogram import Router, F
from aiogram.types import Message, FSInputFile

import pandas as pd

rt = Router()

# df = pd.read_excel('Итоговый по оплатам на кассах.xlsx', skiprows=5)
# heads_h = ['Наличные', 'Безналичные', 'Онлайн оплата']
# heads_s = ['Наличные', 'Безналичные', 'Сайт', 'Vendotek', 'Вендинг']
# h_index = [i for i in df.index if df['Unnamed: 0'][i] == 'HIMKI всего']
# s_index = [i for i in df.index if df['Unnamed: 0'][i] == 'SKAZKA всего']

def result(name_inst, lst_col, dataframe, indx):
    for inst in dataframe['Unnamed: 0']:
        if inst == name_inst:
            for col in dataframe.columns:
                if col in lst_col:
                    return f'{col}: {dataframe[col][indx]}'           # Здесь неправильно работает
            return f'Итог: {dataframe[dataframe.columns[-2]][indx]}'  # программа, с return

@rt.message(F.document)
async def report(message: Message):
    await message.bot.download(message.document, destination='Итоговый по оплатам на кассах.xlsx')
    df = pd.read_excel('Итоговый по оплатам на кассах.xlsx', skiprows=5)
    heads_h = ['Наличные', 'Безналичные', 'Онлайн оплата']
    heads_s = ['Наличные', 'Безналичные', 'Сайт', 'Vendotek', 'Вендинг']
    h_index = [i for i in df.index if df['Unnamed: 0'][i] == 'HIMKI всего']
    s_index = [i for i in df.index if df['Unnamed: 0'][i] == 'SKAZKA всего']
    # await message.answer(f'<дата>\n'
    #                      f'Гостей <кол-во> ч\n'
    #                      f'{result('SKAZKA всего', heads_s, df, s_index[0])}\n'
    #                      f'\nHimki\n'
    #                      f'{result('HIMKI всего', heads_h, df, h_index[0])}')
    s = result('SKAZKA всего', heads_s, df, s_index[0])
    h = result('HIMKI всего', heads_h, df, h_index[0])
    print(s)