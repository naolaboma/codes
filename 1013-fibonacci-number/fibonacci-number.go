func fib(n int) int {
    if n == 0{
        return 0
    }
    memo := make([]int, n+1)
    return sol(n, memo)
}

func sol(n int, memo []int) int{
    if memo[n] != 0{
        return memo[n]
    } 
    if n == 1 || n == 2{
        memo[n] = 1
    } else {
        memo[n] = sol(n - 1, memo) + sol(n - 2, memo)
    }
    return memo[n]
}