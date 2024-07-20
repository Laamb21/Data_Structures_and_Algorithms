'''
How Insertion Sort works:
    1. Take the first value from the unsorted part of the array
    2. Move the value into the correct place in the sorted part of the array
    3. Go through the unsorted part of the array again as many times as there are values

Time Complexity: O(n^2)
Space Complexity: O(1)
'''

#Insertion Sort function
def insertion_sort(arr):
    #Traverse through 1-len(arr)
    for i in range(len(arr)):
        key = arr[i]
        j = i-1
        #Move elements of arr[0...i-1] that are greater than key to one index ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

#Example:
arr = [12, 11, 13, 5, 6]
print("Array before Insertion Sort:",arr)
insertion_sort(arr)
print("Array after Insertion Sort:",arr)