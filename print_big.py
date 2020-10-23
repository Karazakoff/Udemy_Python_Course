def print_big(letter):
    dict = {'a': "  *  \n * * \n*****\n*   *\n*   *\n",
            'b': "**** \n*   *\n**** \n*   *\n**** \n",
            'c': " ****\n*\n*\n*\n ****\n",
            'd': "**** \n*   *\n*   *\n*   *\n**** \n",
            'e': "*****\n*\n*****\n*\n*****\n"
            }
    if letter in dict.keys():
        print(dict[letter])

print_big('e')
