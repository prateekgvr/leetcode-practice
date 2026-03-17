class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        original :int =x 
        rem : int = 0
        while x > 0:
            rem = rem*10 + x%10
            x= x//10
        
        if rem == original: 
            return True
        else:
            return False
