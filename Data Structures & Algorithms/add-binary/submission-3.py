class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        overview
        add bin that comes in str
        what happen when there's carry
        01 carry=1
        01
        11

        Plan:
        while loop
        look at the end, add them, carry if needed

        Pseudo code
        Input: a = "10010", b = "00111"
        """

        n, m = len(a), len(b)
        if n > m: #4 >3
            diff = n - m
            b = diff*'0' + b
        elif n < m: #4 >3
            diff = m - n
            a = diff*'0' + a
        print(a)
        print(b)
        result =[]
        carry = 0
        for i in range(max(n,m)-1,-1,-1):
            if a[i] == b[i] =='1':
                if carry == 1:
                    result.append('1')
                else:
                    result.append('0')
                carry = 1
        
            elif a[i] =='1':
                if carry == 1:
                    result.append('0')
                    carry=1
                else:
                    result.append('1')
                    carry=0
               
            elif b[i] =='1':
                if carry == 1:
                    result.append('0')
                    carry=1
                else:
                    result.append('1')
                    carry=0
            else:
                if carry == 1:
                    result.append('1')
                else:
                    result.append('0')
                carry=0
        if carry == 1:
            result.append('1')
        result.reverse()
        return ''.join(result)