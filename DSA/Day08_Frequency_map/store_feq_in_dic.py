#Store the Frquency in Dictionary 
nums = [1,3,5,5,6,7,2,3,1,8,3,2,1]
frq_map = {}

for i in range(0,len(nums)):
    if nums[i] in frq_map:
        frq_map[nums[i]]+=1 
    else:
        frq_map[nums[i]] = 1

print(frq_map)
'''output
{1: 3, 3: 3, 5: 2, 6: 1, 7: 1, 2: 2, 8: 1}
'''