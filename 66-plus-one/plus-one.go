func plusOne(digits []int) []int {
    c := 1
    for i := len(digits)-1; i > -1; i--{
        digits[i] += 1
        c = 0
        if digits[i] > 9{
            c = 1
            digits[i] = 0
        } else{
            return digits
        }
    }
    if c == 1 {
        return append([]int{1}, digits...)
    }
    return nil
}