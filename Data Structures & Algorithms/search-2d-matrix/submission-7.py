class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])

        top=0
        bottom=rows-1

        while top <=bottom:
            row=top + (bottom-top)//2

            if target > matrix [row][-1]:
                top=row+1
            elif target < matrix [row][0]:
                bottom=row-1
            else:
                break
        if not(top<=bottom):
            return False
        l,r=0,cols-1

        while (l<=r):
            mid=l+(r-l)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid]>target:
                r=mid-1
            else:
                l=mid+1
        return False
        