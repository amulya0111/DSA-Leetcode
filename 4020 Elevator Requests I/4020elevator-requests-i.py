class Solution(object):
    def elevatorRequests(self, n, requests):
        prev=0
        sum=0
        for i in range(len(requests)):
            curr=requests[i]
            if curr>prev:
                sum+=curr-prev
            else:
                sum+=prev-curr

            prev=curr
        return sum
            
            
        