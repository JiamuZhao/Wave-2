num_odd = ['1', '3', '5', '7']
num_even = ['2', '4', '6', '8']
letter_odd = ['a', 'c', 'e', 'g']
letter_even = ['b', 'd', 'f', 'h']


def color(letter, num):
    if letter in letter_odd:
        if num in num_odd:
            print("Black")
        elif num in num_even:
            print("White")
    elif letter in letter_even:
        if num in num_odd:
            print("White")
        elif num in num_even:
            print("Black")


position = input("Please enter a position of the square: ")
color(position[0], position[1])