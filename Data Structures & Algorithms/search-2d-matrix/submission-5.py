class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        while i < len(matrix):
            if target > matrix[i][len(matrix[i])- 1]:
                i+=1
            else:
                if target < matrix[i][0]: return False
                else:
                    l = 0
                    r = len(matrix[i]) - 1
                    while l <= r:
                        m = (l+r)//2
                        if matrix[i][m] < target:
                            l = m + 1
                        elif matrix[i][m] > target:
                            r = m - 1
                        else:
                            return True
                    return False
        return False