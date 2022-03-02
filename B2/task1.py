# Напишите программу, которая на вход получает последовательность чисел, а выводит модифицированный список:
# Первое и последнее числа последовательности должны поменяться местами.
# В конец списка нужно добавить сумму всех чисел.

string = "1 1 2 3 5 8 13 21 34 55";



list_of_strings = string.split() # список строковых представлений чисел
list_of_numbers = list(map(int, list_of_strings)) # cписок чисел

result = [i for i in list_of_numbers[:-1]]
result[0] = list_of_numbers[-1]
result.append(list_of_numbers[0])
result.append(sum(list_of_numbers))

print(result)