#this file has 3 parts:
#Assignments For Lessons 26 To 32
###########################################################

# #1
    # my_list = [1, 2, 3, 3, 4, 5, 1]
    # unique_list = [1, 3]
        # x = set(my_list)
        # y = set(unique_list)
        # z = x.union(y)
            # new_list = list(z)
            # print(new_list)
            # print(type(new_list))

                # new_list.pop(-1)
                # print(new_list)

#2
# nums = {1, 2, 3}
# letters = {"A", "B", "C"}

        #1 method
        # nums |= letters
        # print(nums)

        #2 method
        # nums.update(letters)
        # print(nums)

        #3 method
        # x = list(nums)
        # y = list(letters)
        # x.extend(y)
        # # print(x)
        # nums = set(x)
        # print(nums)

# #3
# my_set = {1, 2, 3}
# letters = {"A", "B", "C"}

# print(my_set)
# my_set.clear()
# print(my_set)
# my_set.update(letters)
# print(my_set)
# my_set.discard("C")
# print(my_set)

# #4
# set_one = {1, 2, 3}
# set_two = {1, 2, 3, 4, 5, 6}

# # set_one.superset(set_two)
# print(set_one.issubset(set_two))


