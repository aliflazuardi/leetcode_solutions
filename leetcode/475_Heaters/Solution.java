class Solution {
    public int findRadius(int[] houses, int[] heaters) {
        int l = 0, r = Integer.MAX_VALUE;

        int ans = 0;
        Arrays.sort(houses);
        Arrays.sort(heaters);

        while(l <=  r) {
            int rad = (l + r)/2;

            boolean isValid = false;

            int i = 0, j = 0;

            while(i < houses.length && j < heaters.length) {
                int heater = heaters[j];
                if(houses[i] >= heater - rad && houses[i] <= heater + rad) {
                    i = i + 1;
                } else {
                    j = j + 1;
                }
            }

            if(i >= houses.length) {
                isValid = true;
            }

            if(isValid) {
                ans = rad;
                r = rad - 1;
            } else {
                l = rad + 1;
            }
        }

        return ans;
    }
}