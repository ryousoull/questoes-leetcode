class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s)).lower()
        
        i = 0
        j = len(s)
        
        while i < j:
            if s[i] != s[j - 1 - i]:
                return False
            i+=1
            
        return True
        
        
# or: 
#     s = "".join(filter(str.isalnum, s)).lower()
#     return s == s[::-1]

