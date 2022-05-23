num=int(input("enter the nubmer"))
i=1
count=0
while i<=num:
    if num%i==0:
        count=count+1
    i+=1
if count==2:
    print("prime number")
    i=0
    rev=0
    while num>0:
        rev=rev*10+num%10
        num=num//10
i=1
count=0
while i<=num:
    if num%1==0:
        count=count+1
    i+=1
if count==2:
    print("twisted prime number")
else:
    print("not") 