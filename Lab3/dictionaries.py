# ------------------------------ Lists: Example ------------------------------ #
# numbers = [1,2,3,4]
# print(len(numbers))

# user1 = ['Maria', 23]
# print(user1[1])



# ------------------------------- Dictionaries ------------------------------- #
# user1 = {
#    'name' : 'Maria',
#    'age'  : 23
# }

# print(user1['age'])

# d1 = {
#     'a':1,
#     'b': [1,2,3]
# }

# print(d1['b'][1])

# RAM:
# user1:            0X324: ..
# user1['name]:   0x123: 'Maria'
# user1['age]:   0x113: 23


### Loops on dictionaries

users = {
    'Maria':23,
    'Ivan':45
}
for name in users.keys(): # ['Maria', 'Ivan']
    print(name)

for age in users.values(): #[23,45]
    print(age)