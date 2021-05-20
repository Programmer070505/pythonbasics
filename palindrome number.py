a=int(input("enter a number: "))
s=0
p=a
while p>0:
    r=p%10
    s=s*10+r
    p//=10
if a==s:
    print(a,"is a Palindrome Number")
else:
    print(a,"is not a Palindrome Number")