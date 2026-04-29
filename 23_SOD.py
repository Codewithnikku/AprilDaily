class Solution(object):
    def distance(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import defaultdict
        d = defaultdict(list)
        for i, num in enumerate(nums):
            d[num].append(i)

        res = [0] * len(nums)
        for num, indices in d.items():
            prefix_sum = [0]
            for i in indices:
                prefix_sum.append(prefix_sum[-1] + i)

            for i, idx in enumerate(indices):
                left_count = i
                right_count = len(indices) - i - 1
                left_sum = prefix_sum[i]
                right_sum = prefix_sum[-1] - prefix_sum[i + 1]

                res[idx] = idx * left_count - left_sum + right_sum - idx * right_count

        return res