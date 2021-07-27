import pandas as pd
import re
import time


t0 = time.time()

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

# Подключение таблиц
no_inn = pd.read_csv("rspd table/no_inn.csv", delimiter=';', encoding='utf-8', low_memory=False)
inn = pd.read_csv("rspd table/zakupki.csv", delimiter=';', encoding='utf-8', low_memory=False)

filtr = "[^А-Яа-я0-9]|(МКО)|(МБО)|(МО)"
k = 0
for i in no_inn.index:
    no_inn_name = no_inn.iloc[i]['Наименование']
    no_inn_name = re.sub(filtr, "", str(no_inn_name))
    for j in inn.index:
        inn_name = inn.iloc[j]['Наименование']
        inn_name = re.sub(filtr, "", str(inn_name))
        if (no_inn_name.lower() in inn_name.lower()) or (inn_name.lower() in no_inn_name.lower()):
            k = k + 1
            print(k)
            no_inn['ИНН'][i] = inn['ИНН'][j]

no_inn.to_csv('rspd table/itog_inn.csv', encoding='utf-8')
t1 = time.time() - t0
print(t1)