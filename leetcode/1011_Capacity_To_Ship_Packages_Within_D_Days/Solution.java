class Solution {
    public int shipWithinDays(int[] weights, int days) {
        int l = 0, r = 25000000;

        int shipCap = 25000000;
        while(l <= r) {
            int cap = (l + r) / 2;

            if(isCapacityAllowed(cap, days, weights)) {
                r = cap - 1;
                shipCap = cap;
            } else {
                l = cap + 1;
            }
        }

        return shipCap;
    }

    public boolean isCapacityAllowed(int capacity, int days, int[] weights) {
        int w = 0;
        
        for(int i = 1; i <= days; i++) {
            int todayCap = 0;
            while(w < weights.length) {
                if(todayCap + weights[w] <= capacity) {
                    todayCap = todayCap + weights[w];
                    w = w + 1;
                } else{
                    break;
                }
            }
        }

        if(w == weights.length) {
            return true;
        }

        return false;
    }
}