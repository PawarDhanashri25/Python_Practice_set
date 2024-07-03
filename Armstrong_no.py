# check the given nummber is armstrong or not


def armstrong(n):
    num_str=str(n)
    no=len(num_str)
    copy=n
    sum=0
    while(n>0):
        d=n%10
        sum+=pow(d,no)
        n=n//10
    if(sum==copy):
        return True
    else:
        return False


n=int(input("Enter any number:"))
print(armstrong(n))


        
