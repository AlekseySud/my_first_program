a = int(input('Введите целое число а: '))
b = int(input('Введите целое число b: '))
rang = []
for a in range(0, a):
    if a%b == 0:
        rang.append(a)
res = sum(rang)
print(res)