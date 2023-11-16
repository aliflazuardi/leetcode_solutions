import java.util.*;

class Solution {
    public int findCircleNum(int[][] isConnected) {

        int n = isConnected.length;

        int[] parent = new int[n];

        for(int i = 0; i < n; i++) {
            parent[i] = i;
        }

        for(int i = 0; i < isConnected.length; i++) {
            for(int j = 0; j < isConnected[0].length; j++) {
                if(isConnected[i][j] == 1) {
                    union(parent, i, j);
                }
            }
        }

        int cnt = 0;

        for(int i = 0; i < n; i++) {
            if(parent[i] == i) {
                cnt++;
            }
        }


        return cnt;
    }
    
    public int find(int[] parent, int x) {
        if(parent[x] == x) {
            return x;
        }

        return parent[x] = find(parent, parent[x]);
    }

    public void union(int[] parent, int x, int y) {
        int xParent = find(parent, x);
        int yParent = find(parent, y);

        if(xParent != yParent) {
            parent[yParent] = xParent;
        }
    }
}