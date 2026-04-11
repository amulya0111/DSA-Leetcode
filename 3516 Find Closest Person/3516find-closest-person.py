class Solution:
    def findClosest(self,x,y,z):
        if(abs(x-z) > abs(y-z)):
            return 2
        elif(abs(x-z) < abs(y-z)):
            return 1
        elif(abs(x-z) == abs(y-z)):
            return 0
# x = int(input(""))
# y = int(input(""))
# z = int(input(""))
# answer= Solution()
# result = answer.findClosest(x,y,z)
# print(result)
       
        