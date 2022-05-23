n=int(input("enter the number"))
i=0
sum=0
while(n):
    num=n%10
    sum=sum+num*pow(2,1)
    n=int(n/10)
    i+=1
    print("decimal num :-",sum)