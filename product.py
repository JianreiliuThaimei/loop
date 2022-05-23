i=1
n=1
while i<=5:
    n=n*1
    print(i)
    i+=1
    print("the product of any number is=",n) 

    n=int(input("enter the number"))
num=1
i=1
while i<=n:
    j=1
    while j<=n:
        print(num,end=' ')
        num=num+2
        j+=1
    print()
    i+=1