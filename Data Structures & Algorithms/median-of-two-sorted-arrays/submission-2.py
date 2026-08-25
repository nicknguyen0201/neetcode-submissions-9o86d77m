class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total=len(nums1)+len(nums2)
        half=total//2
        A=nums1
        B=nums2
        if len(B)<len(A):
            A,B=B,A
        l,r=0,len(A)-1
        while True:
            mid_a=(l+r)//2
            mid_b=half-1-mid_a-1

            a_left=A[mid_a] if mid_a>=0 else -float('inf')
            a_right=A[mid_a+1] if mid_a+1<len(A) else float('inf')
            b_left=B[mid_b] if mid_b>=0 else -float('inf')
            b_right=B[mid_b+1] if mid_b+1<len(B) else float('inf')

            if a_left<=b_right and b_left<= a_right:
                if total%2!=0:
                    return min(a_right,b_right)
                else:
                    return (min(a_right,b_right)+max(a_left,b_left))/2
            elif a_left>b_right:
                r=mid_a-1
            else:
                l=mid_a+1

            


