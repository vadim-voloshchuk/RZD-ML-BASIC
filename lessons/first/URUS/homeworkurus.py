a = 4
count = 0
for i in range(a):
    print(" " * (4-i-1) + '*' * (2*i+1))
    count = count + (2*i+1)
else:
    print("  ***")
    count = count + 3
    print("Количество символов: " + str(count))


for i in range(1,11):
    if i % 2 == 0:
        print(i)


sum = 0
for i in range(1,11):
    if i % 3 == 0:
        sum += i
print(sum)

name = "Программирование на Python"
bukvy = "оаиеy"
sum = 0
for i in name:
    if i in bukvy:
        sum = sum + 1
print(sum)

annual_income = float(input("Введи годовой доход: "))
credit_history = int(input("Количество положительных историй: "))
for i in range(1):
    if annual_income >= 80000 and credit_history >= 2:
        print("Высокий рейтинг")
    elif annual_income >= 60000 and credit_history >= 1:
        print("Средний рейтинг")
    elif annual_income < 60000 and credit_history < 1:
        print("Низкий рейтинг")
    else:
        print('Невозможно присвоить рейтинг')

# if, elif, else