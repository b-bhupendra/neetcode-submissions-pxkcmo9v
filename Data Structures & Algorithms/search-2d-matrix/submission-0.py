class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # initial approach create a new list using the matrix flatten it 
        # then go apply binary search 

        flatten = [ n  for d in matrix for n in d  ]
        print(flatten)
        # return True
        index = self.binarySearch(flatten, target)
        return index != -1

    # returns index
    def binarySearch(self, ls : List[int], target) -> int:
        
        l , r = 0 , len(ls) - 1
        # print("Are we reaching here !!!!")
        while l <= r:
            # print(ls, target)
            mid = (l + r) // 2

            if target == ls[mid]:
                return mid
            elif target > ls[mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1 # none found
                