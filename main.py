# Функция Остаток от деления
def modulus(a, b):
    if b == 0:
        raise ValueError('На ноль делить нельзя')
    return  a % b