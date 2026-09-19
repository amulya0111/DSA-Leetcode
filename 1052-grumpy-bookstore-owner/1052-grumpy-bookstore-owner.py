class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        already=0
        for i in range(len(grumpy)):
            if grumpy[i]==0:
                already+=customers[i]
            
        # we have our already satisfied now 
        # now lets see how my extras we can add up
        maxsave=0
        save=0
        for i in range(minutes):
            if grumpy[i]==1:
                save+=customers[i]
        maxsave=max(save,maxsave)
        # initial max save is calculated 
        # now slide window
        l=0
        r=minutes
        while r<len(grumpy):
            if grumpy[l]==1:
                save-=customers[l]
            l+=1
            if grumpy[r]==1:
                save+=customers[r]                
            r+=1
            maxsave=max(maxsave,save)
        return maxsave+already


