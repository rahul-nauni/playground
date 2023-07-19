from collections import defaultdict
class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        if len(time) < 2:
            return 0
        
        pairs = 0
        remainders = defaultdict(int)
        for t in time:
            remainder = t % 60
            if not remainder:
                pairs += remainders[0] # 60 - remainder is the key
            else:
                pairs += remainders[60 - remainder]
            remainders[remainder] += 1
        print(remainders)
        return pairs

s = Solution()
time = [30,20,150,100,40]
print(s.numPairsDivisibleBy60(time))