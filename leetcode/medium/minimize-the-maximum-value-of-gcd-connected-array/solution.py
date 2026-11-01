class Solution(object):
    def minimumMaxValue(self, n, index, value):
        """
        :type n: int
        :type index: int
        :type value: int
        :rtype: int
        """
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a
        if n>1 and value==1:
            return -1
        nums=[-1]*n
        nums[index]=value
        for i in range(index,len(nums)-1):
            x=nums[i]
            d=2
            ans=float('inf')
            while d*d<=x:
                if x%d==0:
                    ans=min(ans,(x//d+1)*d)
                    while x%d==0:
                        x//=d
                d+=1
            if x>1:
                ans=min(ans,(nums[i]//x+1)*x)
            nums[i+1]=ans
        for i in range(index,0,-1):
            x=nums[i]
            d=2
            ans=0
            while d*d<=x:
                if x%d==0:
                    ans=min(ans,((x-1)//d)*d)
                    while x%d==0:
                        x//=d
                d+=1
            if x>1:
                ans=max(ans,((nums[i]-1)//x)*x)
            if ans==0:
                return -1
            nums[i-1]=ans
            