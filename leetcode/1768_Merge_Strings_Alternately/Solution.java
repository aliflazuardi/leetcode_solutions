class Solution {
    public String mergeAlternately(String word1, String word2) {
        String ans = "";

        int maxIndex = Math.max(word1.length(), word2.length());

        for(int i = 0; i < maxIndex; i++) {
            if(i < word1.length()){
                ans = ans + word1.charAt(i);
            }
            if(i < word2.length()){
                ans = ans + word2.charAt(i);
            }
        }

        return ans;
    }
}
