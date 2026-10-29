rows=int(input("enter the no of row:"))
count=0
for i in range(rows+1):
    for j in range(1,i+1):
        count+=1
        print(count,end="")
    print()
