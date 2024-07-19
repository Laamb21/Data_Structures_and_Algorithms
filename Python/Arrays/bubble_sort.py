'''
How Bubble Sort works:
    1. Go through the array one element at a time
    2. For each value, compare the value with the next value
    3. If the value is higher tham the next one, swap the values so that the hightest value comes last
    4. Repeat until array has beem sorted

Time Complexity: 
    Best Case - O(n)
    Average or Worst case - O(n^2)
Space Complexity: 
    Worst Case - O(1)
'''

#Bubble Sort function
def bubble_sort(arr, n = None):
    #If n is not provided, set n to length of array
    if n is None:
        n = len(arr)

    #Base case: if array has one or zero elements, return array
    if n <= 1:
        return
    
    #One pass of bubble sort; largest element moved to end of array
    for i in range(n - 1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    
    #Largest element fixed, recrusive call for remaining elements
    bubble_sort(arr, n-1)

#Example:
arr = [64, 34, 25, 12, 22, 11, 90]
print("Array before Bubble Sort: ", arr)
bubble_sort(arr)
print("Array after Bubble Sort: ", arr)
