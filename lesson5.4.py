import inspect


class Human:
    def __init__(self, age, height, name="Steve"):
        self.age = age
        self.name = name
        self.secondname = "Jobs"


sig = inspect.signature(Human)
for param in sig.parameters.values():
    print(param.name, param.default)
