a=int(input("enter a number: "))
c=0
d=0
if a>1:
    for i in range(2,a,1):
        if (a%i)==0:
            print(a, "Is a Not Prime Number")
            break
    else:
        print(a, "Is  a Prime Number")
else:
    print(a, "Is Not a Prime Number")