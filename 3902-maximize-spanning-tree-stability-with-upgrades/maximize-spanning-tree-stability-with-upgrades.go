
import (
	"math"
	"slices"
)
type unionFind struct {
	size []int
	p    []int
}

func newUnionFind(n int) unionFind {
	u := unionFind{
		size: make([]int, n),
		p:    make([]int, n),
	}
	for i := 0; i < n; i++ {
		u.p[i] = i
		u.size[i] = 1
	}
	return u
}

func (u *unionFind) find(x int) int {
	if x >= len(u.p) {
		return -1
	}
	if u.p[x] == x {
		return x
	}
	return u.find(u.p[x])
}

func (u *unionFind) union(s1, s2 int) {
	r1 := u.find(s1)
	r2 := u.find(s2)
	if r1 == r2 {
		return
	}
	if u.size[r1] > u.size[r2] {
		u.p[r2] = r1
		u.size[r1] = u.size[r1] + u.size[r2]
	} else {
		u.p[r1] = r2
		u.size[r2] = u.size[r1] + u.size[r2]
	}
}

func (u *unionFind) same(x, y int) bool {
	return u.find(x) == u.find(y)
}

func maxStability(n int, edges [][]int, k int) int {
    // sort
    slices.SortFunc(edges, func(a, b []int) int{
        if a[3] == 1 {
            return -1
        } else if b[3] == 1 {
            return 1
        } else if a[3] == 1 && b[3] == 1 {
            return 0
        } else {
            if a[2] < b[2] {
                return 1
            } else if a[2] > b[2] {
                return -1
            } else {
                return 0
            }
        }
    })
    // init union find
    un := newUnionFind(n)

    // kruskal

    strengths := make([]int, 0, len(edges))
    cycle := false
    musts := 0

    for i := 0; i < len(edges); i++ {
        u := edges[i][0]
        v := edges[i][1]
        s := edges[i][2]
        must := edges[i][3]
        if must == 1 {
            if un.same(u, v) {
                cycle = true
                break // cycle found
            }
            un.union(u, v)
            strengths = append(strengths, s)
            musts++
        } else {
            if !un.same(u, v) {
                un.union(u, v)
                strengths = append(strengths, s)
            }
        }
    }

    if cycle { // no cycles
        return -1
    }

    p := un.find(0)
    for i := 1; i < n ; i++ { // everything connected
        if un.find(i) != p {
            return -1
        }
    }

    min := math.MaxInt
    upgrades := 0
    for i := len(strengths)-1; i >= 0; i-- {
        s := strengths[i]
        if i >= musts && upgrades < k {
            s = s*2
            upgrades++
        }
        if min > s {
            min = s
        }
    }
    return min
}