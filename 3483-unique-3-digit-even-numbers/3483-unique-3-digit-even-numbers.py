class Solution(object):
    def totalNumbers(self, digits):
        count=[0]*10
        for digit in digits:
            count[digit]+=1
        ans=0
        for i in range(1, 10):
            if count[i] == 0:
                continue

            count[i] -= 1

            for j in range(10):
                if count[j] == 0:
                    continue

                count[j] -= 1

                for k in range(0, 10, 2):
                    if count[k] > 0:
                        ans += 1

                count[j] += 1

            count[i] += 1
        return ans