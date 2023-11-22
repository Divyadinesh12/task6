def has_duplicate(seq):
     return len(seq)!=len(set(seq))
#list is duplicate print true not duplicate print false]
list_1=[0,123,8,9]
print(has_duplicate(list_1),list_1)
list_2=[2,5,2]
print(has_duplicate(list_2),list_2)
list_3=[8,5,9,6,3,6]
print(has_duplicate(list_3),list_3)