'''
The following code demonstrates different time and space complexities 
'''
#Function that squares each element in an array
def squares(arr):
    n = len(arr)                        #Define length of array
    for i in range(n):                  #Iterate through array
        arr[i] = arr[i] * arr[i]        #Multiply each element by itself
    return arr

#Function that gives uniques pairs of all elements in an array
def unique_pairs(arr):
    pairs = []                                  #Initialize array for pairs 
    n = len(arr)                                #Define length of array
    for i in range(n):                          #Iterate through array
        for j in range(i + 1, n):               #Iterate through next element in array
            pairs.append((arr[i], arr[j]))      #Add pairs to new array
    return pairs                                #Retrun new array


#The following array will be used to demonstrate different time and space complexities
arr = [1, 2, 3, 4, 5]
print("Array:", arr)


#Returning an element of the array at a given index
#Time Complexity: O(1)
print("Element at index 0:", arr[0])


#Squaring all elements in an array (using function above)
#Time Complexity: O(n)
#Space Complexity: O(1)
print("Elements squared:", squares(arr))


#Redefine array after function call
arr = [1, 2, 3, 4, 5]

#Create unique pairs of all elements in an array (using function above)
#Time Complexity: O(n^2)
#Space Complexity: O(n^2)
print("Unique pairs:", unique_pairs(arr))