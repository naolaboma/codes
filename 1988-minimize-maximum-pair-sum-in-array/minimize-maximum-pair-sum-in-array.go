func minPairSum(nums []int) int {
    slices.Sort(nums)
    l , r := 0, len(nums)-1
    maxi := 0
    for l<r{
        summ := nums[l] + nums[r]
        maxi = max(maxi, summ)
        l+=1
        r-=1
    }
    return maxi
}