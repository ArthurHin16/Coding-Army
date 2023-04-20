"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
"""
def threeSum(nums):
    nums.sort()
    result = []
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < 0 - nums[i]:
                left += 1
            elif nums[left] + nums[right] > 0 - nums[i]:
                right -= 1
            else:
                result.append([nums[i],nums[left],nums[right]])
                left += 1
                right -= 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
    return result


nums = [0,0,0] #[-4,-1,-1,0,1,2]
print(threeSum(nums))