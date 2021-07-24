import pandas as pd
import re

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

# Подключение таблиц
svod = pd.read_csv("Свод.csv", delimiter=';', encoding='1251', low_memory=False)
month = pd.read_csv("январь.csv", delimiter=';', encoding='1251', low_memory=False)

# Удаление стобца и не Муниципальных школ
month.drop(month.columns[[0, 4]], axis=1, inplace=True)
month = month.loc[month['Тип собственности'] == 'Муниципальная']

# Удаление символов из Месяц
for i in month.index:
    buf = (month['Наименование ДОО'][i])
    buf = re.sub("[^А-Яа-я0-9.№ ]", "", str(buf))  # почему то она удаляет до слова если стоят после "_" как решить?
    month['Наименование ДОО'][i] = buf

# Удаление символов из Свод
for i in svod.index:
    buf = svod['Наименование ДОО'][i]
    buf = re.sub("[^А-Яа-я0-9.№ ]", "", str(buf))
    svod['Наименование ДОО'][i] = buf

# Объединение таблицы своl и месяц по столбцам Наименование ДОО с правым пересечением
df3 = pd.merge(svod, month, left_on='Наименование ДОО', right_on='Наименование ДОО', how='right')

# Сохранение фрейма в файл
df3.to_csv('тест1.csv', encoding='1251')

