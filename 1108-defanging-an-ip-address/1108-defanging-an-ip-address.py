class Solution:
    def defangIPaddr(self, address: str) -> str:
        output = ""

        for char in address:
            if char == ".":
                output += "[.]"
            else:
                output += char

        return output