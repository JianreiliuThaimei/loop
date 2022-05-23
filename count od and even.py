odd_count =0
even_count = 0
i=0
while i<=15:
    if i%2==0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1
    i+=1
print(even_count,"even number")
print(odd_count,"odd number")