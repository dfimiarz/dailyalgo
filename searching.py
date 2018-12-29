import functools
from typing import List


list = [0,1]

target = 1

def linear_search(data:List,target:int):
    for item in data:
        if target == item:
            return True
    
    return False

def binary_search_iterative(data:List,target:int):

    item_count = len(data)

    left_b = 0
    right_b = item_count - 1

    

    while left_b <= right_b :
        index = (right_b + left_b) // 2

        print("index {}, left {}, right {}, item {}".format(index,left_b,right_b,data[index]))

        if data[index] == target:
            return True

        if target > data[index]:
            ''' If target is > than item under index, make left = index + 1 '''
            left_b = index + 1
        else:
            ''' If target is < than item under index, make right = index - 1 ''' 
            right_b = index - 1
            
    return False

def binary_search_recursive(data,target,left,right):

    print("Left {}, right {}".format(left,right))

    if left > right:
        return False
    else:
        index = ( right + left ) // 2
        print("index {}, left {}, right {}, item {}".format(index,left,right,data[index]))
        if target == data[index]:
            return True
        elif target > data[index]:
            ''' If target is > than item under index, make left = index + 1 '''
            return binary_search_recursive(data, target, index+1, right)
        else:
            ''' If target is < than item under index, make right = index - 1 '''  
            return binary_search_recursive(data, target, left, index - 1 ) 


print('Linear search found: {}'.format(linear_search(list,target)))
print('Linear binary search found: {}'.format(binary_search_iterative(list,target)))
print('Recursive binary search found: {}'.format(binary_search_recursive(list,target,0,len(list)-1)))

