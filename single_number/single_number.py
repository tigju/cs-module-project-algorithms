'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
import time
import random

# First-Pass solution
# def single_number(arr):
#     # Your code here
#     for i in arr:
#         if arr.count(i) < 2:
#             return i

# optimal solution
def single_number(arr):
    # Your code here
    count_nums = {}
    for i in arr:
        if i in count_nums:
            del count_nums[i]
        else:
            count_nums[i] = 1
    return count_nums

# optimal + lightweight (slight difference from dictionaries)
# def single_number(arr):
#     # Your code here
#     count_nums = set()
#     for i in arr:
#         if i in count_nums:
#             count_nums.discard(i)
#         else:
#             count_nums.add(i)
#     return count_nums


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    # print(f"The odd-number-out is {single_number(arr)}")
    arr = []
    for i in range(10000000):
            arr.append(i)
            arr.append(i)

    random.shuffle(arr)
    rand_index = random.randint(0, len(arr))
    num = arr.pop(rand_index)

    start_time = time.time()
    print(single_number(arr))
    end_time = time.time()

    print(end_time - start_time)
