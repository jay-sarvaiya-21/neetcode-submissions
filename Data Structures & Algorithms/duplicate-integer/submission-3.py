class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = set()
        for ele in nums:
            if ele not in seen:
                seen.add(ele)
            else:
                return True
        return False
        