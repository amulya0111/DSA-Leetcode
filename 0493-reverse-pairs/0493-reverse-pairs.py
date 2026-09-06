class Solution(object):
    def reversePairs(self, nums):
        def mergesort(left,right):
            if right-left<=1:
                return 0
            mid = (left+right)//2
            count= mergesort(left,mid)
            count+=mergesort(mid,right)
            j=mid
            for i in range(left,mid):
                while j<right and nums[i]>2*nums[j]:
                    j+=1
                count += j-mid

            temp=[]
            i=left
            j=mid
            while i<mid and j<right:
                if nums[i]<=nums[j]:
                    temp.append(nums[i])
                    i+=1
                else:
                    temp.append(nums[j])
                    j+=1
            temp.extend(nums[i:mid])
            temp.extend(nums[j:right])
            nums[left:right]=temp
            return count
        return mergesort(0,len(nums))
                    

            
