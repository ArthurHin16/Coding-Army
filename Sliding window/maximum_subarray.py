"""
Given an integer array 'nums', find the subarray with the largest sum, and
return its sum.

SOLUTION:
It is not important to keep track of the sum that is lower than 0, for that reason we set the sum to 0 and continue
with the new value contained in the array, because we want to know the subarray and that item can be of just one element.
"""
def maxSubArray(nums):
    maxSum = nums[0]
    currSum = 0
    for n in nums:
        if currSum < 0:
            currSum = 0
        currSum += n
        maxSum = max(currSum, maxSum)  
    return maxSum
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))