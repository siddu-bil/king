n=int(input("enter the value"))
rve=0
while n>0:
    digit=n%10
    rve=rve*10+digit
    n//=10
print("reverse of the number is:",rve)