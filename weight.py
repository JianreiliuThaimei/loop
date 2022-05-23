# Q.no.5
i=0
weight_total=0
while i<11:
    weight=int(input("enter the number"))
    i+=1
    weight_total=weight_total+weight
print(weight_total)
average=weight_total/11
print(average)
if average%5==0:
    print("multiple of 5")
else:
    print("not multiple of 5")
    i+=1

#  Q.take one user input ,if it is even print user input 4 times n if it is odd print 3 times
num= int (input("enter the number"))
if num%2==0:
    i=1
    while i<=4:
        print("enter:-")
        i+=1
else: 
    i=1
    while i<=3:
        print("enter:")
        i+=1