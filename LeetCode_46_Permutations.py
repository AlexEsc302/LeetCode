class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        perm = []
        ans = []

        def backtracking():
            if len(perm) == n:
                ans.append(perm[:])
                return

            for x in nums:
                if x not in perm:
                    perm.append(x)
                    backtracking()
                    perm.pop()

        backtracking()
        return ans
