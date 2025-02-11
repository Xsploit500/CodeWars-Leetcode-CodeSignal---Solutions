class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        plus, minus = 0, 0

        for operation in operations:
            if operation == "++X" or operation == "X++":
                plus += 1
            else:
                minus -= 1

        return plus + minus