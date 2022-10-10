# Задача №2 Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

number = int(input("Введите число: "))
primeNum = 2
primeList = []
initial = number
while primeNum <= number:
    if number % primeNum == 0:
        primeList.append(primeNum)
        number //= primeNum
        primeNum = 2
    else:
        primeNum += 1
print(f"Список простых множителей {primeList} числа {initial}")