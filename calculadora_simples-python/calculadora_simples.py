def calculadora(op, x, y):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    else:
        return x / y


if __name__ == '__main__':
    op = input()
    x, y = input().split()
    x, y = [int(x), int(y)]

    calc = calculadora(op, x, y)
    print(calc)
    