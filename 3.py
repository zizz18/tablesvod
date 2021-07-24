import pandas as pd
import re

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

# Подключение таблиц
listorg = pd.read_csv("listorg.csv", delimiter=';', encoding='1251', low_memory=False)
table = pd.read_csv("table.csv", delimiter=';', encoding='1251', low_memory=False)

# Удаление стобца и не Муниципальных школ
# month.drop(month.columns[[0, 4]], axis=1, inplace=True)
# month = month.loc[month['Тип собственности'] == 'Муниципальная']

# Удаление символов из Месяц
for i in listorg.index:
    buf = listorg['Наименование'][i]
    buf = re.sub("[^А-Яа-я0-9.№ ]", "", str(buf))  # почему то она удаляет до слова если стоят после "_" как решить?
    listorg['Наименование'][i] = buf

# Удаление символов из Свод
for i in table.index:
    buf = table['Наименование'][i]
    buf = re.sub("[^А-Яа-я0-9.№ ]", "", str(buf))
    table['Наименование'][i] = buf


for i in table.index:
    #print(table['Наименование'][i],'|', listorg['Наименование'][j])
    for j in table.index:
        if (table['Наименование'][i] in listorg['Наименование'][j]) or (listorg['Наименование'][j] in table['Наименование'][i]):
            table['Адрес'][i] = listorg['Юридический адрес'][j]
            table['ИНН'][i] = listorg['ИНН'][j]
            table['Контакты'][i] = listorg['Телефон'][j]
            continue

#table = pd.merge(listorg, table, left_on='Наименование', right_on='Наименование', how='outer')

# Сохранение фрейма в файл
table.to_csv('itog.csv', encoding='utf-8')
