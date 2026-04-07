class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # mp = defaultdict(int)

        # for i, n in enumerate(numbers):

        #     if target - n in mp:
        #         return [mp[target - n] + 1, i + 1]
        #     else:
        #         mp[n] = i

        # return [-1, -1]


        # binary search on the left of the array for the current element 

        for i in range(len(numbers) - 1, -1, -1):

            ele = numbers[i]
            sf = target - ele

            l, r = 0 , i - 1

            while l <= r:
                
                mid = (l + r) // 2
                if sf == numbers[mid]:
                    return [mid + 1, i + 1]
                elif sf > numbers[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return [-1, -1]
             