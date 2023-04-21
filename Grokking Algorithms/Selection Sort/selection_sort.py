"""
Selection sort is a simple and efficient sorting algorithm that works by repeatedly selecting 
the smallest (or largest) element from the unsorted portion of the list and moving it to the sorted portion of the list.
Overall complexity = O(N) * O(N) = O(N*N) = O(N^2)
"""
def findSmallest(arr):
    smallest = arr[0] #Stores the smallest value
    smallest_index = 0 #Stores the index of the smallest value
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArray = []
    for i in range(len(arr)):
        smallest = findSmallest(arr) #Finds the smallest element in the array, and adds it to the new array.
        newArray.append(arr.pop(smallest))
    return newArray

arr = [156, 141, 35, 94, 88, 61, 111]
print(selectionSort(arr))