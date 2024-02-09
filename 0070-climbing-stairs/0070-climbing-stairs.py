class Solution(object):
        
        
    def climbStairs(self, n):
        
        def fact(a):
            if(a > 1):
                return a * fact(a - 1)
            else:
                return 1
    
        def fact2(a,b):
        
            if a == 0:
                return 1
            else:
                k = b
                for _ in range(a-1):
                    k-=1
                    b*=k
                return b

        """
        :type n: int
        :rtype: int
        """
        b = n/2
        a = n%2
        sum = 0

        if a == 1:
            b+=1
           
        while b != n+1:
            sum += fact2(a,b)/fact(a)
            b+=1
            a+=2

        return sum


            


        