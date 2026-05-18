# Puzzle 2
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Emma"))
print(greet("Mike", "Hey"))
print(greet("Steve"))
print(greet(greeting="Yo", name="Sam"))

x = 10

# Puzzle 3
def change_x():
    x = 99
    return x

result = change_x()
print(result)
print(x)