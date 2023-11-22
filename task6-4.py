num=int(input("enter integer:"))
last=num%10
while num!=0:
    first=num%10
    num=num//10
sum=first+last
print(sum)