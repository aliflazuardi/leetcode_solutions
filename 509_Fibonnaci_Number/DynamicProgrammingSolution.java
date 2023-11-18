public class DynamicProgrammingSolution {
    int[] memo;

    public int fib(int n) { 
        if(n == 0)
            return 0;

        memo = new int[n+1];

        memo[1] = 1;

        for(int i = 2; i <= n; i++) {
            memo[i] = memo[i-1] + memo[i-2];
        }
  
        return memo[n];
    }
}
