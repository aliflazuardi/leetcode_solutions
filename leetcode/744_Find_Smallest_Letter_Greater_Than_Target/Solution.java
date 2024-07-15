class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        int left = 0, right = letters.length - 1;

        char ans = letters[0];

        while(left <= right) {
            int mid = (left + right) / 2;

            if(letters[mid] > target) {
                right = mid - 1;
                ans = letters[mid];// satu line missing
            } else {
                left = mid + 1;
            }
        }

        return ans;
    }
}