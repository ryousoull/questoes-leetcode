class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        janela = set()
        inicio = 0
        maior = 0
        
        for fim, caractere in enumerate(s):
            while caractere in janela:
                janela.remove(s[inicio])
                inicio+=1
            janela.add(caractere)
            maior = max(maior,fim - inicio + 1)
            
        return maior