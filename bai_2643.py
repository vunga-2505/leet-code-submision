class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_index = -1
        max_count = -1
        for i in range(len(mat)):
            count = mat[i].count(1)
            if count >= max_count:
                if count > max_count or max_index == -1:
                    max_index = i
                    max_count = count
        return [max_index, max_count]