class Solution(object):
    def peakIndexInMountainArray(self, arr):
        start=1
        end=len(arr)-2
        while start<=end:
            mid=(start+end)/2
            if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                return mid
            elif arr[mid]>arr[mid-1] and arr[mid]<arr[mid+1]:
                start=mid+1              
            else:
                end=mid-1
                
            