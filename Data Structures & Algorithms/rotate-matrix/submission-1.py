class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        l,r =0,len(m)-1
        while l<r:
            top,bot=l,r
            for i in range(r-l):
                top_left=m[top][l+i]
                #bot left to top left
                m[top][l+i] = m[bot-i][l]
                #bot right to bot left
                m[bot-i][l]=m[bot][r-i]
                #top right to bot right
                m[bot][r-i] = m[top+i][r]
                #topleft to top tight
                m[top+i][r]=top_left
            l+=1
            r-=1