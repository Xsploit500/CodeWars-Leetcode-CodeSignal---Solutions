class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = 0
        for char in arr:
            if arr.count(char) == 1:
                count += 1
                if count == k:
                    return char
        return ""

        
        #Method 1 - Ordered Dictionary
        from collections import OrderedDict

        occurences = OrderedDict()

        for char in arr:
            occurences[char] = occurences.get(char, 0) + 1

        for char, count in occurences.items():
            if count == 1:
                k -= 1
                if k == 0:
                    return char
        
        return ""



        #Method 2 - Using a Hashmap and List
        occurences, distinct = {}, []

        for char in arr:
            if char not in occurences:
                occurences[char] = 1
            else:
                occurences[char] += 1

        for key, value in occurences.items():
            if value == 1:
                distinct.append(key)

        return "" if len(distinct) < k else distinct[k - 1]