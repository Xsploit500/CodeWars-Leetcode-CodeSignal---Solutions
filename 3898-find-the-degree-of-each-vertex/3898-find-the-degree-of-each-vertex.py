class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        def one_count(arr):
            output = {}

            for i in arr:
                output[i] = output.get(i, 0) + 1
            return output
        
        result = []

        for mat in matrix:
            counts = one_count(mat)
            if 1 in counts.keys():
                result.append(counts[1])
            else:
                result.append(0)
        
        return result

        