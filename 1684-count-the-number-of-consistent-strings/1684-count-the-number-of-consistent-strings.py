class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        output = 0

        allowed = set(list(allowed))

        for word in words:
            word = set(list(word))
            for char in word:
                if char not in allowed:
                    break
            else:
                output += 1

        return output