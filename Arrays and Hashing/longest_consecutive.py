"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

SOLUTION
This is another solution for the same problem, but instead we are going to have a O(n) run time complexity.
Overall, the nested while loop is executed at most n times, and each iteration
takes O(1) time, so the time complexity of the function is O(n).
"""
def longestConsecutive(nums):
    numSet = set(nums)
    longest = 0
    for n in nums:
        if (n - 1) not in numSet:
            length = 1
            while (n + length) in numSet:
                length += 1
            longest = max(length, longest)
    return longest

nums = [7,6,5]
print(longestConsecutive(nums))