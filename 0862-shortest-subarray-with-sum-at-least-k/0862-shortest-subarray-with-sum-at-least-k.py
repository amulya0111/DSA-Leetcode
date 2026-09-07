class Solution(object):
    def shortestSubarray(self, nums, k):
        prefix=[0]
        for num in nums:
            prefix.append(prefix[-1]+num)
        dequeue=[]
        result=float('inf')
        for i in range(len(prefix)):
            while dequeue and prefix[i]-prefix[dequeue[0]]>=k:
                result=min(result,i-dequeue[0])
                dequeue.pop(0)
            while dequeue and prefix[i] <= prefix[dequeue[-1]]:
                dequeue.pop()
            dequeue.append(i)  
        if result == float('inf'):
            return -1
        else:
            return result  
