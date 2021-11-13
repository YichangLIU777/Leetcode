
def reverse_integer(x):
    if -(2**(31)) <= x <= (2**(31)):
        num_list = [i for i in str(x)]
        pure_num_list = [[i for i in num_list[1:]] if num_list[0] == "-" else [i for i in num_list]][0]
        reverse_list = [pure_num_list[-(i+1)] for i in range(len(pure_num_list))]
        z = 0
        while reverse_list[z] == 0:
            reverse_list = reverse_list[z+1:]
            z += 1
        total = ''
        for i in reverse_list:
            total += i
        return [int(total) if num_list[0]!="-" else -int(total)][0]
    else: 
        return 0

print(reverse_integer(123))
print(reverse_integer(-123000))


# Input: x = -123
# Output: -321