list=[10,501,22,37,100,999,87,351]
list1=[]
counter=0
for i in list:
    if i <=1:
       continue
    for j in range(2,i):
        if i%j==0:
         break   
    else:
     list1.append(i)
     counter+=1
print(list1)    
print("count prime number",counter)