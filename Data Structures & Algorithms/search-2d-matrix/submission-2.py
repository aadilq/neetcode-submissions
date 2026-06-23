class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        TOP, BOTTOM = 0, ROWS - 1

        while TOP <= BOTTOM:
            mid_row = (TOP + BOTTOM) // 2
            if target < matrix[mid_row][0]:
                BOTTOM = mid_row - 1
            elif target > matrix[mid_row][-1]:
                TOP = mid_row + 1
            else:
                break
        
        mid_row = (TOP + BOTTOM) // 2

        L, R = 0, COLS - 1
        while L <= R:
            mid = (L + R) // 2
            if matrix[mid_row][mid] == target:
                return True
            elif target < matrix[mid_row][mid]:
                R = mid - 1
            else:
                L = mid + 1
        return False
        