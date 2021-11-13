def Palindromic_Number(num):
    if -2**31 <= num <= (2**31)-1:
        string = str(num)
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
    else:
        return "The number is beyond the constraints"

print(Palindromic_Number(151))
print(Palindromic_Number(-154))
print(Palindromic_Number(-1544683908186))