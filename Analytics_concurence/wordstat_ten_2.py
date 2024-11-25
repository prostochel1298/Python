import pandas as pd
import numpy as np
from openpyxl import *
from wsparser import WordstatParser
import time

# Задаем URL адрес API Яндекс.Директа
# Адрес песочницы: url ='https://api-sandbox.direct.yandex.ru/v4/json/' 
url ='https://api.direct.yandex.ru/v4/json/'
#url ='https://api-sandbox.direct.yandex.ru/v4/json/' 
# Указываем свой токен на доступ к API Яндекс.Директ
token = 'y0_AgAAAAAHsYDeAAxVkgAAAAEPCMdcAAAhKEdip89Cl41q-VwOHUb00cHrvg'
# Указываем логин своей учетной записи от Яндекс.Директ
userName = 'madking96'

def wordstat2():  
    minusWords = [
        
        ]

    # Пишем список фраз, по которым будем парсить    
    phrases = [
        
        'А Деньги',
        'миг кредит',
        'ЭйрЛоанс',
        'Kviku',
        'Лайм-Займ',
        'Займер',
        'Веб-займ',
        'Money Man',
        'Платиза.ру',
        'Мани Мен'

        ]

    # Указываем регион, при необходимости (можно оставить пустым)        
    geo = []

    # Добавляем минус-слова ко всем фразам
    data = []
    for i in range(len(phrases)):
        data.append(phrases[i])
        for j in range(len(minusWords)):
            data[i] += ' '+minusWords[j]

    # Создаем парсер
    parser = WordstatParser(url, token, userName)

    try:
        # Запрашиваем кол-во оставшихся баллов Яндекс.Директ API
        units = parser.getClientUnits()
        if 'data' in units:
            print ('>>> Баллов осталось: ', units['data'][0]['UnitsRest'])
        else:
            raise Exception('Не удалось получить баллы', units)

        # Отправляем запрос на создание нового отчета на сервере Яндекс.Директ
        response = parser.createReport(data, geo)
        if 'data' in response:
            reportID = response['data']
            print ('>>> Создается отчет с ID = ', reportID)
        else:
            raise Exception('Не удалось создать отчет', response)
            
        # Проверяем список отчетов на сервере. Должен появиться новый. Ожидаем его готовности
        reportList = parser.getReportList()
        if 'data' in reportList:
            lastReport = reportList['data'][len(reportList['data'])-1]
            i = 0
            while lastReport['StatusReport'] != 'Done':
                print ('>>> Подготовка отчета, ждите ... ('+str(i)+')')
                time.sleep(2)
                reportList = parser.getReportList()
                lastReport = reportList['data'][len(reportList['data'])-1]
                i+=1
            print ('>>> Отчет ID = ', lastReport['ReportID'], ' получен!')
        else:
            raise Exception('Не удалось прочитать список отчетов', reportList)

        # Читаем отчет
        report = parser.readReport(reportID)
        if 'data' in report:
            # Сохраняем результаты парсинга в файлы (отдельно фразы, отдельно частотности). 
            # Если rightCol == True, будет сохраняться правая колонка Яндекс.Вордстат (в дополнение к левой)
            parse = []

            for i in range(len(report['data'])):
                for j in report['data'][i]['SearchedWith']:
                    parse.append(j)
                    break
        
                #df = pd.DataFrame(parse)  
            mapping = {"Money Man":['moneyman', 'платиза.ру', 'мани мен'],
               "ЭйрЛоанс":['ЭйрЛоанс','Kviku'],
               "Академическая":['Веб-займ'],
               "Лайм-займ":['Лайм-Займ'],
               "Миг-кредит":['миг кредит'],
               "А-Деньги":['А Деньги'],
               "Займер":['Займер']

               }      
            
            
            mapping = {key: [phrase.lower() for phrase in phrases] for key, phrases in mapping.items()} 
            result = {key: 0 for key in mapping}
            for item in parse:
                phrase = item['Phrase'].lower()  # Приводим фразу к нижнему регистру
                shows = item['Shows']

                for category, phrases in mapping.items():
                    if phrase in phrases:
                        result[category] += shows
                        break        
            df_mfo = pd.DataFrame(list(result.items()), columns=['Компания', 'Количество показов'])            
        else:
            raise Exception('Не удалось прочитать отчет', report)
        
        # Удаляем на сервере Яндекс.Директ новый отчет (он больше не нужен)
        report = parser.deleteReport(reportID)
        if 'data' in report:
            print ('>>> Отчет с ID = ', reportID, ' успешно удален с сервера Яндекс.Директ')
        else:
            raise Exception('Не удалось удалить отчет', report)
        
        print ('>>> Все готово!')
       
    
    except Exception as e:
        print ('>>> Поймано исключение:', e)
    return df_mfo
