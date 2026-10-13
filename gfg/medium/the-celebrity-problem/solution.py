class Solution:
    def celebrity(self, mat):
        # create a stack with all indices (celebs)
        stack=[]
        n=len(mat)
        for i in range(n):
            stack.append(i)
        # until s has atleast 1 element (to compare a , b) pop both and check and append accordingly 
        while len(stack)>1:
            a=stack.pop()
            b=stack.pop()
            # if a knows b, a can't be the celeb
            if mat[a][b]==1:
                stack.append(b)
            # else if ==0 b knows a and b cant be the celebrity 
            else:
                stack.append(a)
        # if stack got empty , we dont have a candidate
        if not stack:
            return -1
        # else: check if the last candidate we found is a celebrity or not  
        candidate=stack.pop()
        for i in range(n):
            # ofcourse the candidate knows himself , so check others only 
            if i!=candidate:
                # if celeb knows anyone , return -1
                if mat[candidate][i]== 1 or mat[i][candidate]==0:
                    return -1
                    
        return candidate 