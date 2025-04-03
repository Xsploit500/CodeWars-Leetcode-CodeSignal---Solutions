class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        Hmap = {5: 0, 10: 0}

        for bill in bills:
            if bill == 5:
                Hmap[5] += 1
            
            elif bill == 10:
                if Hmap[5] > 0:
                    Hmap[5] -= 1
                    Hmap[10] += 1
                else:
                    return False

            elif bill == 20:
                if Hmap[5] > 0 and Hmap[10] > 0:
                    Hmap[10] -= 1
                    Hmap[5] -= 1
                elif Hmap[5] >= 3:
                    Hmap[5] -= 3
                else:
                    return False
        
        return True
