class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        UNderstand:
        building the cartesian product
        P:
        take a number fro the digits
        make for loop
        loop thru all possible char of that digit
        do BT on the next digits
        """
        n=len(digits)
        if not digits:
            return []
        mp={
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z'],
        }
        res=[]

        def BT(start, path):
            if start==n:
                res.append("".join(path))
                return 

            digit=digits[start]#3
            for c in mp[digit]:#[d e f]
                path.append(c)
                BT(start+1, path)
                path.pop()
        BT(0,[])
        return res
            

