class Solution(object):
    def productExceptSelf(self, nums):
        # # lets make left right products differently 
        # left=[1]
        # right=[1]
        # # answer=[]
        # y=1
        # x=1
        # # making left from 0 t i-1
        # for i in range(1,len(nums)):
        #     # if i ==0:
        #     #     left.append(1)
        #     y=y*nums[i-1]
        #     left.append(y)
        # for i in range (len(nums)-2,-1,-1):
        #     x=x*nums[i+1]
        #     right.append(x)
        # for i in range(len(nums)):
        #     left[i]=left[i]*right[len(nums)-i-1]
        # return left
        output = [1] * len(nums)
        x=1
        y=1
        for i in range(len(nums)):
            output[i]=x
            x=x*nums[i]
        for i in range(len(nums)-1,-1,-1):
            output[i]*=y
            y=y*nums[i]
        return output