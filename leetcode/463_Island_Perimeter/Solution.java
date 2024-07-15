import java.util.*;

class Solution {

    Queue<Grid> q = new LinkedList<>();
    int[] dX = {-1, 0, 1, 0};
    int[] dY = {0, -1, 0, 1};
    boolean[][] visited;

    public int islandPerimeter(int[][] grid) {
        visited = new boolean[grid.length][grid[0].length];
        int cnt = 0;

        for(int i = 0; i < grid.length; i++) {
            for(int j = 0; j < grid[0].length; j++) {
                if(grid[i][j] == 1) {
                    q.add(new Grid(i, j));
                    visited[i][j] = true;
                    break;
                }
            }
        }    
        
        while(!q.isEmpty()) {
            Grid curr = q.poll();

            for(int i = 0; i < 4; i++) {
                int nextX = curr.x + dX[i];
                int nextY = curr.y + dY[i];

                if(nextX < 0 || nextX >= grid.length || nextY < 0 || nextY >= grid[0].length) {
                    cnt++;
                    continue;
                }

                if(visited[nextX][nextY])
                    continue;

                if(grid[nextX][nextY] == 0) {
                    cnt++;
                } else {
                    q.add(new Grid(nextX, nextY));
                    visited[nextX][nextY] = true;
                }
            }

    }

    return cnt;
    }
}

class Grid {
    int x;
    int y;

    Grid(int x, int y) {
        this.x = x;
        this.y = y;
    }
}