#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (42.73%)
# Likes:    26453
# Dislikes: 1926
# Total Accepted:    6.5M
# Total Submissions: 15.2M
# Testcase Example:  '"()"'
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
#
# An input string is valid if:
#
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#
#
#
# Example 1:
#
#
# Input: s = "()"
#
# Output: true
#
#
# Example 2:
#
#
# Input: s = "()[]{}"
#
# Output: true
#
#
# Example 3:
#
#
# Input: s = "(]"
#
# Output: false
#
#
# Example 4:
#
#
# Input: s = "([])"
#
# Output: true
#
#
# Example 5:
#
#
# Input: s = "([)]"
#
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.
#
#
#


# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False

        stack: list[str] = list[str]()

        open_brackets: list[str] = ["(", "[", "{"]
        close_brackets: list[str] = [")", "]", "}"]
        closed_to_open: dict[str, str] = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        for item in s:
            if item in open_brackets:
                stack.append(item)
            elif item in close_brackets:
                if len(stack) == 0:
                    return False
                top_item: str = stack.pop()
                if top_item != closed_to_open[item]:
                    return False
            else:
                return False

        return len(stack) == 0


# @lc code=end
