class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        
        aux_div = 1
        while x >= 10 * aux_div:
            aux_div *= 10
            
        while x:
            
            if x // aux_div != x % 10:
                return False
            x = (x % aux_div) // 10
            aux_div = aux_div / 100
        return True