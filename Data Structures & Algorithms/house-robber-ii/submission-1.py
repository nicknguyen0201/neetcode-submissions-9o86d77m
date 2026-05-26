class Solution:
    def rob(self, nums: List[int]) -> int:
        #rob[house i-2],rob[i-1]
        r_2,r_1= 0,0
        if not nums:
            return 0
        if(len(nums)==1):
            return nums[0]

        for i in range(1,len(nums)):
            num=nums[i]
            tmp = max(r_2+num, r_1)
            r_2=r_1
            r_1 = tmp
        
        x_2,x_1 =0,0
        for i in range(0,len(nums)-1):
            num = nums[i]
            tmp = max(x_2+num, x_1)
            x_2=x_1
            x_1 = tmp
        return max(r_1,x_1)