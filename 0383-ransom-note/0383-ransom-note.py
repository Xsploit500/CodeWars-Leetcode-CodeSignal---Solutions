class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_dict, magazine_dict = {}, {}

        for char in ransomNote:
            ransom_dict[char] = ransom_dict.get(char, 0) + 1
        
        for char in magazine:
            magazine_dict[char] = magazine_dict.get(char, 0) + 1

        for key, value in ransom_dict.items():
            if key not in magazine_dict or magazine_dict[key] < value:
                return False
        
        return True

        