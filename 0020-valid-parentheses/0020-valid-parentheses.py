class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        o = ['(', '[', '{']
        c = [')', ']', '}']
        n = []

        for i in range(len(s)):
            if s[i] in o:
                n.append(s[i])
            else:
                if len(n) == 0:
                    return False
                else:
                    k = c.index(s[i])
                    if o[k] == n[-1]:
                        del n[-1]
                    else:
                        return False
        if len(n) == 0:
            return True