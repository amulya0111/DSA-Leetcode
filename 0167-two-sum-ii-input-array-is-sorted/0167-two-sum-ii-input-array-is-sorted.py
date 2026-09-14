class Solution(object):
    def twoSum(self, numbers, target):
    
        for i in range(len(numbers)):
            search=target-numbers[i]
            l=i+1
            r=len(numbers)-1
            while l<=r:
                mid=(l+r)//2
                if search<numbers[mid]:
                    r=mid-1
                elif search>numbers[mid]:
                    l=mid+1
                elif search==numbers[mid]:
                    return [i+1,mid+1]
                