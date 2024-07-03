try:
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))

    c=a/b

except:
    print("Exception occured")
else:
    print("No Errors")
    print(f"c={c}")
finally:
    print("Good Bye!")


