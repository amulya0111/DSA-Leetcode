class Solution(object):
    def maxChunksToSorted(self, arr):
        chunks=0
        k=0
        maxi=0
        for i in range(len(arr)):
            maxi=max(maxi,arr[i])
            if maxi==i:
                chunks+=1
        return chunks
        