#https://leetcode.com/problems/minimum-window-substring/
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash_map = Counter(t)
        start, end = 0, 0

        min_window_length = len(s) + 1
        min_window_start = 0
        num_of_chars_to_be_included = len(t)

        while end < len(s):
            if s[end] in hash_map:
                if hash_map[s[end]] > 0:
                    num_of_chars_to_be_included -= 1
                hash_map[s[end]] -= 1

            # If the current window has all the desired chars
            while num_of_chars_to_be_included == 0:
                if end - start + 1 < min_window_length:
                    min_window_length = end - start + 1
                    min_window_start = start

                if s[start] in hash_map:
                    hash_map[s[start]] += 1

                    if hash_map[s[start]] > 0:
                        num_of_chars_to_be_included += 1

                start += 1

            end += 1

        if min_window_length == len(s) + 1:
            return ""
        else:
            return s[min_window_start:min_window_start + min_window_length]