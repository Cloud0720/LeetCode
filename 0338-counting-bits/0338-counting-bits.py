class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = []
        for i in range(n+1):
            sum = bin(i).count('1')
            ans.append(sum)
        return ans

        