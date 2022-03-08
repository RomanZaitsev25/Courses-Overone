# Дан словарь с числами. Необходима перемножить значения

d = {1: 2, 3: 6, 4: 3}

print(d.values())

result = 1
for i in d.values():
    result *= i
print(result)
