n=int(input("enter the number"))
i=1
sum=0
avg=0
while i<=n:
    num=int(input("enter the number:-"))
    sum=sum+num
    avg=sum/n
    i+=1
print(sum)
print("avg=",avg)