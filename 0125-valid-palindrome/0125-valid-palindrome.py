class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Two Pointer Approach

        cleaned_s = ""

        for char in s:
            if char.isalnum():
                cleaned_s += char.lower()

        left, right = 0, len(cleaned_s) - 1

        while left <= right:
            if cleaned_s[left] != cleaned_s[right]:
                return False
            left += 1
            right -= 1
        
        return True




        new_s = ""

        for i in s:
            if i.isalnum():
                new_s += i.lower()

        return new_s == new_s[::-1]
        