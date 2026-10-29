"""rows=int(input("enter the number of rows:"))
for i in range(rows,0,-1):
    for j in range(i):
        print(j,end="")
    print()"""
"""rows=int(input("enter the number of rows:"))
for i in range(1,rows+1):
    for j in range(rows-i):
        print("",end="")
    for j in range(1,i+1):
      print("*",end="")

    print()"""
text="Hello Python World"
print("original String:",text)
print("Upper:",text.upper())
print("Lower:",text.lower())
print("Strip:",text.strip())
words=text.strip().split()
print("split:",words)
print("join:",'-'.join(words))
print("replace:",text.replace("Python","Java"))
print("find:",text.find("Python"))