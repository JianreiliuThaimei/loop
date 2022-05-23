num=int(input("enter the number"))
i=1
count=0
while i<num:
    if num%i==0:
        count=count+1
    i=i+1
if count==1:
    print(num,"is prime number") 
else:
    print("not prime number")


# Q.no,9

# i=10
# while i<=99:
#     if i%2==0:
#         print(i)
#     i+=1