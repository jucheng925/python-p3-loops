#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")

def square_integers(int_list):
    square_ints = list()
    for int in int_list:
        square_int = int * int
        square_ints.append(square_int)
    return square_ints

def fizzbuzz():
    for i in range(1, 101):
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    
