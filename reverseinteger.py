class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x<0 else 1
        num = abs(x)
        rev:int =0

        while num > 0:
            digit = num % 10
            rev = rev * 10 + digit
            num = num // 10

        return sign * rev
