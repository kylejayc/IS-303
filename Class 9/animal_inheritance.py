class Animal:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Animal: {self.name}"

class Dog(Animal):
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __str__(self):
        base = super().__str__()
        return f"{base} ({self.breed})"

class Rabbit(Animal):

    def run(self):
        print("Rabbit is running.")



print(Dog("Rex", "Labrador"))
print(Rabbit("Fluffy"))