class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = []
        s = s.lower()

        for i in range(len(s)):
            if s[i].isalnum():
                n.append(str(s[i]))
            else:
                pass
    
        n2 = list(reversed(n))

        if n2 == n:
            return True
        else:
            return False