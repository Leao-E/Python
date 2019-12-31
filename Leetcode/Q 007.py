class Solution:
    def reverse(self, x: int) -> int:
        aux = abs(x)
        rev = 0
        while aux!=0:
            rev = rev*10 + aux%10
            aux = aux//10           
        if x < 0 and -rev >= -2**31:
            return -rev
        elif(rev <= (2**31)-1):
            return rev
        else:
            return 0
        