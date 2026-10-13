class Solution:
	def prevSmaller(self, arr):
		# code here
		stack=[]
		n=len(arr)
		ans=[-1]*n
		for i in range(n):
	        while stack and stack[-1] >= arr[i]:
	            stack.pop()
            
            ans[i]=stack[-1] if stack else -1
	        stack.append(arr[i])
	    return ans 
   
		  