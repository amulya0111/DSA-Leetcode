class Solution(object):
    def productExceptSelf(self, nums):
        # lets make left right products differently 
        left=[]
        right=[]
        answer=[]
        y=1
        x=1
        # making left from 0 t i-1
        for i in range(len(nums)):
            if i ==0:
                left.append(1)
            else:
                y=y*nums[i-1]
                left.append(y)
        for i in range (len(nums)-1,-1,-1):
            if i ==len(nums)-1:
                right.append(1)
            else:
                x=x*nums[i+1]
                right.append(x)
        for i in range(len(nums)):
            answer.append(left[i]*right[len(nums)-i-1])
        return answer
            