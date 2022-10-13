ch='y'
while (ch=='y') or (ch=='Y'):
    a=int(input("Enter the number of which you want to find factorial:"))
    pr=1
    for i in range(1,a+1):
        pr=pr*i
    print(pr,"is the factorial of",a)
    ch=input("Do you want to do more:")
print("Goodbye")
