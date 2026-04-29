class Solution(object):
    def minOperations(self, grid, x):
        arr = [v for row in grid for v in row]
        r = arr[0] % x
        for v in arr:
            if v % x != r:
                return -1
        arr.sort()
        m = arr[len(arr)//2]
        return sum(abs(v - m) // x for v in arr)