class Solution:
    def getLucky(self, s: str, k: int) -> int:
        characters = "abcdefghijklmnopqrstuvwxyz"

        charToNum = ""
        total = 0
        
        for i in s:
            charToNum += str(characters.index(i) + 1)
        
        while k > 0:
            values = []
            for char in list(charToNum):
                values.append(int(char))
            total = sum(values)
            k -= 1
            charToNum = str(total)

        return total