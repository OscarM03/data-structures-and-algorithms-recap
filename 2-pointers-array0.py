def is_palindrome(s):
    """
        Determines whether a string is a palindrome using two-pointer technique
        A palindrome is a word, phrase, or sequence that reads the same forward and backward.

        Algorithm:
        - Use two pointers: one starting from the left and one from the right.
        - Compare characters at these positions.
        - If any pair does not match, return False.
        - Move the pointers towards the center until they meet.

        Returns:
        bool: True if the string is a palindrome, False otherwise.

        Example Usage:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("hello")
        False

        Time Complexity: O(n), where n is the length of the string.
        Space Complexity: O(1), as we use only two pointers.
    """
    left_index, right_index = 0, len(s) - 1
    while left_index < right_index:
        if s[left_index] != s[right_index]:
            return False
        
        left_index += 1
        right_index -= 1

    return True

print(is_palindrome("racecar"))
print(is_palindrome("hello"))