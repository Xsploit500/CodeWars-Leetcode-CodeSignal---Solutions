class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        left, right = 0, 0

        min_length = min([len(string) for string in strs])
        
        checker = [string for string in strs if len(string) == min_length]

        while right < min_length:
            count = 0
            for string in strs:
                if checker[0][right] == string[right]:
                    count += 1
            if count == len(strs):
                prefix += checker[0][right]
                count = 0
            right += 1

        return prefix