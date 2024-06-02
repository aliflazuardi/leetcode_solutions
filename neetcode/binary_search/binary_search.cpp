class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0;
        int r = nums.size() - 1;

        int m;
        while (l <= r) {
            m = l + ((r - l) / 2); 
            cout<<m<<endl;
            if (nums[m] == target) {
                return m;
            }

            if (nums[m] < target) {
                l = m + 1;
            } else {
                r = m - 1;
            }
        }

        return -1;
    }
};
