class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

circle = Circle(color="red", radius=5)
rect = Rectangle(color="blue", width=4, height=6)

print(circle.area())
print(rect.area())





class human:
    name = "goblin"
    age = 120
    city = "cave"
    hair = "bald"
    talant = "high jump"

print(f"Його звати {human.name}, йому {human.age} років, він живе в {human.city}, має зачіску {human.hair} і любить {human.talant}")