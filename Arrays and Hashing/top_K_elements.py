"""
Given an integer array 'nums' and an integer 'k', return the 'k' most frequent elements. You may return the answer in any order

SOLUTION
Bucket Sort is a sorting algorithm that divides the unsorted array elements into several group called buckets. Each bucket is then
sorted by using any of the suitable sorting algorithms.

The items() method is a built-in function for dictionaries that returns a view object consisting of a list of (key - value) tuples.
"""

def topKFrequent(nums, k):
    count = {} # DS to keep track of the number of times that a number appeared in the array
    freq = [[] for i in range(len(nums))] # We built an array called freq in order to create the Bucket Sort, is is created in the List Comprehension Syntax
    for i in nums:
        count[i] = 1 + count.get(i, 0) #Verify if the number exists in the 'count' hashmap, if does increment the count, if not added it
    for n, c in count.items(): #Iteration by using the tuple containing the key - value pairs
        freq[c].append(n) #In the index with the number of apperances append the number
    res = []
    for i in range(len(freq)-1, 0,-1): #Backwards loop in order to add the most frequent elements in the result array. 
        for n in freq[i]:
            res.append(n)
            if len(res) == k: #When the length of the array is equal to 'K' return the array with the values. 
                print(len(res))
                return res

nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums,k))