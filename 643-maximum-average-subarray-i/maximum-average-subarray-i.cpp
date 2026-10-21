#include <algorithm>
class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        
        int l = nums.size();
        int sum = 0;
        for(int i =0;i<k;i++){
            sum+=nums[i];
        }

        int maxSum = sum;

        for(int i=k;i<l;i++){
            sum+=nums[i];
            sum-=nums[i-k];
            maxSum = std::max(maxSum, sum);
        }
        return (double)maxSum/k;
    }
};