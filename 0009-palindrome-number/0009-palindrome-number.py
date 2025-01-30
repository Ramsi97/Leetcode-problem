class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x//10 == 0:
            return True
        x = str(x)
        l ,r= 0, len(x)-1
        while(l<r):
            if(x[r] != x[l]):
                return False
            l+=1
            r-=1
        return True
        #


        
        
        