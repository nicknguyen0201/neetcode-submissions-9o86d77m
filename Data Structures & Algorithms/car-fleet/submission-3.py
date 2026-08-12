class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        [1,4]
        [3,2]
        tar=10

        time car 1 get to target = (10-1)//3 = 3 hr
        time car 2 get to target = (10-4)//2 = 3hr
        => 1 fleet

        plan
        car with reach to tar >=another care is in the same fleet
        
        I can have an adj list but it will be n^2 because we need to repeatedly traverse key where >= another arrival time

        [7,4,1,0]
        [1,2,2,1]
        t=10
        stack[3,4.5,10]
        """
        stack=[]
        pairs =[(p,s) for p,s in zip(position,speed)]
        pairs.sort(reverse=True)
        for p,s in pairs:
            
            stack.append((target-p)/s)#append arrival time
           
            if len(stack)>=2 and stack[-2]>=stack[-1]:# new car get get to target faster but got blocked by prev car
                stack.pop()
        return len(stack)

