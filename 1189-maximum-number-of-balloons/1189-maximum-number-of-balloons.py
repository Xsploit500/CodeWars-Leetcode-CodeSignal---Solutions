class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import Counter

        text_count, string_count = Counter(text), Counter('balloon')

        return min([text_count[char] // string_count[char] for char in string_count])

        