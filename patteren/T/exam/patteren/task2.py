"""rows=int(input("enter the number of rows:"))
for i in range(rows):
    print(" "*(rows-i),end="")"""
str1=input("enter first string:")
str2=input("enter second string:")
str1=str1.replace("","").lower()
str2=str2.replace("","").lower()
if sorted(str1)==sorted(str2):
    print("the strings are anagrams")
else:
    print("the strings are not anagrams")