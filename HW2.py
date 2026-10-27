# №1
name = input("Введіть ваше ім'я: ")
age = input("Введіть ваш вік: ")
print(f"Привіт {name}, тобі {age}!")

# №2
age = int(input("Введіть ваш вік: "))
if age > 18:
    print("Вхід дозволено!")
else:
    print("Вхід заборонено!")

# №3
import random
12

secret = random.randint(1, 10)
print("Я загадав число від 1 до 10. У вас 3 спроби.")
for i in range(1, 4):
    guess = int(input(f"Спроба {i}: "))
    if guess == secret:
        print("Вітаю! Ви вгадали!")
        break
    elif guess > secret:
        print("Менше")
    else:
        print("Більше")
else:
    print(f"Спроби закінчились. Було загадано число {secret}.")

# №4
start = int(input("З якого числа: "))
end = int(input("По яке число: "))
for n in range(start, end + 1):
    print(n)

# №5
n = int(input("Введіть n: "))
last_even = n if n % 2 == 0 else n - 1
for i in range(last_even, 0, -2):
    print(i, end=" ")
print()

# №6
n = int(input("Введіть n для факторіала: "))
if n < 0:
    print("Факторіал визначений лише для невід'ємних чисел.")
else:
    result = 1
    for i in range(2, n + 1):
        result *= i
    print(f"{n}! = {result}")

# №7
score = int(input("Введіть кількість балів (0-100): "))
if score < 0 or score > 100:
    print("Некоректна кількість балів.")
elif score <= 49:
    print("Незадовільно")
elif score <= 69:
    print("Задовільно")
elif score <= 89:
    print("Добре")
else:
    print("Відмінно")

# №8
a = float(input("Введіть число a: "))
b = float(input("Введіть число b: "))
op = input("Введіть дію (+, -, *, /): ")
if op == "+":
    print(f"Результат: {a + b}")
elif op == "-":
    print(f"Результат: {a - b}")
elif op == "*":
    print(f"Результат: {a * b}")
elif op == "/":
    if b == 0:
        print("Ділення на нуль")
    else:
        print(f"Результат: {a / b}")
else:
    print("Невідома дія")
