class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        #12.37
        
        #BS1
        rows,cols = len(matrix), len(matrix[0])
        left,right = 0,rows-1
        while left <= right:
            mid = (left + right) // 2
            rowStart,rowEnd = matrix[mid][0],matrix[mid][cols-1]
            print(rowStart,rowEnd)
            if  target >= rowStart and target <= rowEnd:
                print("Mid is",mid)
                break
            if target > rowStart and target > rowEnd:
                left = mid + 1
            else:
                right = mid - 1
        
        if left > right:
            return False
        
        #BS2
        l = 0
        r = cols - 1

        while l <= r:
            m =(l + r) // 2
            print(mid,m)
            if matrix[mid][m] == target:
                return True
            if matrix[mid][m] < target:
                l = m + 1
            else:
                r = m - 1
        return False
             






        