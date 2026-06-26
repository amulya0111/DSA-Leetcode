from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        queue = deque()
        result=[]
        if k==1:
            return nums
        for i in range(len(nums)):
            while queue and queue[0] < i - k + 1:
                queue.popleft()
            if len(queue)==0:
                queue.append(i)
            else:
                while len(queue)>0:
                    if nums[queue[-1]]<nums[i]:
                        queue.pop()
                    else:
                        break
                queue.append(i)
            if i>=k-1:
                result.append(nums[queue[0]])
        return result
                 
