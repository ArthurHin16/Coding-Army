"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

SOLUTION
We use the lower() built in method to transform all the 'UPPER CASE' letters into 'lower case'.
We use the isalnum() to check if the character is alphanumeric (just letters and numbers).
"""
def isPalindrome(s):
    s = s.lower()
    palindrome = ''
    for c in s:
        if c.isalnum():
            palindrome += c
    
    #Definition of the two pinters technique in order to compare if the string is a palindrome
    l = 0
    r = len(palindrome) - 1
    while l <= r: 
        if palindrome[l] == palindrome[r]:
            l += 1
            r -= 1
        else:
            return False
    return True
s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))