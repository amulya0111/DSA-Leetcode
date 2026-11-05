class Solution:
    def isSubsetSum(self, n, arr, target):
        # write your code here
        def find(ind,arr,target):
            if ind==0:
                if arr[ind]==target:
                    return True
                else:
                    return False
            if arr[ind]>target:
                return False
            pick = arr[ind]+find(ind-1,arr,target-arr[ind])
            notpick=find(ind-1,arr,target)
            return pick or notpick
        return find(n-1,arr,target)