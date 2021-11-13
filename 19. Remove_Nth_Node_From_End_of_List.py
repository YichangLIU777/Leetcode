def Remove_Nth_Node_From_End_of_List(head, n):
    head.pop(-n)
    return head

print(Remove_Nth_Node_From_End_of_List([1], 1))
print(Remove_Nth_Node_From_End_of_List([1,2,3,4,5], 2))