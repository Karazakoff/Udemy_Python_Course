def decoration(some_func):

    def new_func():

        print("Do some action")

        some_func()

        print("The end of the action")

    return new_func


@decoration
def func_decorated():
    print("I wanna be decorated")

func_decorated()
