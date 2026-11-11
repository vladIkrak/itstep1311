import random


class Encryptor:
    def __init__(self, *numbers):
        if len(numbers) < 2:
            raise ValueError("At least two numbers are required")
        self.__numbers = numbers
        self.__result = self.__encrypt()

    def __add(self):
        result = 0
        for n in self.__numbers:
            result += n
        return result

    def __subtract(self):
        result = self.__numbers[0]
        for n in self.__numbers[1:]:
            result -= n
        return result

    def __multiply(self):
        result = 1
        for n in self.__numbers:
            result *= n
        return result

    def __encrypt(self):
        operation = random.choice([
            self.__add,
            self.__subtract,
            self.__multiply,
        ])
        return operation()

    def __str__(self):
        return str(self.__result)


first = Encryptor(3, 5, 2)
second = Encryptor(10, 4)
third = Encryptor(7, 1, 8, 2)

print("First:", first)
print("Second:", second)
print("Third:", third)