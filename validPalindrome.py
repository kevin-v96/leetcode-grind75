# https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = re.sub(r'[\W_]', '', s.lower())
        return string == string[::-1]