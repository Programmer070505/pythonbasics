a = 0
b = 1
n=int(input("Enter the number of fibbonaci seriaes you want to see: "))
print(a)
print(b)

for i in range(1, n+1, 1):
    c = a + b
    print(c)
    a = b
    b = c