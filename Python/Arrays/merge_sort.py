'''
How Merge Sort works:
    1. Divide unsorted array into two sub-arrays
    2. Continue to divide into two sub arrays so long as the current piece of the array has more than one element
    3. Merge two sub arrays together by putting the lowest value first
    4. Keep merging until there are no more sub-arrays left

Time Complexity: O(n log n)
Space Complexity: O(n)
'''

#Merge function
def merge(arr, left, mid, right):
    subArr1 = mid - left + 1
    subArr2 = right - mid

    #Create temp arrays
    leftArr = [0] * subArr1
    rightArr = [0] * subArr2

    #Copy data into temp arrays 
    for i in range(subArr1):
        leftArr[i] = arr[left + i]

    for j in range(subArr2):
        rightArr[j] = arr[mid + 1]

    #Initialize indicies of sub arrays
    idxOfSubArr1 = 0
    idxOfSubArr2 = 0
    idxOfMergedArr = left

    #Merge temp arrays back into array
    while idxOfSubArr1 < subArr1 and idxOfSubArr2 < subArr2:
        if leftArr[idxOfSubArr1] <= rightArr[idxOfSubArr2] :
            arr[idxOfMergedArr] = leftArr[idxOfSubArr1]
            idxOfSubArr1 += 1
        else:
            arr[idxOfMergedArr] = rightArr[idxOfSubArr2]
            idxOfSubArr2 += 1
        idxOfMergedArr += 1

    #Copy remaining elements of left array, if any
    while idxOfSubArr1 < subArr1:
        arr[idxOfMergedArr] = leftArr[idxOfSubArr1]
        idxOfSubArr1 += 1
        idxOfMergedArr += 1

    #Copy remaining elements of right array, if any
    while idxOfSubArr2 < subArr2:
        arr[idxOfMergedArr] = rightArr[idxOfSubArr2]
        idxOfSubArr2 += 1
        idxOfMergedArr += 1

#Merge Sort function 
def merge_sort(arr, begin, end):
    if begin >= end:
        return
    
    mid = begin + (end - begin) // 2
    merge_sort(arr, begin, mid)
    merge_sort(arr, mid + 1, end)
    merge(arr, begin, mid, end)


#Example:
arr = [12, 11, 10, 55, 69, 2, 3, 39, 41]
arr_size = len(arr)
print("Array before Merge Sort:",arr)
merge_sort(arr, 0, arr_size - 1)
print("Array after Merge Sort:",arr)