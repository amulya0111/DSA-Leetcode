class Solution(object):
    def uniqueLetterString(self, s):
        n = len(s)
        last = {}
        prev = {}
        ans = 0

        for i in range(n):
            ch = s[i]

            p = last.get(ch, -1)
            q = prev.get(ch, -1)

            ans += (i - p) * (p - q)

            prev[ch] = p
            last[ch] = i

        for ch in last:
            ans += (n - last[ch]) * (last[ch] - prev[ch])

        return ans