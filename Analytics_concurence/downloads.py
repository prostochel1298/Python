import pandas as pd
import numpy as np
from openpyxl import *
import setup_store  as ss
import wordstat_ten_1 as ws1
import wordstat_ten_2 as ws2
import web_traffic as wt
import datetime
from time import sleep
#----------------------------------------------------------------#
# Все необходимые функции лежат в соостветвующих файлах например парсер word
print("Начинаем")
def start_analyst():
    finalws = pd.concat([ws1.wordstat(),ws2.wordstat2()],ignore_index=True)
    print("Распознаем траффик")
    finallwt = wt.web_traffic()
    print("Трафик собран")
    print("Начинаем распознавать количество установок")
    finallapp = ss.store()
    today = datetime.date.today().strftime("%Y_%m_%d")

    with pd.ExcelWriter(fr'C:\Users\Admin\Documents\product_analytic\Concurence_{today}.xlsx') as writer:
        
        finalws.to_excel(writer, sheet_name='Wordstat', index=False)
        finallapp.to_excel(writer, sheet_name='Установки в сторах', index=False)
        finallwt.to_excel(writer, sheet_name='Веб-траффик', index=False)
    
    
start_analyst()
print('the_end')
sleep(5)
    