class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        totalpetrol=0
        totaldist=0
        currrange=0
        start=0
        n=len(gas)
        for i in range(n):
            totalpetrol+=gas[i]
            totaldist+=cost[i]
            currrange+=gas[i]-cost[i]
            if currrange<0:
                start=i+1
                currrange=0
        if totalpetrol<totaldist:
            return -1
        return start