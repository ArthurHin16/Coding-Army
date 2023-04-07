"""
Given an integer array nums, return true if any of the value appears at least twice in the array, and 
return false if every element is distinct.

SOLUTION
A set is an unordered collection of unique elements. Each element can only appear once in the set. 
my_set = {1,2,3} or my_set = set()
my_set.add(4) => Adding a new element in the set
my_set.remove(4) => Removing an element from the set

"""
def containsDuplicate(nums):
    numbers = set()
    for num in nums:
        if num not in numbers:
            numbers.add(num)
        else:
            return True
    return False


nums = [1,2,3,4]
print(containsDuplicate(nums))