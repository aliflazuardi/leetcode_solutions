class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> groups;

        for (auto& s : strs) {
            vector<int> count(26, 0);
            for (char c : s) {
                count[c - 'a']++;
            }

            string key;
            for (int i : count) {
                key += "#" + to_string(i);
            }

            groups[key].push_back(s);
        }

        vector<vector<string>> ans;
        for (auto& group : groups) {
            ans.push_back(group.second);
        }

        return ans;
    }
};
