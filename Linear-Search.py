def linear_search(arr,target):
    size=len(arr)
    for index in range(0,size):
        if(arr[index]==target):
            return index
    return -1
my_list=[10,12,34,25,56,70]
target=70
result=linear_search(my_list,target)
print(result)