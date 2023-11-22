def firstnon_repeated(lst):
    ctr={}
    for i in lst:
        if i in ctr:
            ctr[i]+=1
        else:  
            ctr[i]=1
    for i  in lst:
        if ctr[i]==1:
          return (i) 
nums=[2,3,8,55,89,55,2,3] 
print("orginal list:")
print(nums)
result=firstnon_repeated(nums)
print(result)
                
