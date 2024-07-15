class Solution {
    public int largestAltitude(int[] gain) {
        int[] altitudes = new int[gain.length + 1];

        int highest = 0;
        altitudes[0] = 0;

        for(int i = 0; i < gain.length; i++) {
            altitudes[i + 1] = altitudes[i] + gain[i];
            if(altitudes[i + 1] > highest) {
                highest = altitudes[i + 1];
            }
        }
        
        return highest;
    }
}