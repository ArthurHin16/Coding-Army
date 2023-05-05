def search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        midd = (l + r) // 2
        if target == nums[midd]:
            return midd
        #left sorted function
        if nums[l] <= nums[midd]:
            if target > nums[midd] or target < nums[l]:
                l =  midd + 1
            else:
                r = midd - 1
        #right sorted portion
        else:
            if target < nums[midd] or target > nums[r]:
                r = midd - 1
            else:
                l = midd + 1
    return -1

nums = [4,5,6,7,0,1,2]
target = 0
print(search(nums, target))