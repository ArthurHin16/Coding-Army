"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order

strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

SOLUTION
ord() is a built in function that returns the Unicode code point of a Unicode character.
Time Complexity O(n)
Space Complexity O(n)
"""
from collections import defaultdict
def groupAnagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        ans = [0] * 26 
        for c in s:
            ans[ord(c) - ord('a')] += 1 # Value used as an index into an array to access the element. 
        groups[tuple(ans)].append(s)
    return groups.values()
        


strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
