"""
Given a string s, find the length of the longest substring without repeating characters.
To solve this problem we are going to use the sliding window technique.

SOLUTION:
The sliding window technique is a commonly used algorithmic technique for solving problems
related to arrays or strings. It works by maintaining a "window" of elements in the array
or string and sliding the window over the array or string to find the desired solution.

The sliding window technique can be used to solve a wide range of problems, usch as finding
the maximum sum of a subarray of size 'k', finding the longest substring without repeating characters,
or finding the smallest subsarray with a sum greater than or equal to a given value. 
"""
def lengthOfLongestSubstring(s):
    longest = set()
    l = 0
    res = 0
    for r in range(len(s)):
        while s[r] in longest: 
            longest.remove(s[l]) 
            l += 1
        longest.add(s[r])
        res = max(res, r-l+1)
    return res

s = "abcabcbb"
print(lengthOfLongestSubstring(s))
