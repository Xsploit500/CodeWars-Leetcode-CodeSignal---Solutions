class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1, min2 = float('inf'), float("inf")

        for price in prices:
            if price < min1:
                min1, min2 = price, min1
            elif price < min2:
                min2 = price

        leftover = money - (min1 + min2)

        return money if leftover <= -1 else leftover