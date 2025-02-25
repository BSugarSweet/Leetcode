class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int left = 0;
        int right = 0;
        int ans = INT_MAX;
        int n = nums.size();
        int cur = 0;

        while(right < n){
            cur += nums[right];
            while(cur >= target){
                ans = min(right - left + 1, ans);
                cur -= nums[left];
                left++;
            }
            right++;
        }
        if(ans == INT_MAX) return 0;
        return ans;
    }
};