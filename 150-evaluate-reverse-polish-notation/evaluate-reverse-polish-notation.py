class Solution(object):
    def evalRPN(self, tokens):
        stack=[]
        op=['+','-','/','*']
        for n in tokens:
            if n in op:
                y=stack.pop()
                x=stack.pop()
                if n=='+':
                    stack.append(x+y)
                elif n=='-':
                    stack.append(x-y)
                elif n=='*':
                    stack.append(x*y)
                elif n=='/':
                    stack.append(int(float(x) / y))
            else:
                stack.append(int(n))
        return stack[-1]

        