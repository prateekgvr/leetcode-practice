class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start = 0
        end = 0
        def get_index(i1:int, i2:int):
            while i1>=0 and i2 <len(s) and s[i1]==s[i2]:
                i1-=1
                i2+=1
            return (i1+1,i2-1)

        for i in range(len(s)):
            l1,r1 = get_index(i,i)
            if r1-l1> end -start: 
             start, end = l1,r1
            
            l2,r2 = get_index(i,i+1)
            if r2-l2>end- start:
                start, end = l2, r2
            
        return s[start: end+1]
