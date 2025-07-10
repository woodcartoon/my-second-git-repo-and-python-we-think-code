# functions are used to perform specific tasks
# functions can take inputs and return outputs


print("Hello World")


def get_user_input():
    user = input("please enter your name: ")
    return user


def greet_user():
    user = get_user_input()
    print(f"hello {user}, welcome to WETHINKCODE")


print(greet_user())
