class Solution:
    def scoreOfString(self, s: str) -> int:
        output = 0

        left, right = 0, 1

        while right < len(s):
            output += abs(ord(s[right]) - ord(s[left]))
            left += 1
            right += 1

        return output