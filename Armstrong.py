a=int(input("enter a number: "))
p=a
s=0
while p!= 0:
    r=int(p%10)
    s=s+(r**3)
    p//=10
if s==a:
    print(a,"Is an Armstong Number")
else:
    print(a,"Is Not an Armstrong Number")