class Solution {
    public int findPeakElement(int[] nums) {
        int left = 0, right = nums.length - 1;

        int ans = 0;

        if(nums.length == 1) {
            return 0;
        } else if(nums.length == 2) {
            if(nums[1] > nums[0]){
                    return 1;
            } else {
                    return 0;
            }
        }

        while(left <= right) {
            int mid = (left + right) / 2;
            
            if (mid != 0 && nums[mid] > nums[mid - 1] && mid + 1 == nums.length) {
                return mid;
            } else if (nums[mid] > nums[mid + 1] && mid == 0) {
                return mid;
            } 
            if(mid - 1 >= 0 && mid + 1 < nums.length) {
                if(nums[mid] > nums[mid - 1] && nums[mid + 1] < nums[mid]) {
                    return mid;
                }
            } 
            
            if(nums[mid + 1] > nums[mid]) {
                left = mid + 1;
                continue;
            }
            
            right = mid -1 ;
            
        }

        return ans;
    }
}