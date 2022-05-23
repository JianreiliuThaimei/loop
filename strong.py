num=int(input("enter the no.:-"))
s=0
a=num
while a>0:
    f=1
    i=1
    r=a%10
    while i<=r:
        f=f*i
        i=i+1
    s=s+f
    a=a//10
if s==num:
    print("strong number")
else:
    print("not") 