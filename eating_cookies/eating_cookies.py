'''
Input: an integer
Returns: an integer
'''

# first pass solution
# def eating_cookies(n):
#     # base condition when to stop recurrsion
#     if n == 0:
#         return 1
#     if n < 0:
#         return 0

#     return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)
        
# Optimal solution
def eating_cookies(n, cache):
    # base condition when to stop recurrsion
    if n == 0:
        return 1

    if n < 0:
        return 0
    # check if we have n in cache
    if cache[n] > 0:
        return cache[n]

    cookie_1 = eating_cookies(n-1, cache)
    cookie_2 = eating_cookies(n-2, cache)
    cookie_3 = eating_cookies(n-3, cache)
    
    result = cookie_1 + cookie_2 + cookie_3
    cache[n] = result

    return result



if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 7

    print(
        f"There are {eating_cookies(50, [0 for i in range(51)])} ways for Cookie Monster to each {num_cookies} cookies")
