class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        count = 0

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and self.checkRow(i, mat) and self.checkColumn(j, mat):
                    count += 1

        return count

    def checkRow(self, i: int, mat: List[List[int]]) -> bool:
        count = 0
        for j in range(len(mat[0])):
            if mat[i][j] == 1:
                count += 1
                if count > 1:
                    return False

        return True

    def checkColumn(self, j: int, mat: List[List[int]]) -> bool:
        count = 0
        for i in range(len(mat)):
            if mat[i][j] == 1:
                count += 1
                if count > 1:
                    return False

        return True