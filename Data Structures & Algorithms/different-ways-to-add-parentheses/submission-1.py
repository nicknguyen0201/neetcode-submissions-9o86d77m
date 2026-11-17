class Solution:
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y
    }
    def diffWaysToCompute(self, expression: str) -> List[int]:
        res = []
        left, right = 0, len(expression)-1
        for i in range(len(expression)):
            op = expression[i]
            if op in self.operations:
                result_array1 = self.diffWaysToCompute(expression[:i])
                result_array2 = self.diffWaysToCompute(expression[i+1:])

                #multiply each element of 2 lists
                for x in result_array1:
                    for y in result_array2:
                        res.append(self.operations[op](x,y))
                    
        if len(res) == 0:
            return [int(expression)]
        return res
       



