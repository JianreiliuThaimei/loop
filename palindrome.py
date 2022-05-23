# n=int(input("enter the number"))
# temp=n
# reversed=0
# while temp>0:
#     remainder=temp%10
#     temp=temp//10
#     reversed=reversed*10+remainder
# if n==reversed:
#     print("palindrome")
# else:
#     print("not")


n=int(input("enter the no."))
d=n
r=0
while (n>0):
    digit=n%10
    r=r*10+digit
    n=n//10
if(d==r):
    print("palindrome no.")
else:
    print("not")