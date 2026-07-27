class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        how would you deal with being lower than 1 neighbor but higher than the other
        
        [1 2 3 4 3 2]
        left pass check if I am > than left neighbor
        [1 2 3 4 1 1]
        right pass check if I am > than right neighbor
        [1 2 3 4 2 1] 
        """
        nums=[1]*len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i-1]<ratings[i]:
                nums[i]=nums[i-1]+1
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i+1]< ratings[i]:
                nums[i]=max(nums[i], nums[i+1]+1)
        return sum(nums)