class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            key = tuple(sorted(s))
            groups.setdefault(key, []).append(s)
        return list(groups.values())

        
        
        # groups = {}
        # for string in strs:
        #     key = "".join(sorted(string))
        #     if key not in groups:
        #         groups[key] = []
        #     groups[key].append(string)
        # return list(groups.values())
        