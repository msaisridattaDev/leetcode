################3#############
class Solution:
    def getVal(self, c):
        if c == 'A': return 0
        if c == 'C': return 1
        if c == 'G': return 2
        return 3

    def findRepeatedDnaSequences(self, s):
        n = len(s)
        cnt = defaultdict(int)
        ans = []
        
        dnaHash = 0
        POWN1 = 4 ** 9
        for i in range(n):
            dnaHash = dnaHash * 4 + self.getVal(s[i])
            if i >= 9:
                cnt[dnaHash] += 1
                if cnt[dnaHash] == 2:
                    ans.append(s[i-9:i+1])

                dnaHash -= POWN1 * self.getVal(s[i-9])

        return ans