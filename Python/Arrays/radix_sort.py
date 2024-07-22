'''
How Radix Sort works:
    1. Start with the right most element in an array
    2. Sort the values based on the digit in focus by first putting the values in the correct bucket based on the digit in focus, 
        and then put them back into array in the correct order
    3. Move to the next digit, and sort again until there are no digits remaining

Time Complexity: O(d * (n + k))
Space Complexity: O(n + k)
'''

#Counting Sort function according to digit(represent by exp)
def counting_sort(arr, exp1):
    n = len(arr)

    #The result array elements will have the sorted array
    result = [0] * (n)

    #Initialize count array
    count = [0] * (10)

    #Store count of occurances in count array
    for i in range(0, n):
        idx = arr[i] // exp1
        count[idx % 10] += 1

    #Change count[i] so that count[i] now contains actual position of digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    #Build output array
    i = n - 1
    while i >= 0:
        idx = arr[i] // exp1
        result[count[idx % 10] - 1] = arr[i]
        count[idx % 10] -= 1
        i -= 1

    #Copy the resulting array to the original array, that way arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = result[i]


#Radix Sort function
def radix_sort(arr):
    #Find max num in array
    max1 = max(arr)

    #Do counting sort for each digit 
    #NOTE: instead of passing a digit, exp is passed, which is 10^i where i is the current digit number
    exp = 1
    while max1 / exp >= 1:
        counting_sort(arr, exp)
        exp *= 10



#Example:                     
arr = [178, 34, 76, 98, 800, 45, 5, 66]
print("Array before Radix Sort:",arr)
radix_sort(arr)
print("Array after Radix Sort:",arr)