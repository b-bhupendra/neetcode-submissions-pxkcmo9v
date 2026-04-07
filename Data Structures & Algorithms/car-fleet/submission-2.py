class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        iters = target
        n = len(position)

        fleet = [ [ position[i], speed[i] , ( (target - position[i]) / speed[i] )] for i in range(n) ]

        fleet = sorted(fleet,reverse=True)
        print(fleet)
        ans = len(fleet)

        for i in range(1, len(fleet)):
            if fleet[i - 1][2] >= fleet[i][2]:
                fleet[i][2] = fleet[i - 1][2]
                ans -= 1

        return ans