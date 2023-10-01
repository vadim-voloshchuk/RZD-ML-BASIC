# Первое впечатление
# Типы данных: int, float, string
# Конструкция: if, for
hello_string = "Привет всем!"

age = 0

num = 10

for i in range(num):
    age = age + 1 

    if (age > 5) != False:
        second_string = "Мне всего лишь: " + str(age)
        first_int = len(hello_string)
        second_int = len(second_string)
        result = first_int + second_int
        result_string = "В сумме строк " + str(result) + " символов"
        print(hello_string, second_string)
        print(result_string)