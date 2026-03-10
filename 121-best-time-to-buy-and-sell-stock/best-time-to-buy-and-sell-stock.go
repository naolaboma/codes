func maxProfit(prices []int) int {
    buyp := prices[0]
    profit := 0
    for _, v := range prices{
        buyp = min(buyp, v)
        profit = max(profit, v-buyp)
    }
    return profit

}