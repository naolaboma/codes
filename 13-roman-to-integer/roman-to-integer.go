func romanToInt(s string) int {
    c := map[rune]int {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    total := 0
    for i :=0; i < len(s); i++{
        curr := c[rune(s[i])]
        n := 0
        if i < len(s)-1{
            n = c[rune(s[i+1])]
        }
        if curr < n{
            total += n - curr
            i++
        } else {
            total += curr
        }
    }
    return total
}