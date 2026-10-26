class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        """
        len(nums)=3
              0 1 2 3 4 5 6 
        nums=[1,2,3,4,5,6,1]
                          i
        i=1
        
        """
        i=0
        while i<len(nums):
            if nums[i]==i+1: #value 1 at index 0, value 2 at index 1
                i+=1
            elif nums[i]>len(nums):
                i+=1
            elif nums[i]<=0:
                i+=1
            else:# nums[i]<=len(nums):
                #prevent infinite loop
                index=nums[i]-1
                if nums[i]!=nums[index]:
                    nums[index],nums[i]=nums[i],nums[index]
                else:
                    i+=1
        for i in range(len(nums)):
            if nums[i]!=i+1: #nums[0]!=1, nums[len(nums)-1]!=len(nums)
                return i+1# return 1

        return len(nums)+1