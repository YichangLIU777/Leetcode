def Valid_Parentheses(s):
    s_list = ["()","[]", "{}"]
    if len(s)%2 == 1:
        output = False
    else: 
        True_list = []
        for i in range(int(len(s)/2)):
            if s[i]+s[-(i+1)] in s_list:
                True_list.append(True)
            else:
                True_list.append(False)
        if False not in True_list:
            output = True
        else:
            True_list_1 = []
            for j in range(0,len(s),2):
                if s[j:j+2] in s_list:
                    True_list_1.append(True)
                else:
                    True_list_1.append(False)
            if False not in True_list_1:
                output = True
            else:
                output = False
    return output
print(Valid_Parentheses("()[]{}"))
print(Valid_Parentheses("([])"))
print(Valid_Parentheses("[(])"))
     


