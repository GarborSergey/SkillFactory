# Попробуйте теперь самостоятельно подсчитать произведение всех чисел от 1 до N включительно.
P = 1
N = 5
for i in range(1, N+1):
    P *= i
print(P)

# Написать программу, которая будет печатать лесенку следующего типа:
P = 123
for i in range(1, P+1):
    print('*'*i)

# Дана двумерная матрица 3x3 (двумерный массив). Определить максимум и минимум каждой строки, а также их индексы.
random_matrix = [
   [9, 2, 1],
   [2, 5, 3],
   [4, 8, 5]
]

max1 = [random_matrix[0][0], 0, 0]
max2 = [random_matrix[1][0], 1, 0]
max3 = [random_matrix[2][0], 2, 0]

for str in random_matrix:
    if random_matrix.index(str) == 0:
        for i in str:
            if i > max1[0]:
                max1[0] = i
                max1[2] = str.index(i)
    elif random_matrix.index(str) == 1:
        for i in str:
            if i > max2[0]:
                max2[0] = i
                max2[2] = str.index(i)
    elif random_matrix.index(str) == 2:
        for i in str:
            if i > max3[0]:
                max3[0] = i
                max3[2] = str.index(i)

print(max1)
print(max2)
print(max3)

# Начинающий программист написал программу, которая находит индекс последнего отрицательного элемента в списке.
