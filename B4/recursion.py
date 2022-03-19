# С помощью рекурсивной функции найдите сумму чисел от 1 до n.
def rec_sum(N):
    if N == 1:
        return 1
    return N + rec_sum(N - 1)


# С помощью рекурсивной функции развернуть строку.
def u_turn(str: str):
    if len(str) == 0:
        return ''
    else:
        return str[-1] + u_turn(str[:-1])


# Рекурсивную функцию, которая считает до 0 от n
def sets(n):
    if n == 0:
        return print('end')
    else:
        print(n)
        return sets(n - 1)

# Дано натуральное число N. Вычислите сумму его цифр.
# При решении этой задачи нельзя использовать строки, списки, массивы (ну и циклы, разумеется)
def sum_numbers(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_numbers(n//10)

