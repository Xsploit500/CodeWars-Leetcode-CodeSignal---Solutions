class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        fullarr = set(nums1 + nums2 + nums3)

        def buildcount(arr):
            count = {}

            for val in arr:
                count[val] = count.get(val, 0) + 1

            return count

        count1, count2, count3 = buildcount(nums1), buildcount(nums2), buildcount(nums3)

        output = []

        for num in fullarr:
            if (num in count1 and num in count2) or (num in count1 and num in count3) or (num in count2 and num in count3):
                output.append(num)

        return output
                

        
