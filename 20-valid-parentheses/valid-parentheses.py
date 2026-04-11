class Solution(object):
    def isValid(self, s):
        stack=[]
        #initially we will make a dictionary to keep opening and closing brackets check
        dic = {')':'(','}':'{',']':'['}
        #char will refer to the key
        for char in s:
            if char in dic:
                if stack:
                    peek=stack.pop()
                    #check if the popped element was the opening bracket for the closing key or not - '('=')'?
                    if dic[char]!=peek:
                        return False
                else:
                    return False
            #now open brackets check 
            else:
                stack.append(char)
        if stack:
            return False
        return True


        