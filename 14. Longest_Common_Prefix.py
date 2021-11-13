def intersection(list_1, list_2, list_3):
    lst3 = [value for value in list_1 if value in list_2 if value in list_3]
    return lst3
def Longest_Common_Prefix(strs):
    total_substring = []
    for k in strs:
        list_substring = []
        for i in range(len(k)):
            j = 0
            while j < (len(k)-i):
                each = k[i]
                each += k[i+1:i+j+1]
                j = j+1
                list_substring.append(each)
        total_substring.append(list_substring)
    output = intersection(total_substring[0], total_substring[1], total_substring[2])
    output_length = [len(i) for i in output]
    try:
        if max(output_length) != " ":
            return output[output_length.index(max(output_length))]
    except:
        return " "

print(Longest_Common_Prefix(["flower","flow","flight"]))
print(Longest_Common_Prefix(["dog","racecar","car"]))
# Input: strs = ["flower","flow","flight"]
# Output: "fl"


