class Solution:
    def trap(self, heights: List[int]) -> int:
        """
        U: return int that is max water trapped
        P:
        solve this with 2 ptr
        [0,2,0,3,   1,0,1,3,   2,1]
                          l    r
        tmp_sum = -2 
            run 2 ptr to identif gaps
            the condition to add to vol is the right bar has to be tall er or equal left bar
            if the bar next to left is taller or eq, move left bar

            add it to sum

        """
        if not heights:
            return 0

        l, r = 0, len(heights) - 1
        leftMax, rightMax = heights[l], heights[r]
        res = 0

        while l < r:
            # We move the pointer with the smaller "wall" height
            # because that wall is the bottleneck for trapped water.
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, heights[l])
                # Water trapped = current max wall - current bar height
                res += leftMax - heights[l]
            else:
                r -= 1
                rightMax = max(rightMax, heights[r])
                res += rightMax - heights[r]
                
        return res
            