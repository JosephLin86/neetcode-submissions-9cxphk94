class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first, last = 0, len(nums)-1
        while first <=last:
            between = (first + last) // 2
            if nums[between] < target:
                first = between+1
            elif nums[between] > target:
                last = between-1
            else:
                return between
        return -1