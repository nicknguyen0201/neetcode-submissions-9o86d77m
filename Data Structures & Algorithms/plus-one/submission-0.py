class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        need to implement some sort of carry over function

         9 9 9 +1
        9+1 % 10 =0
        9+1 /10 =1 carry over
        """
        carry=False
        
        if (digits[-1] + 1 ) %10 ==0:

            carry=True
        else:
            digits[-1]+=1
            return digits

        i=len(digits)-1
        while carry and i>=0:
            if (digits[i] + 1 ) %10 ==0:
                digits[i]=0
            else:
                digits[i]+=1
                carry=False
            i-=1
        if carry:
            digits.insert(0,1)
            
        return digits

            
