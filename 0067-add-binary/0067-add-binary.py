class Solution(object):
    def addBinary(self, a, b):
        n1=len(a)
        n2=len(b)
        s=0
        i=n1-1
        j=n2-1
        carry=0
        curr=0
        output=[]
        while i>=0 or j>=0 or carry:
            x=int(a[i]) if i>-1 else 0
            y=int(b[j]) if j>-1 else 0 
            curr=(x+y+carry)
            carry=curr//2
            s=curr%2
            output.append(str(s))
            i-=1
            j-=1
        return "".join(output[::-1])
        