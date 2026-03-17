import "sort"

func largestSubmatrix(grid [][]int) int {
    rows := len(grid)
    cols := len(grid[0])
    maxArea := 0

    for r := 0; r < rows; r++ {

        // Build height histogram
        for c := 0; c < cols; c++ {
            if grid[r][c] == 1 && r > 0 {
                grid[r][c] += grid[r-1][c]
            }
        }

        // Copy and sort heights
        heights := make([]int, cols)
        copy(heights, grid[r])
        sort.Ints(heights)

        // Compute area
        for i := cols - 1; i >= 0; i-- {
            width := cols - i
            area := heights[i] * width
            if area > maxArea {
                maxArea = area
            }
        }
    }

    return maxArea
}