class Solution:

    def recursive(self, n):
        if n == 1:
            return [[1]]
        elif n == 2:
            return [[1], [1, 1]]
        else:
            previous_result = self.recursive(n-1)
            last_result = previous_result[-1]
            current_result = []
            current_result.append(1)
            for i in range(len(last_result)-1):
                current_result.append(last_result[i] + last_result[i+1])
            current_result.append(1)
            return previous_result + [current_result]

    def generate(self, numRows: int) -> List[List[int]]:
        return self.recursive(numRows)