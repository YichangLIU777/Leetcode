letter_num_dict = {2:["a","b","c"],
    3:["d","e","f"],
    4:["g","h","i"],
    5:["j","k","l"],
    6:["m","n","o"],
    7:["p","q","r","s"],
    8:["t","u","v"],
    9:["w","x","y","z"]}

def Letter_Combinations_of_a_Phone_Number(digits):
    digits_list = [i for i in digits]; count = 0
    each_list = []
    try:
        for i in letter_num_dict[int(digits_list[0])]:
            each = i
            each_list.append(each)
            try: 
                for k in letter_num_dict[int(digits_list[1])]:
                    each = i+k
                    each_list.append(each)
                    try:
                        for m in letter_num_dict[int(digits_list[2])]:
                            each = i+k+m
                            each_list.append(each)
                            try:
                                for n in letter_num_dict[int(digits_list[3])]:
                                    each = i+k+m+n
                                    each_list.append(each)
                            except:
                                pass
                    except:
                        pass
            except:
                pass
    except:
        pass
    return [i for i in each_list if len(i) == len(digits_list)]

print(Letter_Combinations_of_a_Phone_Number("2345"))
print(Letter_Combinations_of_a_Phone_Number("234"))
print(Letter_Combinations_of_a_Phone_Number("23"))