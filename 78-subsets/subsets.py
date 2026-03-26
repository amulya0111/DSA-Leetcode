class Solution(object):
    def subsets(self, nums):
        result=[] #we will append the result found in last index here 
        path=[]
        def backtrack(index,path):
            #base case
            if index==len(nums):
                result.append(path[:])
                return result 
            #include 
            path.append(nums[index])
            backtrack(index+1,path)
            #pop
            path.pop()
            backtrack(index+1,path)
        backtrack(0,[])
        return result