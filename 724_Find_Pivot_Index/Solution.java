class Solution {
    public int pivotIndex(int[] nums) {
        int[] prefixSum = new int[nums.length];
        prefixSum[0] = nums[0];

        for(int i = 1; i < prefixSum.length; i ++){
            prefixSum[i] = prefixSum[i - 1] + nums[i];
        }

        if(prefixSum[prefixSum.length - 1] - prefixSum[0] == 0) {
            return 0;
        }

        for(int i = 1; i < prefixSum.length-1; i++) {
            if(prefixSum[i-1] == prefixSum[prefixSum.length - 1] - prefixSum[i]) {
                return i;
            }
        }
        
        if(prefixSum[prefixSum.length - 2] == 0) {
            return prefixSum.length - 1;
        }


        return -1;
    }
}