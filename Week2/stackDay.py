# 232 Implementing queue using stack
# use two stacks in and out

# 225 Implement stack using queues
# use two queues use one another for storage
class MyStack(object):

    def __init__(self):
        self.queue1 = []
        self.queue2 = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue1.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        ans = self.queue1.pop(0)
        while self.queue2:
            self.queue1.append(self.queue2.pop(0))
        return ans

    def top(self):
        """
        :rtype: int
        """
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        ans = self.queue1[0]
        self.queue2.append(self.queue1.pop(0))
        while self.queue2:
            self.queue1.append(self.queue2.pop(0))
        return ans
        

    def empty(self):
        """
        :rtype: bool
        """
        return not (self.queue1 or self.queue2)
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

# 20 Valid Parentheses
# use stack for matching characters

# 1047 Remove all adjacent duplicates in string
# use stack to cancel out duplicates

# 150 Evaluate reverse Polish Notation
# use stack
# careful with - and /
# return int(num2 / num1) if num2 * num1 > 0 else -(abs(num2) // abs(num1))
