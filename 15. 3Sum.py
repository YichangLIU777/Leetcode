def Three_sum(nums, target = 0):
    i = 0; each_comb_list = []
    while i <= len(nums)-2:
        for j in range(1,len(nums)-(i+1)):
            for k in nums[i+j+1:]:
                each_comb_list.append([nums[i],nums[i+j],k])
        i += 1
    output = []
    for i in each_comb_list:
        i.sort()
        if sum(i) == target and i not in output:
            output.append(i)
    return output

print(Three_sum([-1,0,1,2,-1,-4]))
print(Three_sum([0]))
print(Three_sum([]))





# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]