class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        livre = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[livre-1]:
                nums[livre] = nums[i]
                livre+=1
        return livre