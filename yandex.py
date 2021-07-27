from decimal import Decimal
import pandas as pd
from yandex_geocoder import Client

import requests
koll_adr = pd.read_csv("rspd table/koll.csv", delimiter=';', encoding='utf-8', low_memory=False)


client = Client("7a54df66-aca5-41ce-958d-2ba447d92eb4")

for i in koll_adr.index:
    coordinates = client.coordinates(koll_adr.iloc[i]['Адрес'])
    koll_adr['Широта'][i] = coordinates[0]
    koll_adr['Долгота'][i] = coordinates[1]
    print()
koll_adr.to_csv('rspd table/koll_itog.csv', encoding='utf-8')
