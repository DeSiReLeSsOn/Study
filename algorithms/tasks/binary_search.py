"""binary search""" 

def binary_search(arr, target):
    low = 0 
    high = len(arr) -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid -1 
    return -1 

arr = [1, 2, 3, 4, 5, 6, 7, 1, 1000, 2222452525325235235, 45566666, -100]
 
target = 1000
print(binary_search(arr, target))