class Solution:
    def convertDateToBinary(self, date: str) -> str:
        result = ""

        values = date.split("-")

        for val in values:
            current_val = int(val)
            binary_val = ""

            while current_val != 0:
                current_val, remainder = current_val // 2, current_val % 2
                binary_val += str(remainder)
            
            binary_val = binary_val[::-1]
            result += binary_val + "-"

        return result[0:len(result) - 1]