# Бесконечный счетчик
def count(start, step):
    counter = start
    while True:
        yield counter
        counter += step

my_gen_func = count(100, 10)
for i in range(10):
    print(next(my_gen_func))

# Последовательность чисел Фибоначи
def fib():
    a, b = 0, 1
    yield a
    yield b

    while True:
        a, b = b, a + b
        yield b

# Запускай это только через точку останову и дебаг!!!
for i in fib():
    print(i)