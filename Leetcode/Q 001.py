class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lidos = {}
        for x in range(0, len(nums)):
            if((target-nums[x]) in lidos.keys()):
                return [x, lidos.get(target-nums[x])]
            lidos[nums[x]] = x