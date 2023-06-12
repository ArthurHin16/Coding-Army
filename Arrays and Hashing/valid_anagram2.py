def isAnagram(s, t):
    if len(s) != len(t):
        return False
    incidences = {}
    for char in s:
        if char not in incidences:
            incidences[char] = 1
        else:
            incidences[char] += 1
    for char in t:
        if char in incidences:
            incidences[char] -= 1
    for e in incidences:
        if incidences[e] != 0:
            return False
    return True            

s = "anagram"
t = "nagaram"
print(isAnagram(s,t))