'''
How Binary Search works:
    1. Check the value in the center of the array
    2. If the target is lower, search the left half of the array. If the target is higher, search the right half of the array
    3. Repeat the first two steps with the new subarrays until the target is found, or until the search area is empty
    4. If the value is found, retuen the target value index. Otherwise, retuen -1

Time Complexity:
Space Complexity: 
'''

#Binary Search function:
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        
    return -1

#Example:
arr = [1, 2, 3, 5, 8, 9, 11, 12, 13, 15, 17, 20, 21]
target = 8
result = binary_search(arr, target)
if result == -1:
    print("Value",target,"not found")
else:
    print("Value",target,"found at",result)