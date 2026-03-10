func containsDuplicate(nums []int) bool {
    slices.Sort(nums)

    for i := 0; i <len(nums)-1; i++{
        if ok := nums[i]==nums[i+1]; ok{
            return true
        }
    }
    return false
}