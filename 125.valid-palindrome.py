#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (51.56%)
# Likes:    10749
# Dislikes: 8580
# Total Accepted:    4.6M
# Total Submissions: 8.9M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# A phrase is a palindrome if, after converting all uppercase letters into
# lowercase letters and removing all non-alphanumeric characters, it reads the
# same forward and backward. Alphanumeric characters include letters and
# numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.
#
#
# Example 1:
#
#
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
#
#
# Example 2:
#
#
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
#
#
# Example 3:
#
#
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric
# characters.
# Since an empty string reads the same forward and backward, it is a
# palindrome.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 2 * 10^5
# s consists only of printable ASCII characters.
#
#
#

# @lc code=start


class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabetic_s: str = ""
        for c in s:
            if c.isalpha() or c.isnumeric():
                alphabetic_s += c
        lower_case_s: str = alphabetic_s.lower()
        no_space_s: str = lower_case_s.strip(" ")

        s = no_space_s

        for i in range(0, len(s)):
            a: str = s[i]
            b: str = s[len(s) - 1 - i]
            if a != b:
                return False
            if i > len(s) / 2:
                return True

        return True


# @lc code=end


assert Solution().isPalindrome("0P") == False
assert Solution().isPalindrome(" ") == True
