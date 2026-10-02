from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
      
      stack = deque()
      pares = {
      "(": ")",
      "[": "]",
      "{": "}"
      }
      
      for char in s:
        if char in pares:
          stack.append(char)
        else:
          if not stack:
            return False
          
          abertura = stack.pop()
          if pares[abertura] != char:
            return False
            
            
      return len(stack) == 0