class RecentCounter(object):
    '''
    count no. od recent requests , initialised 0
    '''
    def __init__(self):
        self.queue=[]

    def ping(self, t):
        #t=time of adding request, return no. of requests happened
        if len(self.queue)==0 or self.queue[0]>=(t-3000):
            self.queue.append(t)
        else:
            while self.queue[0]<(t-3000):
                self.queue.pop(0)
                if len(self.queue)==0:
                    break
            self.queue.append(t)
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)