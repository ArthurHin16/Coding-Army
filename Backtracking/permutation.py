"""
The code below is an example of finding all of the possible arrangements of a given set of letters
"""
def permutation(list, res):
    if list == 1:
        return res
    else:
        return [
            y + x #This line concatenates the two values
            for y in permutation(1, res)
            for x in permutation(list - 1, res)
        ]
print(permutation(1, ["a","b","c"]))
print(permutation(5, ["a","b","c"]))