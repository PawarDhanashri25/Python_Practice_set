# Factorial of number


def factorail(n):
    fact=1
    if (n==1 or n==0):
        return fact;
    else:
        for i in range(1,n+1):
            fact*=i
    return fact; 

n=int(input("Enter any number: "))
f=factorail(n)
print("factorail of number", f)

#inbuilt functions:-->
#1) (math.factorial(n))
#2) numpy.prod([i for i in range(1,n+1)])


        
