# def greet(user_name):
#     # user_name = 'Maria'
#     '''
#         function which greets a user!
#     '''
#     print('*' * 30)
#     print('Hello', user_name)
#     print('*' * 30)

# def foo(user_name):
#     # user_name = 'Pesho'
#     print(user_name)

# print('Start')
# greet('Maria')
# print('End')


# ---------------------------------- Example --------------------------------- #
# def add(x,y):
#     #x=2, y=3
#     print(x+y)


# add(2,3) # 5
# add(4,5) # 9

# Keyword Arguments/Paramether
# def do_something_with_user_data(
#         name,
#         age,
#         town,
#         eye_color
# ):
#     print('Hello', name)
#     print(f'You are {age} years old')
#     print(f'You are from {town}')
#     print(f'Your eyes are {eye_color}')


# do_something_with_user_data('Maria', 'Blue', 23, 'Sofia')
# print('*' * 30)
# do_something_with_user_data(
#     name='Maria',
#     eye_color='Blue',
#     age=23,
#     town='Sofie'
# )

# ------------------------ Default  Paramether Values ------------------------ #
# def do_something_with_user_data(age='undefined',name='Anonymous'):
#     print(f'Hello {name}, you are {age} years old!')


# # do_something_with_user_data(23, 'Maria')
# do_something_with_user_data()

# --------------------------- Function Return Value -------------------------- #
# def mult(x,y):
#     return x*y
#     print('Hello')

# def cub(x):
#     res=x**3
#     print(res)
#     return res

# print( mult(2,3) + cub(2) )
# # print( 6 + cub(2) )
# # print( 6 + 8 )
# # print( 14 )

# #8
#14

# ---------------------------------- Example --------------------------------- #
# def is_even(x):
#     if x%2==0:
#         return True
#     else:
#         return False

# x = 5
# if is_even(x):
#     print('Even')


# ---------------------------- Scope and Namespace --------------------------- #
# def foo():
#     x=9
#     print(f'x in foo = {x}') #9

# def bar():
#     x = 100
#     print(f'x in bar = {x}')


# x=5
# foo()
# print(f'x in global = {x}')

# global:
#     foo: function...
#     bar: function...
#     x:5

# foo:
#     x:9


# ---------------------------------- Example --------------------------------- #
# def greet(user_name):
#     # user_name='Pesho
#     print(f'Hello from local {user_name}')


# user_name = "Maria"
# greet('Pesho')
# print(f'Hello from global: {user_name}')

# # Hello from local: Pesho
# # Hello from global: MAria
# # global:
# #     user_name: Maria

# # greet:
# #     user_name:Pesho

# ---------------------------------- Example --------------------------------- #
x = 1

def foo():
    print(f"x = {x} във foo")

foo()
# x = 99 във foo

print(f"x = {x} извън foo")
# x = 1 извън foo


# global:
#     x: 1
#     foo: function...

# foo:










