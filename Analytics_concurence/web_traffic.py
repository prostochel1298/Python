import pandas as pd
import numpy as np
from selenium import webdriver
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import re
import pyautogui

def web_traffic():
    driver = uc.Chrome()
    def wait_for_load():
        time.sleep(7)

    urls_site = {'Е-капуста':'https://spymetrics.ru/ru/website/ekapusta.com',
        'Деньги Сразу':'https://spymetrics.ru/ru/website/dengisrazy.ru',
        'cashtoyou':'https://spymetrics.ru/ru/website/cashtoyou.ru',
        'oneclickmoney':'https://spymetrics.ru/ru/website/oneclickmoney.ru',
        'kviku':'https://spymetrics.ru/ru/website/kviku.ru',
        'Лайм-займ':'https://spymetrics.ru/ru/website/www.lime-zaim.ru',
        'beeon':'https://spymetrics.ru/ru/website/beeon.ru',
        'Веб-займ':'https://spymetrics.ru/ru/website/web-zaim.ru',
        'Быстроденьги':'https://spymetrics.ru/ru/website/bistrodengi.ru',
        'Турбозайм':'https://spymetrics.ru/ru/website/turbozaim.ru',
        'Кнопка-деньги':'https://spymetrics.ru/ru/website/knopkadengi.ru',
        'Виваденьги':'https://spymetrics.ru/ru/website/www.vivadengi.ru',
        'А-деньги':'https://spymetrics.ru/ru/website/www.adengi.ru',
        'Займер':'https://spymetrics.ru/ru/website/www.zaymer.ru',
        'Мани мен':'https://spymetrics.ru/ru/website/moneyman.ru',
        'Плати за':'https://spymetrics.ru/ru/website/platiza.ru',
        'Миг-кредит':'https://spymetrics.ru/ru/website/migcredit.ru'}


    name_mfo = urls_site.keys()
    url_mfo = urls_site.values()

    mapping = {"Finbridge":['Е-капуста','Деньги Сразу','cashtoyou','oneclickmoney'],
               "ЭйрЛоанс":['kviku'],
               "Лайм-Займ":['Лайм-займ'], 
               "Академическая":['beeon','Веб-займ'],
               "Eqvanta":['Быстроденьги','Турбозайм','Кнопка-деньги'],
               "VivaДеньги":['Виваденьги'],
               "А-Деньги":['А-деньги'],
           "Займер":['Займер'],
           "MoneyMan":['Мани мен','Плати за'],
           "МигКредит":['Миг-кредит']}
    mfo = {key: 0 for key in mapping.keys()}
    

    for name, url in urls_site.items():
        driver.get(url)
        pyautogui.moveTo(550, 380)
        wait_for_load()
        pyautogui.click()
        wait_for_load()
    
        try:
            traffic_element = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[5]/div/div/div[1]/p[3]')
            pattern = r'\b\d{1,3}(?:\s\d{3})+\b'
            traffic = [int(num.replace(" ", "")) for num in re.findall(pattern, traffic_element.text)]
        
        # Суммируем трафик для каждого сайта по группе
            for company, sites in mapping.items():
                if name in sites:
                    mfo[company] += sum(traffic) if traffic else 0
                    break
            
        except Exception as e:
            print(f"Ошибка при обработке {name}: {e}")

    time.sleep(5)
    driver.close()
    driver.quit()

    df_mfo = pd.DataFrame(list(mfo.items()), columns=['Компания', 'Суммарный трафик'])
    return df_mfo



