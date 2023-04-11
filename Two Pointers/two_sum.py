"""
Given a 1-indexed array of integers 'numbers' that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number. 
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
"""
#SOLUTION 1:
#The following solution takes Extra Space Memory O(n), and the Time Complexity is O(n)
def twoSum(numbers, target):
    hashmap = {}
    for i in range(len(numbers)):
        if numbers[i] in hashmap:
            return [hashmap[numbers[i]] + 1,i + 1]
        res = target - numbers[i]
        hashmap[res] = i

#Solution 2:
#Constant extra space
def twoSumConstant(numbers, target):
    l, r = 0, len(numbers) - 1
    while l < r:
        currSum = numbers[l] + numbers[r]
        if currSum > target:
            r -= 1
        elif currSum > target:
            l += 1
        else:
            return [l + 1, r + 1]


numbers = [2,7,11,15]
target = 9
print('Solution 1:',twoSum(numbers,target))
print('Solution 2:', twoSumConstant(numbers, target))