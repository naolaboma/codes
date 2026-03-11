func lengthOfLongestSubstring(s string) int {
    slice := make(map[byte]bool)
    maxi := 0
    l := 0
    for i:= 0; i <len(s); i++{
        for slice[s[i]]{
            delete(slice, s[l])
            l++
        }
        slice[s[i]] = true
        maxi = max(maxi, i - l +1)
    }
    return maxi
}