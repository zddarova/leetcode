#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (46.00%)
# Likes:    19844
# Dislikes: 4794
# Total Accepted:    4.9M
# Total Submissions: 10.6M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
#
# If there is no common prefix, return an empty string "".
#
#
# Example 1:
#
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#
#
# Example 2:
#
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
#
# Constraints:
#
#
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.
#
#
#

# @lc code=start
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = strs[0]
        for i in range(1, len(strs)):
            word: str = strs[i]
            if len(word) == 0:
                return ""
            for y in range(len(word)):
                symbol: str = word[y]

                if y > len(result) - 1:
                    continue

                if symbol != result[y]:
                    result: str = result[0:y]
                elif len(word) < len(result):
                    result = result[0 : len(word)]

        return result


# @lc code=end

assert Solution().longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
assert Solution().longestCommonPrefix(["ab", "a"]) == "a"
assert Solution().longestCommonPrefix(["a", "b"]) == ""
assert Solution().longestCommonPrefix(["abab", "aba", ""]) == ""
assert Solution().longestCommonPrefix(["ca", "a"]) == ""
