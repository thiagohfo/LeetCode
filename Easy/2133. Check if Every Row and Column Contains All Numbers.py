class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        import numpy as np

        for i in range(1, len(matrix) + 1):
            for j in range(len(matrix)):
                if i not in matrix[j]:
                    return False

        matrix_T = np.array(matrix).transpose()

        for i in range(1, len(matrix_T) + 1):
            for j in range(len(matrix_T)):
                if i not in matrix_T[j]:
                    return False

        return True