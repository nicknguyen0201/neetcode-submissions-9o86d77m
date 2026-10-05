class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr,left_ptr,mid,right_ptr):
            left_arr=arr[left_ptr:mid+1]
            right_arr=arr[mid+1:right_ptr+1]
            i,l,r=left_ptr,0,0

            while l<len(left_arr) and r<len(right_arr):
                if left_arr[l]<=right_arr[r]:
                    arr[i]=left_arr[l]
                    l+=1
                else:
                    arr[i]=right_arr[r]
                    r+=1
                i+=1

            #one is shorter than another
            while l<len(left_arr):
                arr[i]=left_arr[l]
                l+=1
                i+=1
            
            while r<len(right_arr):
                arr[i]=right_arr[r]
                r+=1
                i+=1


        def mergesort(arr,l,r):
            if l>=r:
                return
            m=l+(r-l)//2
            mergesort(arr,l,m)
            mergesort(arr,m+1,r)
            merge(arr,l,m,r)
        
        mergesort(nums,0,len(nums)-1)
        return nums
        