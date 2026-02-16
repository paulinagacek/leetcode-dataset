class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_map<int, int> m;
        int res = 0, prev, next;
        for (auto num : nums) {
            if (m.find(num) == m.end()) {
                prev = m.find(num-1) != m.end() ? m[num-1] : 0;
                next = m.find(num+1) != m.end() ? m[num+1] : 0;
                m[num] += prev + next + 1;
                m[num-prev] = m[num];
                m[num+next] = m[num];
                res = max(res, m[num]);
            }
        }
        return res;
    }
};
