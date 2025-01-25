n = list(map(int, input("Enter a list of numbers separated by comma: ").split(",")))
odd = []
even = []
for i in n:
    if i % 2 == 0:  
        even.append(i)
    else:
        odd.append(i)
print("Odd numbers:", odd)
print("Even numbers:", even)

