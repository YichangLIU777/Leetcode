def String_to_Intege(s):
    s = [i for i in s if i != " "]
    first = ['-','1','2','3','4','5','6','7','8','9','0']
    if s[0] in first:
        num_list = []
        for i in s:
            try:
                if i == "-":
                    num_list.append(i)
                num_list.append(str(int(i)))
            except:
                pass
        output = ''
        for i in num_list:
            output += i
        if int(output) <= -2**31:
            output = -2**31
        elif int(output) >= 2**31-1:
            output = 2**31-1
    else: 
        output = 0
    return int(output)

print(String_to_Intege("-4193 with words"))

















































