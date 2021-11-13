def judge_Palindromic(string):
    result_list = []
    string = [i for i in string]
    for i in range(int(len(string)/2)):
        if string[i] == string[-(i+1)]:
            result_list.append(True)
        else: 
            result_list.append(False)
    if False in result_list:
        return False
    else:
        return True

def Longest_Palindromic_Substring(s):
    substring_list = []
    for i in range(len(s)):
        j = 0
        while j < (len(s)-i):
            each = s[i]
            each += s[i+1:i+j+1]
            j = j+1
            substring_list.append(each)
    judge_pal_list = []
    for i in substring_list:
        if judge_Palindromic(i) == True:
            judge_pal_list.append(i)
        judge_len_pal_list = [len(i) for i in judge_pal_list]
        index = judge_len_pal_list.index(max(judge_len_pal_list))
        output = judge_pal_list[index]
    return output

print(Longest_Palindromic_Substring("babad"))

    







# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.