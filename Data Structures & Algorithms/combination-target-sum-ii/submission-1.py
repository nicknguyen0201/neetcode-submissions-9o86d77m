class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        n=len(candidates)
        candidates.sort()
        def BT(start, path, sum):
            
            if sum==target: 
                res.append(path[:])
                return 
            if start == n or sum>target:
                return 
            num=candidates[start]
            path.append(num)
            BT(start+1,path, sum+num)
            path.pop()

            while (start+1<n and candidates[start]==candidates[start+1]):
                start+=1
                

            BT(start+1,path,sum)
            

                
        BT(0,[],0)
        return res