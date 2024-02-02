class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        answer = [0,0]
        for i in range(len(nums)):
            if target -  nums[i] in nums and i!= nums.index(target - nums[i]):
                answer[0] = i
                answer[1] = nums.index(target - nums[i])
                
        return sorted(answer)



        