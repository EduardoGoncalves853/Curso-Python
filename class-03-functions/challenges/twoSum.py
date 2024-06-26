
# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# You can return the answer in any order.

def twoSum(array,target):
    hashmap = {}
    for i, num in enumerate(array):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = 1
    return None
    

array = [1,7,5,2,9,6,3]
target = 6
print(twoSum(array, target))


