n=int(input("enter the number"))
n2=int(input("enter the number"))
if n>n2:
    ref=n
else:
    ref=n2
    while True:
        if n%ref==0 and n2%ref==0:
            break
        else:
            ref=ref-1
print("in HCF("+str(n)+","+str(n2)+")=",ref)