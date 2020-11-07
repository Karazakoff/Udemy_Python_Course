while True:
    try:
        number = int(input("Please provide a number to see the square of this number: "))
    except ValueError:
        print("Something went wrong")
    else:
        print("Thank you, your number squared is: {}".format(number ** 2))
        break
