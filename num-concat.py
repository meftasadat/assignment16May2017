import itertools

# input test cases; I added one with Sean's test case
input_arr_case_1 = [99, 99975]
input_arr_case_2 = [99, 5, 991, 9, 9999, 999231, 15, 1]


# The naive approach as we discussed
def get_max_concat_naively(input_arr):
    max_out_num = 0
    for i in itertools.permutations(input_arr):
        out_num = ''

        for j in range(0, len(input_arr)):
            out_num = (out_num + str((i[j])))

        if int(out_num) > max_out_num:
            max_out_num = int(out_num)

    return max_out_num


# Helper Function
def compare_two_elements(first, second):
    my_flag = True
    first_element_len = (len(str(first)))
    second_element_len = (len(str(second)))
    max_iter_len = min([first_element_len, second_element_len])

    for i in range(0, max_iter_len):

        if int(str(first)[i]) < int(str(second)[i]):
            my_flag = False

    return my_flag


# The alternative approach
def get_max_concat(arr):
    result_set = []
    arr_ = arr
    i = 0
    while len(arr_) > 0:

        if i == len(arr):
            i = 0
        if arr[i] not in result_set:

            flag_ = True
            for j in range(0, len(arr_)):

                if compare_two_elements(arr[i], arr_[j]) is False:
                    flag_ = False

            if flag_ is True:
                # print(arr[i])
                arr_ = (list(set(arr_)-{arr[i]}))
                result_set.append(arr[i])
        i += 1
    out_num = ''

    for i in range(0, len(result_set)):
        out_num += str(result_set[i])
    return out_num


# Running Test Case #1
print(get_max_concat(input_arr_case_1))
print(get_max_concat_naively(input_arr_case_1))


# Running Test Case #2
print(get_max_concat(input_arr_case_2))
print(get_max_concat_naively(input_arr_case_2))
