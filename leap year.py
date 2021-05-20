y=input("enter a year:")
a=int(y)
if (a%4== 0) :
    print("it is a leap year")
elif (a%100 ==0):
    print("it is a leap year")
elif (a%400==0):
    print("it is a leap year")
else:
    print("it is not a leap year")