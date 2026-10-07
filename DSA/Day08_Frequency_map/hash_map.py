#Store the Frquency in Dictionary 
nums = [1,3,5,5,6,7,2,3,1,8,3,2,1]

hash_map = {}
n = len(nums)

for i in range (0,n):
    hash_map[nums[i]] = hash_map.get(nums[i],0) + 1
    #In the process there are one line perform 
    #ex :- hash_map[num[i]] = index 0 = 1 
    #hash_map.get(nums[i],0) = index 0 is present in hash_map if no then 0 is output 
    # 0 + 1 = 1 put in the dictionary

print(hash_map)
#output :- {1: 3, 3: 3, 5: 2, 6: 1, 7: 1, 2: 2, 8: 1} 

