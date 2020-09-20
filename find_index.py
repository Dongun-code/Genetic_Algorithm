import numpy as np

class find_index:
    def compare_value(self, value):
        left = 0
        right = len(value)
        print(value)

        m = 0.8807685985303476

        while left <= right:
            middle = (left+right)//2
            if value[middle] == m:
                return middle+1
            elif value[middle] > m:
                right = middle - 1
            else:
                left = middle + 1
        return middle


# regressor_result_list = [0.4138410374558745, 0.44534467404874734, 0.7250403628102964, 0.8170224948838356, 0.8615194561873204, 0.8807685985303476, 0.9532861754098799]

# left = 0
# right = len(regressor_result_list)
# print(right)
# m = 0.8807685985303476
# parent_index = []
# for m in regressor_result_list[-5:]:
#     print('m value',m)
#     while left <= right:
#         middle = (left + right) // 2
#         print('mid',middle)
#         if regressor_result_list[middle] == m:
#             print(regressor_result_list[middle])
#             m = middle + 1
#             break
#         elif regressor_result_list[middle] > m:
#             right = middle - 1
#         else:
#             left = middle + 1
#     print('final middle', middle)
#     parent_index.append(middle)
#
# print(parent_index)[array([[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0,
