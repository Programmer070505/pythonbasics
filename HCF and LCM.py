a=int(input("enter a smaller number: "))
b=int(input("enter a bigger number: "))
r=a*b
while (b!= 0):
    t = b
    b = a%b
    a = t
hcf=a
lcm=r/hcf
print("HCF =" ,hcf)
print("LCM =" ,lcm)