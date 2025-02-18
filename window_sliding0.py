def max_sum(arr, k):
    """
    Finds the maximum sum of any contiguous subarray of size `k` using the sliding window technique.

    Parameters:
    arr (list): A list of integers.
    k (int): The size of the subarray.

    Returns:
    int | None: The maximum sum of any contiguous subarray of size `k`, or None if `k` is greater than the array length.
    
    Example:
    >>> max_sum([1, 4, 2, 10, 2, 3, 1, 0, 20], 4)
    24
    """
    arr_length = len(arr)

    if arr_length <= k:
        return None
    
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(arr_length - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(window_sum, max_sum)

    return max_sum

print(max_sum([1, 4, 2, 10, 2, 3, 1, 0, 20], 4))