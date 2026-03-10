func containsDuplicate(nums []int) bool {
    seen := make(map[int]int)

    for _, v := range nums{
        if seen[v] == 0{
            seen[v] += 1
        } else{
            return true
        }
    }
    return false
}