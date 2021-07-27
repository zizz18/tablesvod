import pandas as pd
import re

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

# Подключение таблиц
listorg = pd.read_csv("listorg.csv", delimiter=';', encoding='utf-8', low_memory=False)
table = pd.read_csv("table.csv", delimiter=';', encoding='utf-8', low_memory=False)

# Удаление стобца и не Муниципальных школ
# month.drop(month.columns[[0, 4]], axis=1, inplace=True)
# month = month.loc[month['Тип собственности'] == 'Муниципальная']
nameorg = listorg['Наименование'].copy()
print(nameorg.head)
# Удаление символов из Месяц
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

for i in table.index:
    t1 = table.iloc[i]['Наименование']
    for j in table.index:
        l2 = listorg.iloc[j]['Наименование']
        if (t1.lower() in l2.lower()) or (l2.lower() in t1.lower()):
            table['Наименование'][i] = nameorg[j]
            table['Адрес'][i] = listorg['Юридический адрес'][j]
            table['ИНН'][i] = listorg['ИНН'][j]
            table['Контакты'][i] = listorg['Телефон'][j]
            continue

#(table[table['Наименование'][i]].str.containt(listorg[listorg['Наименование'][j]].str, case = False)) or (listorg[listorg['Наименование'][j]].str.containt(table[table['Наименование'][i]].str, case = False)):

#table = pd.merge(listorg, table, left_on='Наименование', right_on='Наименование', how='outer')

# Сохранение фрейма в файл
table.to_csv('itog.csv', encoding='utf-8')
print(nameorg.head)