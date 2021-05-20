ran=input("enter the number of rows:")
rang=int(ran)
k = 1
for i in range(1, rang+1):
    for j in range(1, i+1):
        print(k, end=" ")
        k = k+1
    print()