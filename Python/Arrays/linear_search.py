'''
How Linear Search works:
    1. Iterate through array
    2. Compare each value to check if it is equal to the desired value
    3. If value is found, return index of value
    4. If value is not found by the end of the array, return -1 to indicate value was not found


Time Complexity: O(n)
Space Complexity: O(1)
'''

#Linear Search function
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

#Example:
arr = [1, 5 , 32, 56, 99, 69, 6, 50, 0, 45, 78, 8, 2, 4]
target = 32
result = linear_search(arr, target)
if result == -1:
    print("Value", target,"not found")
else:
    print("Value",target,"found at",result)