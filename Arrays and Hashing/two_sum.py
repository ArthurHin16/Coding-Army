"""
Given any array of integers nums and an integer target, return indices of the two numbers such that they
add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""
def twoSum(nums, target):
    difference = {} # value -> index
    for i in range(len(nums)):
        ans = target - nums[i]
        if ans in difference:
            return[difference[ans], i]
        difference[nums[i]] = i


nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))