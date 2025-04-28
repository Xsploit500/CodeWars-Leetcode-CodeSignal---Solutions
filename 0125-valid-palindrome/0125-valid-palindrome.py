class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = [i.lower() for i in s if i.isalnum()]

        return chars == chars[::-1]