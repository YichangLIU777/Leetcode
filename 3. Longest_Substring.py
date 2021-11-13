def Longest_Substring_Without_Repeating_Characters(s):
    substring_list = []
    for i in range(len(s)):
        j = 0
        while j < (len(s)-i):
            each = s[i]
            each += s[i+1:i+j+1]
            j = j+1
            substring_list.append(each)
    without_dup = []
    for i in substring_list:
        each_single = [k for k in i]
        if len(each_single) == len(set(each_single)):
            without_dup.append(len(i))
    return max(without_dup)

s = "abcabcbb"
print(Longest_Substring_Without_Repeating_Characters(s))
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.