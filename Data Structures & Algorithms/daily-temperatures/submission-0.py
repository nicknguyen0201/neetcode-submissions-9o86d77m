class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        a monotonic stack is a always decreasing stack
        such that temp from higest is loweest, this is saying that whoever on the stack
        is waiting for a say hotter than themselves
        """
        stack=[]
        res=[0]*len(temperatures)
        for i, temp in enumerate(temperatures):
            #if empty stack or top stack is taller than current element
            if not stack or stack[-1][0]>=temp:
                stack.append((temp,i))
            else:
                # pop stack and record the higher temp for top stack element
                #the current iter temp is bigger than the top stack tmp
                while stack and stack[-1][0]<temp:
                    _,past_idx = stack.pop()
                    res[past_idx]=i - past_idx
                stack.append((temp,i))
        return res

                


