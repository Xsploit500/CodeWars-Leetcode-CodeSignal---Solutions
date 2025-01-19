class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        if len(s) == 0:
            return True

        occurences, frequencies = {}, []

        for char in s:
            occurences[char] = occurences.get(char, 0) + 1

        for key, value in occurences.items():
            frequencies.append(value)

        if len(set(frequencies)) > 1:
            return False
        else:
            return True