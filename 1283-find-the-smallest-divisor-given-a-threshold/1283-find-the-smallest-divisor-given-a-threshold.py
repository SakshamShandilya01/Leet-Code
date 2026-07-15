class Solution(object):
    def smallestDivisor(self, nums, threshold):

        low = 1
        high = max(nums)

        while(low <= high):

            mid = (low + high) // 2

            total = 0

            for i in range(len(nums)):
                total += (nums[i] + mid - 1) // mid

            if(total <= threshold):
                high = mid - 1
            else:
                low = mid + 1

        return low