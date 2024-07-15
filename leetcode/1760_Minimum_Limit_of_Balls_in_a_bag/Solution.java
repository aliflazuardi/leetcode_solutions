class Solution {
    public int minimumSize(int[] nums, int maxOperations) {
        int penalty = 0;
        int left = 1;
        int right = 1000000000;

        while(left <= right) {
            int mid = left + (right - left) / 2;
            int cnt = 0;

            for(int i = 0; i < nums.length; i++) {
                cnt += (nums[i] - 1) / mid;
            }

            if(cnt <= maxOperations) {
                penalty = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return penalty;
    }
}