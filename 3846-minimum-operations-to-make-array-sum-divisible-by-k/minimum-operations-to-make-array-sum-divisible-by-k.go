func minOperations(nums []int, k int) int {
    summ := 0
    for _, v := range nums{
        summ+= v
    }
    return summ%k
}