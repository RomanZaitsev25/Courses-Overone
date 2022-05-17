# Дан словарь с числами. Необходима перемножить значения

d = {1: 2, 3: 6, 4: 3}

print(d.values())
resylt = 1
for i in d.values():
    resylt *= i
print(resylt)