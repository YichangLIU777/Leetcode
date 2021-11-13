def Three_sum_Closest(nums, target = 0):
    i = 0; each_comb_list = []
    while i <= len(nums)-2:
        for j in range(1,len(nums)-(i+1)):
            for k in nums[i+j+1:]:
                each_comb_list.append([nums[i],nums[i+j],k])
        i += 1
    sum_list = []
    for i in each_comb_list:
        i.sort()
        sum_list.append(sum(i))
    difference_list = [abs(i-target) for i in sum_list]
    output = sum_list[difference_list.index(min(difference_list))]
    return output

print(Three_sum_Closest([-1,2,1,-4],1))
print(Three_sum_Closest([0,0,0],1))