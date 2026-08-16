class Solution(object):
    def nearestDrone(self, drones, target):
        min_dis=float('inf')
        min_i=-1
        a=0
        for i in range(len(drones)):
            curr_dis=abs(drones[i][0]-target[0])+abs(drones[i][1]-target[1])
            if curr_dis<=drones[i][2] and curr_dis<min_dis:
                min_dis=curr_dis
                min_i=i
        return min_i
                