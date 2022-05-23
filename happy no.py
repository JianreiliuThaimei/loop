n=int(input("enter the number"))
temp=n
while sum!=1 and sum!=4:
    sum=0
    while temp !=0:
        r=temp%10
        sum=sum+r*r
        temp=temp//10
    temp=sum
if sum==1:
    print("happy number")
else:
    print("not")    



# num=int(input("enter the number"))
# i=1
# sum=0
# while i<num:
#     if (num%i==0):
#         sum=sum+i
#     i+=1
# if (sum==num):
#     print("%d perfect no."%num)
# else:
#     print("%d not perfect no."%num)
 
# n=int(input("enter the number"))
# temp=n
# while sum!=1 and sum!=4:
#     sum=0
#     while temp!=0:
#         r=temp%10
#         sum=sum+r*r
#         temp=temp//10
#         temp=sum
# if sum==1:
#     print("happy no.")
# else:
#     ("not")