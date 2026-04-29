class Solution(object):
    def minimumHammingDistance(self, source, target, allowedSwaps):
        """
        :type source: List[int]
        :type target: List[int]
        :type allowedSwaps: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        n = len(source)
        parent = list(range(n))
        for x, y in allowedSwaps:
            union(x, y)

        groups = defaultdict(list)
        for i in range(n):
            groups[find(i)].append(i)

        ans = 0
        for group in groups.values():
            count = defaultdict(int)
            for i in group:
                count[source[i]] += 1
            for i in group:
                if count[target[i]] > 0:
                    count[target[i]] -= 1
                else:
                    ans += 1

        return ans