class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
                              i 
        Input: heights = [7, 1,7,2,2, 4]

           stack=[1,4]
           leftMost=.    [-1,-1,1,1,1,4]
            stack=[1]
            rightMost    [1, 6,3,6,6,6]
            maxArea=7
           for i=1->n:
            max=(maxArea,1*(2-0+1))
        """
        stack=[]
        left_bound=[-1]*len(heights)
        for i in range(len(heights)):
            while stack and heights[i]<=heights[stack[-1]]:
                stack.pop()
            if stack:
                left_bound[i]=stack[-1]
            stack.append(i)
        stack=[]
        right_bound=[len(heights)]*len(heights)
        for i in range(len(heights)-1,-1,-1):
            while stack and heights[i]<=heights[stack[-1]]:
                stack.pop()
            if stack:
                right_bound[i]=stack[-1]
            stack.append(i)
        max_area=heights[0]
        for i in range(len(heights)):
            l=left_bound[i]+1
            r=right_bound[i]-1
            max_area=max((r-l+1)*heights[i],max_area)
        return max_area

        