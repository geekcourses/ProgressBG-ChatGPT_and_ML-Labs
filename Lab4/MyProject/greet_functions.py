def greet(user_name):
    '''
        function which greets a user!
    '''
    print('*' * 30)
    print('Hello', user_name)
    print('*' * 30)

def get_user_name():
    user_name = input('Enter your name: ') # ada


    if user_name.isalpha():
        return user_name   #ada
    else:
        print('Wrong Input')
        exit()