class Solution(object):
    def shipWithinDays(self, weights, days):
        # find ship capacity 
        def possible(capacity):
            day=1
            weight=0
            for i in range(len(weights)):
                if (weight+weights[i])<=capacity:
                    weight+=weights[i]
                    
                else:
                    day+=1
                    weight=weights[i]
                
            return day
        l=max(weights)
        h=sum(weights)
        while l<h:
            capacity=(l+h)//2
            if possible(capacity)<=days:
                h=capacity
                
            else:
                l=capacity+1
        return l
        
                 