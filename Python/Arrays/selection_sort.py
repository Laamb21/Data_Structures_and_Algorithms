'''
How Selection Sort works:
    1. Go through the array to find the lowest value 
    2. Move the lowest value to the front of the unsorted part of the array
    3. Go through the array again as many times as ther are values in the array 

Time Complexity:
Space Complexity: 
'''

#Selection Sort function
def selection_sort(arr, n = None):
    #If n is not provided, set n to length of array
    if n is None:
        n = len(arr)
    
    #Base case: if array has one or zero elements, return array
    if n <= 1:
        return
    
    #One pass of selection sort: swap min value with first element of array
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

#Example:
arr = [64, 25, 12, 22, 11]
print("Array before Selection Sort: ", arr)
selection_sort(arr)
print("Array after Selection Sort: ", arr)