class Solution:
    def minimumDistance(self, nums):
        from collections import defaultdict
        pos = defaultdict(list)
        for i, v in enumerate(nums):
            pos[v].append(i)
        ans = float('inf')
        for v in pos:
            p = pos[v]
            if len(p) >= 3:
                for i in range(len(p) - 2):
                    ans = min(ans, p[i+2] - p[i])
        return -1 if ans == float('inf') else ans * 2