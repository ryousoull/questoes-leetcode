class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        visto = {}
        for i, num in enumerate(nums):
          complementar = target - num
          if complementar in visto:
            return [ visto[complementar], i]
          visto[num] = i

def calcularTotal(horas, valorHora):
    valorBruto = horas * valorHora

    if horas > 5:
        return valorBruto * 0.90

    return valorBruto


def classificarPermanencia(horas):
    if horas <= 2:
        return "CURTA"
    elif horas <= 5:
        return "MEDIA"
    else:
        return "LONGA"


def main():
    placa = input()
    horas = int(input())
    valorHora = float(input())

    total = calcularTotal(horas, valorHora)
    permanencia = classificarPermanencia(horas)

    print(f"Placa: {placa}")
    print(f"Total: {total:.2f}")
    print(f"Permanencia: {permanencia}")


main()