'''
How Counting Sort works:
    1. Create a new array for counting how many elements there are of different values
    2. Traverse unsorted array
    3. For each value, count it by increasing the counting array at the corresponding index
    4. After counting the values, traverse the counting array and create a sorted array
    5. For each count in the counting array, create the correct number of elements, with values that correspond to the counting array index

Time Complexity: O(n+m)
Space Complexity: O(n+m)
'''

#Counting sort function
def counting_sort(arr):
    #Find the maximum element of an array
    m = max(arr)

    #Initialize count array with 0
    count_arr = [0] * (m + 1)

    #Map each element of array as index of count array
    for i in arr:
        count_arr[i] += 1

    #Calculate prefix sum at every index of count array
    for i in range(1, m + 1):
        count_arr[i] += count_arr[i - 1]

    #Create resulting array
    result = [0] * len(arr)
    for i in range(len(arr)):
        result[count_arr[arr[i]] - 1] = arr[i]
        count_arr[arr[i]] -= 1
    
    return result

#Example:
arr = [4, 3, 12, 1, 5, 6, 3, 9]
print("Array before Counting Sort:", arr)
result = counting_sort(arr)
print("Array after Counting Sort:",result)