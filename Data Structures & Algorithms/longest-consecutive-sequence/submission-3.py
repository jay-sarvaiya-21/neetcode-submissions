class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # 2 20 4 10 3  4 5

        0 -1

        visit = set()
        res = 0
        for num in nums:
            visit.add(num)

        for num in nums:
            if num - 1 not in visit:
                length = 1
                val = num + 1
                while val in visit:
                    length += 1
                    val += 1
                res = max(res,length)

        return res

        