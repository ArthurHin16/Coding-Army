"""
You are given an 'm x n' integer matrix with the following two properties:
    - Each row is sorted in non-decreasing order.
    - The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise. 
"""
def searchMatrix(matrix, target):
    ROWS = len(matrix)
    COLS = len(matrix[0])
    top = 0
    bottom = ROWS - 1
    while top <= bottom:
        row = (top + bottom)//2
        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bottom = row - 1
        else:
            break
    
    if not(top <= bottom):
        return False
    
    row = (top + bottom)//2
    low = 0
    high = COLS - 1
    while low <= high:
        midd = (low + high)//2
        if matrix[row][midd] == target:
            return True
        elif matrix[row][midd] > target:
            high -= 1
        else:
            low += 1
    return False
    
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 61
print(searchMatrix(matrix, target))
#The general time complexity is O(log n * m) and the space complexity is O(1)