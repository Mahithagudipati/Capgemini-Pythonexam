n=int(input("Enter the number of people present : "))
bill=int(input("Enter the bill amount : "))
tip=int(input("Enter the tip percentage : "))
t= (tip/100)*bill
total=bill+t
print(total/n)