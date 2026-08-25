class Solution(object):
    def reverseWords(self, s):
        arr=list(s)
        # Remove leading and trailing spaces
        while arr and arr[0] == ' ':
            arr.pop(0)

        while arr and arr[-1] == ' ':
            arr.pop()
        i = 1
        while i < len(arr):
            if arr[i] == ' ' and arr[i-1] == ' ':
                arr.pop(i)
            else:
                i += 1
            
        l=0
        r=len(arr)-1

        while l<r:
            arr[l],arr[r]=arr[r],arr[l]
            l+=1
            r-=1
        l=0
        for i in range(len(arr)+1):
            if i == len(arr) or arr[i]==' ':
                #reverse the current word
                arr[l:i]=arr[l:i][::-1]
                #move to next word 
                l=i+1
        ans="".join(arr)
        return ans
        