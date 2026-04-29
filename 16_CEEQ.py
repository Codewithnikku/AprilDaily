class Solution(object):
    def solveQueries(self, nums, queries):
        n = len(nums)
        
        pos = {}
        for i in range(n):
            if nums[i] not in pos:
                pos[nums[i]] = []
            pos[nums[i]].append(i)
        
        def lower_bound(arr, target):
            l, r = 0, len(arr)
            while l < r:
                m = (l + r) // 2
                if arr[m] < target:
                    l = m + 1
                else:
                    r = m
            return l
        
        def dist(a, b):
            d = abs(a - b)
            return d if d < n - d else n - d
        
        res = []
        
        for q in queries:
            indices = pos[nums[q]]
            
            if len(indices) == 1:
                res.append(-1)
                continue
            
            i = lower_bound(indices, q)
            
            prev_idx = indices[i - 1] if i > 0 else indices[-1]
            next_idx = indices[i + 1] if i < len(indices) - 1 else indices[0]
            
            d1 = dist(q, prev_idx)
            d2 = dist(q, next_idx)
            
            res.append(d1 if d1 < d2 else d2)
        
        return res