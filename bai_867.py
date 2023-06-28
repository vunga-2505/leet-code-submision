class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        A=len(matrix[0])
        x=len(matrix)
        return [ [ matrix[j][i] for j in range(x)]  for i in range(A)]