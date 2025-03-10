class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        mid_state, output = {}, []
        
        for num in nums1:
            if num[0] not in mid_state:
                mid_state[num[0]] = 0
            mid_state[num[0]] += num[1]

        for num in nums2:
            if num[0] not in mid_state:
                mid_state[num[0]] = 0
            mid_state[num[0]] += num[1]

        for key, value in mid_state.items():
            output.append([key, value])

        return sorted(output, key = lambda x: x[0])
