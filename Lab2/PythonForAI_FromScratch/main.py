# ----------------------------- Basic Data Types ----------------------------- #
# print( type(4))  #
# print( type(4.45))
# print( type("4.45"))
# print( type('4.45'))
# print( type("""4.45"""))
# print( type('''4.45'''))
# print( type(True))


### Example 1
# price_without_vat = float(input("Please, enter price: "))
# vat_coefficient = 1.2

# print(price_without_vat * vat_coefficient)


# --------------------------- Arithmetic Operations -------------------------- #
# import math

# print(2**10)

# print(10 % 2)  # 0
# print(15 % 2)  # 1

# print(math.ceil(0.99))


# --------------------------- Comparison Operations -------------------------- #
# x = 5
# y = 10


# print(x == y)
# print(x != y)
# print(x < y)
# print(x <= y)
# print(x > y)
# print(x >= y)

# -------------------------- Conditional Statements -------------------------- #
# if 40 > 20:
#     print("*" * 30)
#     print("OK")
#     print("*" * 30)

### Find if x is even or odd
# x = int(input("x="))

# if x == 0:
#     print("Zero!")
# elif x % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# print("END")


# temperature = 45

# if temperature > 30:
#     print("Hot")
# elif temperature > 20:
#     print("Ideal")  # Executes
# else:
#     print("Cold")

# ----------------------------------- Loops ---------------------------------- #
### FOR each element in sequence
# user_names = ["Ada", "Ivan", "Maria"]

# for name in user_names:
#     print(name)

# print("END")

### WHILE condition is True:
# x = 6
# while x > 5:
#     print("hello")
#     # x = x - 1
#     x -= 1

# print("END")


# TASK: user must enter positive number
# age = int(input("Enter your age: "))

# while not (age > 0 and age <= 100):
#     print("Invalid Age!")
#     age = int(input("Enter your age: "))

# print("Thanks, your age is", age)


# ---------------------------- Collections of data --------------------------- #
# list: Подредена, променлива (mutable) колекция от елементи.
# list_of_numbers = [1, 2, 3]
# x = int(input("x="))  # 9
# list_of_numbers.append(x)
# print(list_of_numbers)  # [1,2,3,9]

# tuple: Подредена, непроменлива (immutable) колекция.
# birth_date = (1990, 8, 12)
# birth_date[0] = 1980
# print(birth_date[0])


# names = ('ada', 'maria')
# names[0] = 'pesho'
# print(names)

### Numbers are IMMUTABLE!
# x = 5
# x = 7

# RAM:
#      : 0x123:010101010101 (5 immutble)
#     x: 0x456:0111010101010 (7 immutable)
