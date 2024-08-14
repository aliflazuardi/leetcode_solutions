class TimeMap {
private:
    unordered_map<string, vector<pair<int, string>>> store;
public:
    TimeMap() {}
    
    void set(string key, string value, int timestamp) {
        store[key].push_back({timestamp, value})
    }
    
    string get(string key, int timestamp) {
        auto& values = store[key];
        int l = 0;
        int r = values.size() - 1;

        string res = "";

        while(l <= r) {
            int mid = l + (r - l) / 2;

            if (values[m].first <= timestamp) {
                res = values[m].second;
                l = m + 1;
            } else {
                r = m - 1;
            }
        }

        return res;
    }
};

