import pandas as pd

def Zigzag_Conversion(string, num_rows):
    if num_rows!= 1:
        iterate = num_rows + (num_rows-2)
        string_list = [i for i in string]
        last_list_num = len(string_list)%iterate
        class_list = []
        for i in range(0,len(string_list)-last_list_num,iterate):
            each_string_list = string_list[i:i+iterate]
            for j in range(len(each_string_list)-(num_rows-2)):
                class_list.append(j)
            for j in range(num_rows-2):
                class_list.append(num_rows-j-2)
        for i in range(last_list_num):
            class_list.append(i)
        class_df = pd.DataFrame({"index": class_list, "string": string_list})
        class_df = class_df.sort_values("index")
        output_list = class_df['string'].tolist()
        output = ''
        for i in output_list:
            output += i
    else:
        output = string
    return output

string = "PAYPALISHIRING"
num_rows = 4
print(Zigzag_Conversion(string, num_rows))
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"