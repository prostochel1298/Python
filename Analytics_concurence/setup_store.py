from bs4 import BeautifulSoup
import requests
import re
import unicodedata
import pandas as pd
import numpy as np
from google_play_scraper import app
import openpyxl


def store():
    dict_mfo = {"Kviku":"https://www.rustore.ru/catalog/app/ru.kviku.mobile.credits",
        "Деньги Сразу":"https://www.rustore.ru/catalog/app/ru.dc",
        "Быстроденьги - займы онлайн":"https://www.rustore.ru/catalog/app/ru.bistrodengi.app",
        "VIVA Деньги - Займы на карту":"https://www.rustore.ru/catalog/app/ru.viva.mobile",
        "А Деньги - Займы онлайн":"https://www.rustore.ru/catalog/app/ru.adengi",
        "Займер - Робот онлайн займов":"https://www.rustore.ru/catalog/app/robot.zaimer.ru",
        "MoneyMan займы онлайн на карту":"https://www.rustore.ru/catalog/app/ru.moneyman",
        "МигКредит - Займы на карту":"https://www.rustore.ru/catalog/app/ru.migcredit.migcredit2"}  # URL приложения
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    name_mfo = dict_mfo.keys()
    url_rustore = dict_mfo.values()
    score_downloads = []
    mfo = []
    for i in url_rustore:
        response = requests.get(i, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            # Поиск числа скачиваний 
            downloads_tag = soup.find("li", {"class": "k1Cqy_n5 S4Tah8me"})
            downloads = downloads_tag.text if downloads_tag else "Н/Д"
            pattern = r'[A-я]{10}:|[+]'
            repl = ''
            result = unicodedata.normalize('NFKC',downloads)
            score_downloads.append(re.sub(pattern,repl,result,count=0))
        else:
            print("Ошибка при запросе страницы:", response.status_code)
    for b in name_mfo:
        mfo.append(b)

    Ru_store = pd.DataFrame({"Название приложения в Ru Store":mfo,
                    "Загрузок":score_downloads})
    appid = ['ru.limezaim.www',
            'ru.dc','com.oneclickmoney.ocm','ru.cashtoyou.app','ru.kviku.mobile.credits',
            'ru.bistrodengi.my','ru.viva.mobile','ru.adengi','robot.zaimer.ru',
            'ru.moneyman','ru.payps.payps','ru.migcredit.migcredit2']
    # Получение информации о приложении
    name = []
    install = []
    errors = []

    for i in appid:
        try:
            result = app(i)
            name.append(result['title'])
            install.append(result['realInstalls'])
        except:
            errors.append(i)
            
    name_mfo_PM={'Название приложения в Google play':name,
            'Количестов установок':install,
            'Не найдено':errors}


    GP = pd.DataFrame({'Название приложения в Google Play':name,
            'Количестов установок':install})

    new_table = pd.concat([Ru_store, GP], axis=1)
    return new_table

