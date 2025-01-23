def fun_lst(arr):
    return fun_int(arr)

def fun_int(arr, i = 0):
    if(i == len(arr)):
        return 0
    if(type(arr[i]) == type([])):
       return fun_lst(arr[i]) + fun_int(arr, i + 1)
    else:
        return arr[i] + fun_int(arr, i + 1)

arr = [1, 2, [3,4], [5,6]]
arr = [1, 2, [3,4,[5,5,[1,2]]], [5,6]]
print(fun_int(arr, 0))
import unittest
print("unittest module is available")
