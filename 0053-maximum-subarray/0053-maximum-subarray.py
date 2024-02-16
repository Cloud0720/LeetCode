class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        M = current_sum = nums[0]

        
        for i in range(1,len(nums)):
            next_sum = current_sum + nums[i]
            current_sum = max(next_sum, nums[i])
            M = max(current_sum, M)
      
       
        return M
        