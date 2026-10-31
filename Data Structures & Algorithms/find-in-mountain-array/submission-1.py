class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        """
            Input: mountainArr = [2,4,5,2,1], target = 2

            [1, 2, 3, 4, 2, 1] 2
             l        r
        """
        def bin_search(l,r, ascending):
            while l<=r:
                m = l + (r-l) // 2
                mid_val = mountainArr.get(m)
                if mid_val == target:
                    return m
                elif mid_val > target:
                    if ascending:
                        r = m - 1
                    else:
                        l = m + 1
                else:
                    if ascending:
                        l = m + 1
                    else:
                        r = m - 1
            return -1

        def find_peak():
            l, r = 0, n - 1
            while l <= r:
                m = l + (r-l) //2
                left_val, mid_val, right_val = mountainArr.get(m-1), mountainArr.get(m), mountainArr.get(m+1)

                if left_val < mid_val > right_val:
                    return m
                elif left_val < mid_val < right_val:
                    l = m + 1
                else: 
                    r = m - 1
            return -1
        peak = find_peak()
        res = bin_search(0, peak, True)
        if res != -1:
            return res
        res = bin_search(peak, n-1, False)
        return res if res != -1 else -1
