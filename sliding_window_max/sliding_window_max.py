'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    new_arr = []

    pointer_1 = 0
    pointer_2 = k - 1
    while pointer_2 != len(nums):
        temp_list = nums[pointer_1:pointer_2 + 1]
        max_of_window = max(temp_list)
        pointer_1 += 1
        pointer_2 += 1
        new_arr.append(max_of_window)

    return new_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
