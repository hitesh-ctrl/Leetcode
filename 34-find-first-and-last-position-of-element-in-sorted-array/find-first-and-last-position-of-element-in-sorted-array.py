class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def bs(x):
            lo, hi = 0, len(nums)
            while lo<hi:
                mid=(lo+hi)/2
                if nums[mid]<x:
                    lo=mid+1
                else:
                    hi=mid
            return lo
        
        lo=bs(target)
        hi=bs(target+1) - 1

        if(lo<=hi):
            return [lo,hi]
        return[-1,-1]