def Four_sum(nums, target):
    i = 0; each_comb_list = []
    while i <= len(nums)-3:
        for j in range(1,len(nums)-(i+1)):
            for m in range(i+j+1,len(nums)-1):
                for k in nums[m+1:]:
                    each_comb_list.append([nums[i],nums[i+j],nums[m],k])
        i += 1
    output = []
    for i in each_comb_list:
        i.sort()
        if sum(i) == target and i not in output:
            output.append(i)
    return output

print(Four_sum([1,0,-1,0,-2,2],0))
print(Four_sum([2,2,2,2,2],8))