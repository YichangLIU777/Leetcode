def Median_of_Two_Sorted_Arrays(list1, list2):
    list_total = list1 + list2
    sorted(list_total)
    if len(list_total)%2 == 1:
        median = list_total[int(len(list_total)/2)+1]
    else: 
        median = (list_total[int(len(list_total)/2)-1]+list_total[int(len(list_total)/2)])/2
    return median

print(Median_of_Two_Sorted_Arrays([1,3], [2]))
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.






