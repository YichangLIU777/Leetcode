def twoSum(nums, target):
    two_sum_list = []
    index_list = []
    for i in range(len(nums)):
        a = 1
        while a < len(nums)-i:
            two_sum = nums[i]+nums[i+a]
            index_list.append([i,i+a])
            a = a+1
            two_sum_list.append(two_sum)
    for i in two_sum_list:
        if i == target:
            output = index_list[two_sum_list.index(i)]
    return output
print(twoSum(nums = [2,7,11,15], target = 9))
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].