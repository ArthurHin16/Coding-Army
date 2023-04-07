"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order

SOLUTION
ord() is a built in function that returns the Unicode code point of a Unicode character.
"""
from collections import defaultdict
def groupAnagrams(strs):
    ans = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1 # Value used as an index into an array to access the element. 
        ans[tuple(count)].append(s)
    return ans.values()

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
#Output: [["bat"],["nat","tan"],["ate","eat","tea"]]