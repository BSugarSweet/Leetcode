class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int left = 0;
        int n = s.size();
        int right = 0;
        int ans = 0;
        unordered_set<char> char_set;
        while(right < n){
            while(char_set.find(s[right]) != char_set.end()){
                char_set.erase(s[left]);
                left++;
            }
            char_set.insert(s[right]);
            ans = max(ans, right - left + 1);
            right++;
        }
        return ans;
    }
};