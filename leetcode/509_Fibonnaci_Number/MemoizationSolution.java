class MemoizationSolution {
    int[] memo = new int[31];

    public int fib(int n) { 
        if(n == 0)
            return n;

        if(memo[n] != 0)
            return memo[n];
        if(n == 1 || n == 2) {
            memo[n] = 1;
            return 1;
        }
        
        int result = fib(n-1) + fib(n-2);
        memo[n] = result;
        return result;
    }
}