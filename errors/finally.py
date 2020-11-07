def ask_user_input():
    while True:
        try:
            number = int(input("Please provide a number: "))
        except:
            print("Something went Wrong!")
            continue
        else:
            print("We got a number")
            break
        finally:
            print("I will always run!")
#
# ask_user_input()

try:
    f = open("testfile", 'r')
    f.write("Write a test line")
except TypeError:
    print("There was a Type problem")
except OSError:
    print("We have got an OSError")
finally:
    print("I will always run")
