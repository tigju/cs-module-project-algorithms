'''
Input: a List of integers
Returns: a List of integers
'''
# Firs-Pass solution
# def moving_zeroes(arr):
#     # Your code here
#     # get zeros from arr
#     zeros = [n for n in arr if n == 0]
#     # get non zeros from array
#     non_zeros = [n for n in arr if n != 0]
#     # return concatenated array
#     return non_zeros+zeros


# def moving_zeroes(arr):
#     # Your code here
#     count = 0
#     while min(arr) == 0:
#         count += 1
#         arr.remove(min(arr))

#     return arr + [0]*count

def moving_zeroes(arr):
    for i in range(len(arr)):
        if arr[i] != 0:
            arr.insert(0, arr.pop(i))
    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    # arr = [0, 3, 1, 0, -2]
    arr2 = [0, 0, 0, 0, 3, 2, 1]
    # print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")

    print(moving_zeroes(arr2))
