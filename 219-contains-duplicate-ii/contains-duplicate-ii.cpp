class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int> windowMap;
        for (int i = 0;i<nums.size();i++){
            if(windowMap.count(nums[i])){
                if(i-windowMap[nums[i]]<=k){
                    return true;
                }
            }
            windowMap[nums[i]] = i; 
            
        
        }
    return false;
    }
};