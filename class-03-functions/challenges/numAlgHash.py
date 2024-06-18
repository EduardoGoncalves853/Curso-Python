# Fórmula
#* n => td => d1
#* a => a * x = ax
#* d = d1 + ax

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

