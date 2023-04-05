'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write function
to search target in nums. If tarfet exists, then return its index. Otherwise, return -1
'''

def binarySearch(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        midd = (high + low)//2
        if nums[midd] == target:
            return midd
        elif nums[midd] > target:
            high -= 1
        else:
            low += 1
    return -1

nums = [-1,0,3,5,9,12]
target = 9
print(binarySearch(nums, target))
#The general time complexity is O(log n) and the space complexity is O(1)