
def findtriplet(list,k):
     triplet_count=0
     final_templist=[]
     for i in range(0,len(list)-1):
          s=set()
          temp_list=[]
          temp_list.append(list[i])  
          curr_k =k-list[i]     
          for j in range (i+1,len(list)):
               if (curr_k-list[j]) in s:
                    triplet_count+=1
                    temp_list.append(list[j])
                    temp_list.append(curr_k-list[j])
                    final_templist.append(tuple(temp_list))
                    temp_list.pop(2)
                    temp_list.pop(1)
               s.add(list[j])    
     return final_templist   
list=[10,20,30,9]    
k=59
print(findtriplet(list,k))