class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        """
        sort
        do 1 pass from left to right
       
        """
  
        good=set()
        for triplet in triplets:
            if triplet[0]>target[0] or triplet[1]>target[1] or triplet[2]>target[2]:
                continue
            for t in range(3):
                if triplet[t]==target[t] and t not in good:
                    good.add(t)
            if len(good)==3:
                return True
        return len(good)==3
