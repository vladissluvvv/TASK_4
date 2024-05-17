def calculator(v):
    op1, i, op2 = v.split()
    op1 = float(op1)
    op2 = float(op2)
    if i == '+':
        x = op1 + op2
    elif i == '-':
        x = op1 - op2
    elif i == '*':
        x = op1 * op2
    elif i == '/':
        x = op1 / op2
    else:
        x = "ошибка"
    return x
v = input(" ")
x = calculator(v)
print("результат: ", x)
