'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    new_arr = []

    for i in arr:
        if i != 0:
            new_arr.append(i)
    for i in arr:
        if i == 0:
            new_arr.append(i)

    return new_arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")