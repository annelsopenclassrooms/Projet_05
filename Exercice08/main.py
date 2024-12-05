def log_decorator(func):

    def wrapper():

        print("Massage avant")

        result = func()

        print("Message apres")

        return result

    return wrapper


@log_decorator
def function_test():
    print("Cette fonction ne prend pas d'arguments.")


function_test()
