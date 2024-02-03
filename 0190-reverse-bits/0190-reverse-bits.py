class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        a = list(bin(n))[2:]
        a.reverse()
        a = ''.join(a)
        b = '0'*(32-len(a))
        a = '0b'+a+b
        a = int(a,2)
        return a


