class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0;
        int r = nums.size() - 1;

        while (l <= r) {
            int m = l + (r - l)/2;

            if (nums[m] == target) {
                return m;
            }

            if (nums[m] > target) {
                if (nums[l] <= target) {
                    r = r - 1;
                } else {
                    l = l + 1;
                }
            } else {
                if (nums[r] >= target) {
                    l = l + 1;
                } else {
                    r = r - 1;
                }
            }
        }

        return -1;
    }
};

