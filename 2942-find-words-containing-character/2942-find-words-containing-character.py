class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        output = []

        for i, n in enumerate(words):
            if x in n:
                output.append(i)
                
        return output