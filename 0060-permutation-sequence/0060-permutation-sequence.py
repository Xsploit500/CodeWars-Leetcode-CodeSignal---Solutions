class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        from itertools import permutations

        string = ""

        for i in range(1, n + 1):
            string += str(i)

        output = ["".join(perm) for perm in permutations(string)]

        return output[k-1]

        
        
        
        
        # string = ""

        # for i in range(1, n + 1):
        #     string += str(i)

        # def permute(string, prefix="", perm=None):
        #     if perm is None:
        #         perm = []
    
        #     if len(string) == 0:
        #         perm.append(prefix)
            
        #     else:
        #         for i in range(len(string)):
        #             rem = string[:i] + string[i + 1:]
        #             permute(rem, prefix + string[i], perm)
            
        #     return perm

        # output = permute(string, prefix, [])

        # return sorted(output)[k-1][4:]