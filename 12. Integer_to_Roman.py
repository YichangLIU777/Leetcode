import pandas as pd
def Integer_to_Roman(num):
    global roman
    roman = pd.DataFrame({"Symbol":["I","V","X","L","C","D","M"],\
        "Value":[1,5,10,50,100,500,1000]})
    num_list = [i for i in str(num)]; digits = [1000,100,10,1]
    add_list = []
    for i in range(len(num_list)):
        add_list.append(int(num_list[-(i+1)])*digits[-(i+1)])
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
        "Value":value_list})
    Symbol_list_output = []
    for i in add_list:
        Symbol_list_output.append(list(roman[roman["Value"]==i].Symbol)[0])
    output = ''
    for i in range(len(Symbol_list_output)):
        output += Symbol_list_output[-(i+1)]
    return output
print(Integer_to_Roman(1994))
print(Integer_to_Roman(58))
print(Integer_to_Roman(9))
print(Integer_to_Roman(4))