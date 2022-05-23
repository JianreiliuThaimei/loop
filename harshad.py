# num=int(input("enter the number"))
# temp=num
# sum=0
# while temp>0:
#     remainder=temp%10
#     sum=sum+remainder
#     temp=temp//10
# if num%sum==0:
#     print(num,"harshad number")
# else:
#     print("not")

num=int(input("enter the number"))
b=num
sum=0
while b>0:
    remainder=b%10
    sum=sum+remainder
    b=b//10
if num%sum==0:
    print(num,"harshad number")
else:
    print("not")