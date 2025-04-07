class Solution:
    def repeatedCharacter(self, s: str) -> str:
        Hmap = {}

        for char in s:
            if char not in Hmap:
                Hmap[char] = 0
                Hmap[char] += 1
            else:
                return char
                
