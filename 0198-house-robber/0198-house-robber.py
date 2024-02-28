class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        odd,eve=0,0
        for i in nums:
            temp=max(i+odd,eve)
            odd=eve
            eve=temp
        return eve
        