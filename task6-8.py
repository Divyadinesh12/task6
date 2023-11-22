#find minimum element roted and sorted lisy
def findmin(list,N):
    min_else=list[0]
    for i in range(N):
        if list[i]<min_else:
           min_else=list[i]
    return min_else  
list=[5,4,6,3,2]    
N=len(list)
print(findmin(list,N))
