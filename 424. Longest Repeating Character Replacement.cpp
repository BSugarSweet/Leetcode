class Solution {
public:
    int characterReplacement(string s, int k) {
        int left = 0;
        int right = 0;
        int ans = 0;
        int max_freq = 0;
        int n = s.size();
        unordered_map<char, int> m;
        while(right < n){
            m[s[right]]++;
            max_freq = max(max_freq, m[s[right]]);
            if((right - left + 1 - max_freq) > k){
                m[s[left]]--;
                left++;
            }
            ans = max(ans, right - left + 1);
            right++;
        }
        return ans;
    }
};