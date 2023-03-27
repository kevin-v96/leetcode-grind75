#https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        output = 0
        for right in range(len(s)):
            if s[right] not in seen:
                output = max(output, right - left + 1)
            else:
                #if it's not in the window
                if seen[s[right]] < left:
                    output = max(output, right - left + 1)
                else:
                    left = seen[s[right]] + 1

            seen[s[right]] = right

        return output