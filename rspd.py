import pandas as pd
import re
import time
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


t0 = time.time()

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

# Подключение таблиц
szo_df = pd.read_csv("rspd table/mkou_szo.csv", delimiter=';', encoding='utf-8', low_memory=False)
rspd_df = pd.read_csv("rspd table/rspd_mkou.csv", delimiter=';', encoding='utf-8', low_memory=False)

# Удаление стобца и не Муниципальных школ
# month.drop(month.columns[[0, 4]], axis=1, inplace=True)
# month = month.loc[month['Тип собственности'] == 'Муниципальная']

# nameorg = listorg['Наименование'].copy()
# print(nameorg.head)
# Удаление символов из Месяц
'''
for i in listorg.index:
    buf = listorg['Наименование'][i]
    buf = re.sub("[^А-Яа-я0-9.№]|(РД)", "", str(buf))  # почему то она удаляет до слова если стоят после "_" как решить?
    listorg['Наименование'][i] = buf
listorg.to_csv('lorg2.csv', encoding='utf-8')
# Удаление символов из Свод
for i in table.index:
    buf = table['Наименование'][i]
    buf = re.sub("[^А-Яа-я0-9.№IVX]|(РД)", "", str(buf))
    table['Наименование'][i] = buf
table.to_csv('t2.csv', encoding='utf-8')
'''

filtr = "[^А-Яа-я0-9]|(МКО)|(МБО)|(МО)"
k=0
for i in rspd_df.index:
    rspd_name = rspd_df.iloc[i]['Полное наименование учреждения']
    rspd_name = re.sub(filtr, "", str(rspd_name))
    for j in szo_df.index:
        szo_name = szo_df.iloc[j]['Полное наименование учреждения']
        szo_name = re.sub(filtr, "", str(szo_name))
        if (rspd_name.lower() in szo_name.lower()) or (szo_name.lower() in rspd_name.lower()):
            k = k+1
            print(k)

            rspd_df['Полное наименование учреждения 2'][i] = szo_df['Полное наименование учреждения'][j]
            rspd_df['Муниципальное образование'][i] = szo_df['Муниципальное образование'][j]
            rspd_df[' Тип населённого пункта'][i] = szo_df[' Тип населённого пункта'][j]
            rspd_df['Наименование населенного пункта'][i] = szo_df['Наименование населенного пункта'][j]
            rspd_df[' Адрес учреждения'][i] = szo_df[' Адрес учреждения'][j]
            rspd_df['Широта'][i] = szo_df['Широта'][j]
            rspd_df['Долгота'][i] = szo_df['Долгота'][j]
            rspd_df['Тип подключения (сущ.)'][i] = szo_df['Тип подключения (сущ.)'][j]
            rspd_df['Провайдер (сущ.)'][i] = szo_df['Провайдер (сущ.)'][j]
            rspd_df['Тип подключения (план)'][i] = szo_df['Тип подключения (план)'][j]
            rspd_df['Скорость подключения (план), Мбит/с'][i] = szo_df['Скорость подключения (план), Мбит/с'][j]
            rspd_df['Скорость подключения (сущ.), Мбит/с'][i] = szo_df['Скорость подключения (сущ.), Мбит/с'][j]
            rspd_df['Дата планируемого подключения'][i] = szo_df['Дата планируемого подключения'][j]




'''
            szo_df['Свод'][j] = rspd_df['Наименование учреждения'][i]
            key = True
        if key == False:
            szo_df['Не вошедшее'][i] = rspd_df['Наименование учреждения'][i]

    continue
'''
# (table[table['Наименование'][i]].str.containt(listorg[listorg['Наименование'][j]].str, case = False)) or (listorg[listorg['Наименование'][j]].str.containt(table[table['Наименование'][i]].str, case = False)):

# table = pd.merge(listorg, table, left_on='Наименование', right_on='Наименование', how='outer')

# Сохранение фрейма в файл
rspd_df.to_csv('rspd table/itog.csv', encoding='utf-8')
t1 = time.time() - t0
print(t1)