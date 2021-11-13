def Merge_Two_Sorted_Lists(l1, l2):
    l_t = l1+l2
    l_t.sort()
    return l_t

print(Merge_Two_Sorted_Lists([1,2,4], [1,3,4]))
print(Merge_Two_Sorted_Lists([], [0]))
print(Merge_Two_Sorted_Lists([], []))
print(Merge_Two_Sorted_Lists([1,1,2,3,4,4], [0]))