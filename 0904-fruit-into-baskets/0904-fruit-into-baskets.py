class Solution(object):
    def totalFruit(self, fruits):
        l=0
        r=0
        twounique=[]
        count={}
        maxlen=0
        while l<=r and r<len(fruits):
            
            count[fruits[r]]=count.setdefault(fruits[r],0)+1
            if fruits[r] not in twounique:
                twounique.append(fruits[r])
               
            while len(twounique)>2:
                count[fruits[l]]-=1
           
                if count[fruits[l]]==0:
                    twounique.remove(fruits[l])
                l+=1
            maxlen=max(maxlen,r-l+1)

            r+=1
        return maxlen
    
            