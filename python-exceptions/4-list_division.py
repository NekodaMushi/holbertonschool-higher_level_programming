#!/usr/bin/python3
"""divides element by element 2 lists"""


def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
        except (ValueError, TypeError):
            res = 0
            print("wrong type")
        except ZeroDivisionError:
            res = 0
            print("division by 0")
        except IndexError:
            print("out of range")
            res = 0
        finally:
            result_list.append(res)
    return result_list
