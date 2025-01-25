import random
i = random.randint(1, 100)
while True:
    n=int(input())
    if(i>n):
        print("higher")
    elif(i<n):
        print("lower")
    elif(i==n):
        print("yes,thats the right answer")
    print(i)