import math
def is_prime(n):
    c=0
    if n==0 or n==1:
        return False
    if n==2 or n==3:
        return True
    else:
        for i in range(1,int(math.sqrt(n)+1)):
            if n%i==0:
                c+=1
            else:
                continue
    if c>1:
        return False
    return True
def find_primes(a,b):
    primes=[]
    for num in range(a,b+1):
        if is_prime(num):
            primes.append(num)
    return primes

def main():
    a=int(input("Enter starting number : "))
    b=int(input("Enter an ending number : "))
    primes=find_primes(a,b)
    print(primes)
main()