list1 = []
list2 = []

n = int(input())

for i in range(n):
    value=int(input())
    list1.append(value)
for i in range(n):
    value=int(input())
    list2.append(value)
    
def summation(list1,list2):
    global n
    update_list = [0]*n 
    for i in range(n):
        update_list[i] = list1[i]+list2[i]
    # return list1+list2
    return update_list

def find_min_max(update_list):
    return (min(update_list),max(update_list))    


print(summation(list1,list2))
print(find_min_max(summation(list1,list2)))
