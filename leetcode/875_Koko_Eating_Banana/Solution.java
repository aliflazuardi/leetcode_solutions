class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int l = 1, r = Integer.MAX_VALUE;

        int ans = 0;
        int k = 0;

        if(piles.length == 1) {
            return (int)Math.ceil((double) piles[0] / h);
        }

        while(l <= r) {
            k = l + ((r - l)/ 2);

            boolean isValid = false;
            int idx = 0;

            int i = 0;

            while(i <= h) {
                if(piles[idx] <= k) {
                    i = i + 1;
                } else {
                    i = i + (int) Math.ceil((double) piles[idx] / k);                  
                }
                if(i > h) {
                    break;
                } else {
                    idx = idx + 1;
                }

                if(idx == piles.length) {
                    isValid = true;
                    break;
                }
            }

            if(isValid) {
                r = k - 1;
                ans = k;
            } else {
                l = k + 1;
            }
        }
        
        return ans;
    }
}