#CHECKING ALPHABETS

c=input("Enter Character ")

if len(c)>1:
    print("Enter only one character")
else:
    if (c>='a' and c<='z') or (c>='A' and c<='Z'):
        print(c," is an alphabet")
    else:
        print(c," is not an alphabet")
