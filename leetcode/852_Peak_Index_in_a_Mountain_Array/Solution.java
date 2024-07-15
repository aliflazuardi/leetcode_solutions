class Solution {
    public int peakIndexInMountainArray(int[] arr) {
        int l = 0, r = arr.length - 1;

        int peak = 0;
        while(l <= r) {
            int mid = (l + r) / 2;

            if(isAsc(arr, mid)) {
                peak = mid;
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }

        return peak;
    }

    public boolean isAsc(int[] arr, int index) {
        if(index == 0) {
            return true;
        }

        if(arr[index] - arr[index - 1] > 0) {
            return true;
        }


        return false;
    }
}