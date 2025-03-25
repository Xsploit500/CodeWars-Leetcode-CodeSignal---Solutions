class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        Hmap, output = {}, []

        for num in nums:
            if num not in Hmap:
                Hmap[num] = 0
            Hmap[num] += 1

        for num in nums:
            smaller_vals = 0

            for key, value in Hmap.items():
                if key < num:
                    smaller_vals += Hmap[key]
            output.append(smaller_vals)

        return output


        
        # output = []

        # for i in nums:
        #     smaller = 0

        #     for j in nums:
        #         if j < i:
        #             smaller += 1
            
        #     output.append(smaller)

        # return output
        