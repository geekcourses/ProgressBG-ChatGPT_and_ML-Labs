def greet(user_name):
    '''
        function which greets a user!
    '''
    print('*' * 30)
    print('Hello', user_name)
    print('*' * 30)

def get_user_name():
    user_name = input('Enter your name: ')
    print(isinstance(user_name, str))

    if not isinstance(user_name, str):
        print('Wrong Input')
        exit()
    else:
        return user_name


user_name = get_user_name()
greet(user_name)