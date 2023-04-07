"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise. 
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once. 

SOLUTION:

In Pyhton, we can compare two dictionaries using the == operator. This operator compares the key - value 
pairs of the two dictionaries and returns `True` if they are equal, and `False` otherwise. 
Note that the order of the key -  value pairs does not matter comparing dictionaries. 

get(key, default_value) key is the value to look up in the dictionary and the second one is the default
value to return if key is not found in the dictionary. 
"""
def isAnagram(s,t):
    if len(s) != len(t):
        return False
    
    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    return countS == countT

s = "anagram"
t = "nagaram"
print(isAnagram(s,t))
