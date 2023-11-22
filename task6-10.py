def printallsublist(nums):
    for i in range (len(nums)):
        total=0
        for j in range(i,len(nums)):
            total+=nums[j]
            if total==0:
                print("sublist",(i,j))
if __name__=='__main__':               
     nums=[4,2,-3,1,6]
     printallsublist(nums)

