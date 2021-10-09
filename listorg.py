import pandas as pd
import re

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

# Подключение таблиц
listorg = pd.read_csv("listorg.csv", delimiter=';', encoding='1251', low_memory=False)
table = pd.read_csv("table.csv", delimiter=';', encoding='1251', low_memory=False)

# Удаление стобца и не Муниципальных школ
month.drop(month.columns[[0, 4]], axis=1, inplace=True)
month = month.loc[month['Тип собственности'] == 'Муниципальная']

# Удаление символов из Месяц
filtr = "[^А-Яа-я0-9.№ ]"
listorg = listorg(filtr,'',regex = True) 

# Удаление символов из Свод
table = table(filtr,'',regex = True) 

#Объединение фреймов по стобцам Наименование, полное соединение
table = pd.merge(listorg, table, left_on='Наименование', right_on='Наименование', how='outer')

# Сохранение фрейма в файл
table.to_csv('itog.csv', encoding='1251')
