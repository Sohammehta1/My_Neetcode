class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])# rows, cols
        # First find the row in which the target element might be present

        l = 0
        h = m-1
        target_row = 0
        while l <=h:
            mid = (l+h)//2
            if matrix[mid][0] <= target:
                if matrix[mid][-1] >= target :# target present in this row
                    target_row = mid
                    break
                else:
                    l = mid+1
            else:
                h = mid-1
        l, r = 0,n-1
        while l <=r:
            mid = (l+r)//2
            if matrix[target_row][mid] ==target:
                return True
            elif matrix[target_row][mid] > target:
                r = mid-1
            else:
                l = mid+1
        return False
        
            