func maxProfit(prices []int) int {
    var profit int
    lowest := 10000
    
    for i := range prices {
        if prices[i] < lowest {
            lowest = prices[i]
        }
        if profit < (prices[i] - lowest) {
            profit = prices[i] - lowest
        }
    }
    return profit
}