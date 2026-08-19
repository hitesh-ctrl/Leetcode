class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res=[]
        for i,a in enumerate(nums):
            if i>0 and nums[i-1] == a:
                continue
            l, r = i+1, len(nums)-1
            while l<r:
                sum = a+nums[l]+nums[r]
                if sum<0:
                    l+=1
                elif sum>0:
                    r-=1
                else:
                    res.append([a, nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
                     
        return res            
                      
            
