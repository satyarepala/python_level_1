"""
Problem Statement: Palindromic Substrings Count

You are given a string s. Your task is to write a Python function count_palindromic_substrings(s) that counts the
number of palindromic substrings in the given string.

A palindromic substring is a substring that reads the same forwards and backward. For example, in the string
"racecar," the palindromic substrings are "racecar," "aceca," and "cec."

Write a function that efficiently calculates and returns the count of palindromic substrings in the given string s.

"""

def count_palindromic_substrings(s):
    def expand_around_center(left, right):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            count += 1
        return count

    count = 0
    for i in range(len(s)):
        # Odd-length palindromic substrings
        count += expand_around_center(i, i)

        # Even-length palindromic substrings
        count += expand_around_center(i, i + 1)

    return count

# Test cases
print(count_palindromic_substrings("abba"))  # Output: 4
print(count_palindromic_substrings("abcde"))  # Output: 5
print(count_palindromic_substrings("banana"))  # Output: 9
