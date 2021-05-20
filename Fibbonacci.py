n=int(input("Enter a number you want to see the fibbonaci series: "))
print("Fibonacci Series:")
a=1
b=1
print(a)
print(b)
for i in range(0,10,1):
    c=a+b
    print(c)
    b=a
    a=c
