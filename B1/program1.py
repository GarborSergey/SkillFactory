# "Анализ валютного портфеля"
# 1. Как хранить данные
# 2. Функции для построения графиков в консоли
# 3. Добавление информации
# 4. Функции для подсчета статистики

# Данные хранятся в словаре, где ключ это номер недели,
# а значение список из словарей с каждой валютой, имя, стоимость в долларах, количество у нас
import json
from copy import deepcopy

d = {
    '20': [{'name': 'RUB',
            'cost': 0.01354,
            'amount': 1000
            },
           {'name': 'BTS',
            'cost': 36000,
            'amount': 0.003
            }
           ],
    '21': [{'name': 'RUB',
            'cost': 0.01354,
            'amount': 2000
            },
           {'name': 'BTS',
            'cost': 36000,
            'amount': 0.006
            }
           ]
}


# Функция по записи информации в файл
def save_data(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=2)


# Функция по чтению информации из файла
def load_data():
    with open('data.json') as file:
        data = json.load(file)
    return data


def show_percent(name, percent, width=50):
    fill = '█'
    empty = '-'
    bars = round(percent*width)
    progress = fill * bars + empty * (width - bars)
    # : 10 означает что под строку выделили 10 символов
    print(f"{name:7} - {round(percent*100)}% {progress}")

def plot_stat(data, sings, height=12):
    # Идем по строкам
    for i in range(height):
        if i % 3 == 0:
            current = max(data) - (max(data)-min(data))/height * i
            line = f"{str(round(current, 2)):10}"
        else:
            line = ' '*10
        for num in data:
            # Будет ли это значение на данной высоте
            if max(data) - (max(data)-min(data))/height * (i+1) <= num:
                line += '█   '
            else:
                line += '    '
        print(line)
    print(f"{str(round(min(data), 2)):10}"+ '█   ' * len(data))
    print(' ' * 10 + '█   ' * len(data))
    print(' '*9, end=' ')

    for sing in sings:
        print(sing + '  ', end=' ')

def select_mode():
    print()
    print("-"*30)
    print(' select work mode:')
    print(' 1. Add new week')
    print(' 2. Copy new week')
    print(' 3. Add information obout currency')
    print(' 4. Change information about currency')
    print(' 5. Exit program')
    print("-" * 30)
    print()

    return int(input('mode --->'))

def loop():
    data = load_data()

    while True:
        mode = select_mode()
        if mode == 1:
            week = input('Input number a new week --->')
            data[week] = []
        elif mode == 2:
            week = input('Input number a new week --->')
            from_week = input('Number week to copy? --->')
            data[week] = deepcopy(data[from_week])
        elif mode == 5:
            break
        else:
            print('!!!not correct command!!!')
        save_data(data)
loop()
plot_stat([1, 3, 4, 6, 10], ['A', 'B', 'C', 'D', 'E'])