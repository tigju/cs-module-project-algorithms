'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

from collections import deque
import time

## First pass solution
# def sliding_window_max(nums, k):
#     # Your code here
#     newArr = []
#     i = 0
#     while i <= len(nums)-k:
#         max_val = max(nums[i:k+i])
#         newArr.append(max_val)
#         i += 1
#     return newArr

# optimized solution
def sliding_window_max(nums, k):
    max_vals = []
    q = deque()
    # remove all elems from a queue
    for i, n in enumerate(nums):
        while len(q) > 0 and n > q[-1]:
            q.pop()

        q.append(n)

        # calc the window range
        window_range = i - k + 1

        # as long as our windows range == k, then we will add elements to the queue
        if window_range >= 0:
            # add the max elem (in this case 1st in the queue) to the max_vals
            max_vals.append(q[0])

            # check num on the left needs to be evicted
            # if so take it out of the start of the queue
            if nums[window_range] == q[0]:
                q.popleft()

    return max_vals



if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = []
    with open("data/input.txt") as file:
        for line in file:
            arr.append(int(line.strip()))
    k = 1000
    start_time = time.time()
    sliding_window_max(arr, k)
    # print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
    end_time = time.time()

    print(end_time - start_time)
