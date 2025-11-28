# Frequency Map / Dictionary

nums = [1,2,3,4,56,6,7,4,4,24,2,3,3,4,4,4,456,34,636,24]
freq_map = dict() # or {}

for i in range(0,len(nums)):
    if(nums[i] in freq_map):
        freq_map[nums[i]] += 1
    else:
        freq_map[nums[i]] = 1

print(freq_map)