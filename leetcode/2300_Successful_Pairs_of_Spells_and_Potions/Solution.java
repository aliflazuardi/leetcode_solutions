class Solution {
    public int[] successfulPairs(int[] spells, int[] potions, long success) {
        Arrays.sort(potions);

        int[] ans = new int[spells.length];
        for(int i = 0; i < spells.length; i++) {
            int l = 0, r = potions.length - 1;
            
            int minIdx = -99;
            while(l <= r) {
                int mid = (l + r) / 2;

                if((long)spells[i] * potions[mid] >= success) {
                    minIdx = mid;
                    r = mid - 1;
                } else {
                    l = mid + 1;
                }
            }

            if(minIdx == -99) {
                ans[i] = 0;
            } else {
                ans[i] = potions.length - minIdx;
            }
        }

        return ans;
    }
}