class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmaps = set()
        for num in nums:
            if num not in hashmaps:
                hashmaps.add(num)
            else:
                return True
        return False