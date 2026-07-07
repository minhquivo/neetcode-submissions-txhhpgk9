class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumMap = {}
        for i in range(len(nums)):
            if target-nums[i] not in sumMap:
                sumMap[nums[i]] = i
                continue 
            return [sumMap[target-nums[i]], i]