class Solution(object):
    def maxDepth(self, s):
        left=0
        maxi=0
        for i in range(len(s)):
            if s[i]=='(':            
                left+=1    
                maxi = max(maxi,left)
            elif s[i]==')':
                left-=1
            else:
                pass
        return maxi
# s1=Solution()
# print(s1.maxDepth("(1+2(3*(4*3))+(5-2))"))
# print(s1.maxDepth("()()()"))


