class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_length = min(len(word1), len(word2))

        result = ""

        for i in range(min_length):
            result += word1[i]
            result += word2[i]
        
        result += word1[i + 1:]
        result += word2[i + 1:]

        return result
        