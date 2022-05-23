n=20
i=0
count=0
while i<=n:
    if n%i==1:
        count=count+1
    i+=1
if count==2:
    print("prime no.")
else:
    print("not")