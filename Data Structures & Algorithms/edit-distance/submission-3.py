from functools import cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def BT(i,j):
            if j>=len(word2):
                return len(word1)-i
            #guard on i>=len word1, auto insert the rest
            if i >=len(word1):
                return len(word2)-j

            if word1[i]==word2[j]:
                return BT(i+1,j+1)
            # insert is i, j+1 because you insert a matching char before i, and thus j get to move one, but you stll
            #need to somehow take care of the char was at i that you bumbed ahead
            return 1+ min(BT(i+1,j+1), BT(i,j+1), BT(i+1,j))
        return BT(0,0)