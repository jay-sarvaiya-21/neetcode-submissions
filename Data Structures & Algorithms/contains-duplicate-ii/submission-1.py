class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        l, r = 0, 0
        seen = set()
        if k == 0: return False
        for r in range(len(nums)):
            if r - l <= k:
                if nums[r] in seen:
                    return True
            if r - l >= k:
                seen.remove(nums[l])
                l += 1
            seen.add(nums[r])
        return False
        