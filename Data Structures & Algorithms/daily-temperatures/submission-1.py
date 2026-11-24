class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """

        use monotonic stack, keep track on strictly increasing 
        stack [ 30(0), 38(1)]

        plan
        keep an empty res array size temp
        keep tuple in stack
        stack has to always inc
        if the condition violated, pop stack

        pseudo code
        
        stack = []
        res = [0]*len(temperatures)
        for temp in temperatures:
            
            while temp> stack top:
                pop
                res[index]=new index - index 

        """
        stack = []
        res = [0]*len(temperatures)
        for i,temp in enumerate(temperatures):
            if not stack:
                stack.append((temp,i))
                continue

            while stack and temp > stack[-1][0]:
                past_temp, past_day_index = stack.pop()
                res[past_day_index]= i - past_day_index
            stack.append((temp,i))
        return res





