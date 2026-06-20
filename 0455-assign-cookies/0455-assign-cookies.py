class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g_ptr, s_ptr = 0, 0

        g.sort()
        s.sort()

        if len(s) == 0:
            return 0

        count = 0

        while s_ptr < len(s) and g_ptr < len(g):
            while s_ptr < len(s) and g[g_ptr] > s[s_ptr]:
                s_ptr += 1
            if s_ptr < len(s) and g[g_ptr] <= s[s_ptr]:
                count += 1
                g_ptr += 1
                s_ptr += 1

        return count