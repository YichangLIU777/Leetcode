def add_two_number(l1,l2):
    num_list = [];num_1 = ''; num_2 = ''
    total_1 = [str(i) for i in l1]; total_2 = [str(i) for i in l2]
    for i in total_1:
        num_1 += i
    for i in total_2:
        num_2 += i
    num_1 = int(num_1); num_2 = int(num_2); num = num_1+num_2; num = str(num); new_num_list = []
    for i in num:
        num_list.append(int(i))
    for i in range(1,len(num_list)+1):
        new_num_list.append(num_list[-i])
    return new_num_list

l1 = [2,4,3];l2 = [5,6,4]
print(add_two_number(l1,l2))

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.