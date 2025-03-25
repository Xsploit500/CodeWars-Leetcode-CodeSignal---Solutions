class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        Hmap, output = {}, []

        for i, n in enumerate(heights):
            Hmap[n] = names[i]

        Hmap = sorted(Hmap.items(), key=lambda x:x[0], reverse=True)

        for val in Hmap:
            output.append(val[1])

        return output