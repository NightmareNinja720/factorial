ch='y'
while (ch=='y') or (ch=='Y'):
    a=int(input("enter the no. of which you want to find factorial:"))
    pr=1
    for i in range(1,a+1):
        pr=pr*i
    print(pr,"is the factorial of",a)
    ch=input("do you want to do more:")
print("goodbye")
