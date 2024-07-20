'''
How Quick Sort works:
    1. Choose a value in the array to be the pivot element 
    2. Order the rest of the array so that the lower values than the pivot element are on the left, and the higher values are on the right.
    3. Swap the pivot element with the first element of the higher values so that the pivot element lands in between the lower and higher values
    4. Do the same operation recursively for the sub-arrays on the left and right side of the pivot element 

Time Complexity: O(n^2)
Space Complexity: O(1)
'''

#Partition function
def partition(arr, low, high):
    #Set right most element as pivot
    pivot = arr[high]
    
    #Pointer for greater element 
    i = low - 1

    #Traverse through array, compare each element with pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            #If element is smaller than pivot, swap with pointer i
            i = i + 1
            
            #Swap element at i with element at j
            arr[i], arr[j] = arr[j], arr[i]

    #Swap pivot element with pointer
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    #Return position from where partition is done
    return i + 1


#Quick Sort function
def quick_sort(arr, low, high):
    if low < high:
        #Find pivot element where smaller elements are on the left and greater elements are on the right
        pivot = partition(arr, low, high)

        #Recursive call for left of pivot
        quick_sort(arr, low, pivot-1)

        #Recursive call for right of pivot
        quick_sort(arr, pivot + 1, high)


#Example:
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
print("Array before Quick Sort:", arr)
quick_sort(arr, 0, n - 1)
print("Array after Quick Sort:",arr)