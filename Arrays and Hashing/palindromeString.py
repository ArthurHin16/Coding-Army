def isPalindrome(s: str):
    """
        Space complexity = O(n) Time Complexity = O(n) 
        s = "A man, a plan, a canal: Panama"
        STEPS:
        1. Transfor all letters into lower case s = "a man, a plan, a canal: panama"
        2. Create another string and save only the letters isalpha() s = "amanaplanacanalpanama"
        3. Use two pointers one at the beginning and one at the end, chek if they are the same, if not return True
        4. After checking the condition in the loop, return True
    """
    s = s.lower()
    new_string = ""
    for c in s:
        if c.isalpha():
            new_string = new_string + c
    print(new_string)
    l, r = 0, len(new_string) - 1
    while l <= r:
        if new_string[l] != new_string[r]:
            return False
        l += 1
        r -= 1
    return True
s = "0P"
print(isPalindrome(s))