class Solution:
    def decodeMessage(self, key: str, message: str) -> str:

        Hmap, output = {}, ""

        alphabets = 'abcdefghijklmnopqrstuvwxyz'

        count = 0

        for char in key:
            if char not in Hmap and char != " ":
                Hmap[char] = alphabets[count]
                count += 1
        
        for char in message:
            if char == " ":
                output += " "
            else:
                output += Hmap[char]

        return output

        