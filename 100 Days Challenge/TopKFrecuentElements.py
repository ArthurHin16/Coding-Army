def top_k_frecuents_elements(nums, k):
    count = {}
    bucket = [[] for i in range(len(nums) + 1)]
    for num in nums:
        count[num] = 1 + count.get(num, 0)
    for n, c in count.items():
        bucket[c].append(n)
    result = []
    for i in range(len(bucket) - 1, 0, -1):
        for n in bucket[i]:
            result.append(n)
            if len(result) == k:
                return result

nums = [1,1,1,2,2,3]
k = 2
print(top_k_frecuents_elements(nums, k))