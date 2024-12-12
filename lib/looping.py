#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    while True:
        print("10")
        print("9")
        print("8")
        print("7")
        print("6")
        print("5")
        print("4")
        print("3")
        print("2")
        print("1")
        print("Happy New Year!")
        break
    
    

def square_integers(int_list):
    # code goes here!
    while True:
        return [num**2 for num in int_list]
        

def fizzbuzz():
    # code goes here!
    while True:
        for i in range(1,101):
            if i % 15 == 0:
                print("FizzBuzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)
        break