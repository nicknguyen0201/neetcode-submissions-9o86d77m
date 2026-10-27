"""
stack = [5, 7, 5, 7, 4, 5]

everytime we increment counter, we also push to stack

hash map num -> cnt

max heap
(- cnt, - insertion order, num)


"""
class FreqStack:

    def __init__(self):
        self.frequency = defaultdict(int)
        self.frequency_stacks = defaultdict(list)
        self.max_count=0

    def push(self, val: int) -> None:
        self.frequency[val] += 1
        count = self.frequency[val]
        if count>self.max_count:
            self.max_count += 1
        self.frequency_stacks[count].append(val)
       
    def pop(self) -> int:
        res = self.frequency_stacks[self.max_count].pop()
        if len(self.frequency_stacks[self.max_count]) == 0:
            self.max_count -= 1
        self.frequency[res] -= 1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()