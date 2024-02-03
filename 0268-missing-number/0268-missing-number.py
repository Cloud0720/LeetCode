class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = -1
        m = max(nums)
        
        for i in range(m + 1):
            if i not in nums:
                a = i

        if a == -1:
            a = m+1
        return a


            
        