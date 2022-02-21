# Выводит числа от 1 до 100 если кратно 3 то печатает Fizz если
# кратно 5 то Buzz если и так и так то печатает FizzBuzz

def task_1():
    for i in range(100):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)


# Создать список 18 14 10 6 2 функцией range
# print([i for i in range(18, 0, -4)])


# Дан список lst вывести элементы, которые одновременно меньше 30 и делятся на 3
# все остальные просуммировать

def task_3(lst: list):
    result = 0
    for elem in lst:
        if elem < 30 and elem % 3 == 0:
            print(elem)
        else:
            result += elem
    return result


# task_3([11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20])

# Функция, которая складывает два минимальных элемента из списка
def task_4(lst: list):
    return lst.pop(lst.index(min(lst))) + lst.pop(lst.index(min(lst)))


# print(task_4([1, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]))