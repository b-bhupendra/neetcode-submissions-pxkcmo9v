class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # initial approach create a new list using the matrix flatten it 
        # then go apply binary search 
        # space optimization 
        # first find the row the potential value might exist 
        # then apply binary search on that column
        # and return the result

        # mapped approch 
        return self.map2DTo1D(matrix, target) != (-1,-1)

        rowIdx = self.returnRowIndex(matrix, target)
        
        if rowIdx != -1:
            index = self.binarySearch(matrix[rowIdx], target)
            return index != -1
        
        return False


    def returnRowIndex(self, ls: List[List[int]], target) -> int:
        # return row index if exist otherwise -1
        init , end = 0 , len(ls) - 1
        # first and last index

        while init <= end:
            mid = (init + end) // 2
            #check if the target exist in middle rows range , else check if target is greater than last value so increment left by 1 else it will certainly fall under the mid so update the end row to -1 

            if ls[mid][0] <= target <= ls[mid][-1]:
                return mid
            elif ls[mid][-1] < target:
                init = mid + 1
            else:
                end = mid - 1

        return -1


    # returns index
    def binarySearch(self, ls : List[int], target) -> int:
        
        l , r = 0 , len(ls) - 1
        
        while l <= r:
            
            mid = (l + r) // 2

            if target == ls[mid]:
                return mid
            elif target > ls[mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1 # none found



    def map2DTo1D(self,ls : List[List[int]], target)-> int:
        
        ROW = len(ls)
        COL = len(ls[-1])

        l , r = 0 , len(ls) * len(ls[0]) - 1

        while l <= r:
            
            mid = (l + r) // 2

            row = mid // COL
            col = mid % COL
            # print(f"pointers to {l} , {r}")
            # print(f" Our r, c is {row}, {col} our mid is {mid} , mid val {ls[row][col]} and we are searching for {target} ")
            if ls[row][col] == target:
                return (row, col)
            elif ls[row][col] > target:
                r = mid - 1
            else:
                l = mid + 1
            # print(f"updated pointers to   {l} , {r}",end="\n\n")

        return (-1, -1)