class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        output = t

        while t > 0:
            num += 1
            t -= 1

        return num + output