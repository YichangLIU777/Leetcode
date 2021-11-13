import pandas as pd
def get_roman_table():
    roman = pd.DataFrame({"Symbol":["I","V","X","L","C","D","M"],\
        "Value":[1,5,10,50,100,500,1000]})
    value_list = []; symbol_list = []
    value_list = [i for i in range(1,10,1)]+\
        [i for i in range(10,100,10)]+\
            [i for i in range(100,1000,100)]+\
                [i for i in range(1000,4000,1000)]
    for i in value_list:
        try:
            m = len([k for k in str(i)])
            if i < 4*(10**(m-1)):
                each = ''
                for j in range(int(i/(10**(m-1)))):
                    each += roman["Symbol"].tolist()[(m-1)*2]
                symbol_list.append(each)
            elif i == 4*(10**(m-1)):
                each = roman["Symbol"].tolist()[(m-1)*2]+roman["Symbol"].tolist()[(m-1)*2+1]
                symbol_list.append(each)
            elif 4*(10**(m-1))<i<=8*(10**(m-1)):
                each = ''
                for h in range(int((i-5*(10**(m-1)))/(10**(m-1)))):
                    each += roman["Symbol"].tolist()[(m-1)*2]
                each = roman["Symbol"].tolist()[(m-1)*2+1]+each
                symbol_list.append(each)
            else:
                each = roman["Symbol"].tolist()[(m-1)*2]+roman["Symbol"].tolist()[m*2]
                symbol_list.append(each)
        except:
            pass
    roman = pd.DataFrame({"Symbol":symbol_list,\
        "Value":value_list, "Order": [i for i in range(len(value_list))]})
    return roman



def Split_Roman(s):
    s_list = [i for i in s]
    each_list = []; i = 0
    while i < len(s_list)-1:
        if list(get_roman_table()[get_roman_table().Symbol == s_list[i+1]].Order)[0] > list(get_roman_table()[get_roman_table().Symbol == s_list[i]].Order)[0]:
            each_list.append(s_list[i]+s_list[i+1])
            i += 2
        else:
            each_list.append(s_list[i])
            i += 1
    if s[-1] == s[-2]:
        each_list.append(s[-1])
    return each_list

s = Split_Roman("MCMXCIV")
output = 0
for i in s:
    output += list(get_roman_table()[get_roman_table().Symbol == i].Value)[0]
print(output)
