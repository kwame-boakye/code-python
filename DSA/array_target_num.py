nums = [9, 4, 5, 0, 45, 67, 3, 1, 8, 7]
target_num = 11
output = []
seen = {}


# Iterate through the nums list to find two indices whose values sum to target_num 
#using a hashmap for efficient lookup
for i, num in enumerate(nums):
    complement = target_num - num
    if complement in seen:
        output = [seen[complement], i]
        break
    seen[num] = i



print(output)
#print(seen)


        
