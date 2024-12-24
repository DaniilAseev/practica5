import math

def sin_series(x, n_terms=10):
    """
    Вычисляет синус числа x с использованием ряда Маклорена.

    Аргументы:
    x (float): Значение, для которого вычисляется синус.
    n_terms (int): Количество итераций для вычисления ряда.

    Возвращает:
    float: Значение синуса x.
    """
    result = 0
    for n in range(n_terms):
        term = (-1)**n * x**(2*n+1) / math.factorial(2*n+1)
        result += term
    return result

def sh_series(x, n_terms=10):
    """
    Вычисляет гиперболический синус числа x с использованием ряда Маклорена.

    Аргументы:
    x (float): Значение, для которого вычисляется гиперболический синус.
    n_terms (int): Количество итераций для вычисления ряда.

    Возвращает:
    float: Значение гиперболического синуса x.
    """
    result = 0
    for n in range(n_terms):
        term = x**(2*n+1) / math.factorial(2*n+1)
        result += term
    return result