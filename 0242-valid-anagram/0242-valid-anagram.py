class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter

        s_dict, t_dict = Counter(s), Counter(t)

        for key, value in s_dict.items():
            if key not in t_dict or t_dict[key] < value:
                return False
        
        for key, value in t_dict.items():
            if key not in s_dict or s_dict[key] < value:
                return False
        
        return True



        
        return sorted(s) == sorted(t)