# FizzBuzz Problem
#    - Write a program that prints numbers from 1 to 100, but:
#      - Prints "Fizz" for multiples of 3.
#      - Prints "Buzz" for multiples of 5.
#      - Prints "FizzBuzz" for multiples of both 3 and 5.

for i in range(1,100):
    if(i%3==0 and i%5==0):
        print("Fizzbuzz")
    elif(i%3==0):
        print("fizz")
    
    elif(i%5==0):
        print("buzz")
    
    else:
        print(i)