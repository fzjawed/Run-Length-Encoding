class Solution:
    def solve(self, s):
        counter = 1
        result = ''
        prevLetter = s[0]
        if len(s) == 1:
            return str(1)+s[0]
        for i in range(1,len(s),1):
            if s[i] != prevLetter:
                result += str(counter) + s[i-1]
                prevLetter = s[i]
                counter = 1
            else:
                counter += 1
            if i == len(s)-1:
                result += str(counter) + s[i]
        return result
        