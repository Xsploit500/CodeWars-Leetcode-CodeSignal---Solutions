class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        values = []

        for arr in grid:
            values.extend(arr)

        from collections import Counter
        
        output = []

        count = Counter(values)

        for key, val in count.items():
            if val > 1:
                output.append(key)

        for i in range(1, max(values) + 2):
            if i not in count:
                output.append(i)
                break


        return output

        


        