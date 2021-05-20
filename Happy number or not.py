n=int(input("Enter a 3 digit number: "))
s=0
p=n
for i in range(0,3,1):
        s=n%10
        n//= 10
        r=s
if r==0:
    print(p," is not a happy number")
else:
    print(p,"is  a happy number")