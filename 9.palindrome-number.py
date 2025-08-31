#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number/description/
#
# algorithms
# Easy (59.54%)
# Likes:    14589
# Dislikes: 2849
# Total Accepted:    6.9M
# Total Submissions: 11.5M
# Testcase Example:  '121'
#
# Given an integer x, return true if x is a palindrome, and false otherwise.
#
#
# Example 1:
#
#
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
#
#
# Example 2:
#
#
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it
# becomes 121-. Therefore it is not a palindrome.
#
#
# Example 3:
#
#
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a
# palindrome.
#
#
#
# Constraints:
#
#
# -2^31 <= x <= 2^31 - 1
#
#
#
# Follow up: Could you solve it without converting the integer to a string?
#


# @lc code=start
from math import ceil


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        s = str(x)
        for i in range(len(s)):
            if i >= ceil(len(s) / 2):
                break
            if s[i] != s[-i - 1]:
                return False

        return True


# @lc code=end


assert Solution().isPalindrome(121) == True
