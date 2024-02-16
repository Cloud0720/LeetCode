class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total = 1
        check = 0
        answer = []

        for i in nums:
            if i != 0:
               total *= i 
            else:
                check += 1

        for i in nums:
            if check != 0 and i!=0 or check > 1:
                answer.append(0)
            
            elif i == 0:
                answer.append(total)
            else:
                answer.append(total/i)

        return answer

        