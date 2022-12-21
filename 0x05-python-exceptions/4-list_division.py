#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    # Check if element at index i in my_list_1 is an integer or float
    for i in range(list_length):
        try:
            if not isinstance(my_list_1[i], (int, float)):
                print("Wrong type")
                result.append(0)
                continue
        # Check if element at index i in my_list_2 is an integer or float
            if not isinstance(my_list_2[i], (int, float)):
                print("Wrong type")
                result.append(0)
                continue
            # Check if element at index i in my_list_2 is 0
            if my_list_2 == 0:
                print("division by 0")
                result.append(0)
                continue
            # Divide elements and append result to result list
            result.append(my_list_1[i] / my_list_2[i])
        except IndexError:
            print("out of range")
            result.append(0)
    return result
    