class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums: return 0
        aux = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[aux], nums[i] = nums[i], nums[aux]
                aux += 1
        return aux