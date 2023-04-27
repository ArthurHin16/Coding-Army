import math
def minEatingSpeed(piles,h):
    l,r = 1, max(piles)
    res = max(piles)
    while l <= r:
        k = (l + r) // 2
        totalTime = 0
        for p in piles:
            totalTime += math.ceil(p/k)
        if totalTime <= h:
            res = min(res, k)
            r = k - 1
        else: 
            l = k + 1
    return res
piles = [3,6,7,11]
h = 8
print(minEatingSpeed(piles, h))
