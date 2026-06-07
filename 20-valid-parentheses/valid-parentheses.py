class Solution(object):
    def isValid(self, s):
        stack=[]
        #initially we will make a dictionary to keep opening and closing brackets check
        dic = {')':'(','}':'{',']':'['}
        #char will refer to the key
        for char in s:
            if char in dic: #if the char we got is a parenthesis
            #if )}] is there but stack is empty or the last added is not the value of the key:
                if not stack or stack[-1] != dic[char]:
                    return False
                stack.pop()
            #now open brackets check 
            else:
                stack.append(char)
        if stack:
            return False
        return True        