class Solution(object):
    def closestTarget(self, words, target, startIndex):
        n = len(words)
        min_distance = float('inf')

        for i in range(n):
            if words[i] == target:
                d = abs(i - startIndex)
                circular_dist = min(d, n - d)
                min_distance = min(min_distance, circular_dist)

        return min_distance if min_distance != float('inf') else -1