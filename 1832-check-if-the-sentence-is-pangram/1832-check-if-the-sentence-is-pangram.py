class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        from collections import Counter

        letters = "abcdefghijklmnopqrstuvwxyz"

        counts = Counter(sentence)

        for char in letters:
            if char not in counts:
                return False
        return True

        