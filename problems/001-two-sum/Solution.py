class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        visto = {}
        for i, num in enumerate(nums):
          complementar = target - num
          if complementar in visto:
            return [ visto[complementar], i]
          visto[num] = i