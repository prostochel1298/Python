import pandas as pd

# Создаем массив данных
data = {
    'Имя': ['Анна', 'Борис', 'Карла', 'Дмитрий'],
    'Возраст': [25, 30, 22, 35],
    'Город': ['Москва', 'Санкт-Петербург', 'Киев', 'Минск']
}

# Создаем DataFrame
df = pd.DataFrame(data)

# Выводим массив данных
print(df)