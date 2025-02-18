def two_sum_sorted(arr, target):
    """
    Finds two indices in a sorted array where the sum equals the target using the two-pointer technique.

    Algorithm:
    - Initialize two pointers: one at the start (left) and one at the end (right).
    - Calculate the sum of the elements at these indices.
    - If the sum equals the target, return the indices.
    - If the sum is smaller than the target, move the left pointer rightward.
    - If the sum is greater than the target, move the right pointer leftward.
    - Repeat until the pointers meet.

    Parameters:
    arr (list[int]): A sorted list of integers.
    target (int): The target sum to find.

    Returns:
    list[int]: A list containing the indices of the two numbers that sum to the target.
               Returns an empty list if no valid pair is found.

    Example Usage:
    >>> two_sum_sorted([1, 2, 3, 4, 5, 6], 6)
    [0, 4]

    Time Complexity: O(n), where n is the length of the array.
    Space Complexity: O(1), as only two pointers are used.
    """
    left_index, right_index = 0, len(arr) - 1

    while left_index < right_index:
        current_sum = arr[left_index] + arr[right_index]
        if current_sum == target:
            return [left_index, right_index]
        elif current_sum < target:
            left_index += 1
        else:
            right_index -= 1

    return []


def two_sum_unsorted(arr, target):
    """
    Finds two indices in an unsorted array where the sum equals the target using brute force.

    Algorithm:
    - Iterate over each pair of elements in the array.
    - Check if the sum of any two elements equals the target.
    - If found, return their indices.
    - If no such pair exists, return an empty list.

    Parameters:
    arr (list[int]): An unsorted list of integers.
    target (int): The target sum to find.

    Returns:
    list[int]: A list containing the indices of the two numbers that sum to the target.
               Returns an empty list if no valid pair is found.

    Example Usage:
    >>> two_sum_unsorted([2, 5, 3, 7, 8], 12)
    [2, 3]
    >>> two_sum_unsorted([1, 4, 6, 8], 10)
    [1, 2]

    Time Complexity: O(n²), where n is the length of the array.
    Space Complexity: O(1), as no extra space is used.
    """
    arr_length = len(arr)

    for i in range(arr_length):
        for j in range(i + 1, arr_length):
            if arr[i] + arr[j] == target:
                return [i, j]
    
    return []



print(two_sum_sorted([1,2,3,4,5,6], 6))
print(two_sum_unsorted([2,5,3,7,8], 12))


