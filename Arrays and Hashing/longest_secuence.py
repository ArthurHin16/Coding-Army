"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

SOLUTION
In first instance we are going to use extra space in order to keep track of the ordered numbers.
The time complexity of the algorithm is O(n log n) in worst case and O(n) in best case scenario
"""
def longestConsecutive(nums):
    longSeq = 0
    if len(nums) == 0:
        return longSeq
    ord_nums = sorted(list(set(nums)))
    nxt = ord_nums[0] + 1
    longest = 1
    for i in range(1,len(ord_nums)):
        if ord_nums[i] == nxt:
            longest += 1
            nxt += 1
        else:
            longSeq = max(longest,longSeq)
            longest = 1
            nxt = ord_nums[i] + 1
    longSeq = max(longest,longSeq)
    return longSeq
nums = [100,4,200,1,3,2,201,202,203,204,500]
print(longestConsecutive(nums))