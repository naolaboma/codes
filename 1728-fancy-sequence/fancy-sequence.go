type Fancy struct {
    raw  []int64
    mult int64
    add  int64
}

const MOD int64 = 1000000007

func modPow(a, b int64) int64 {
    res := int64(1)
    a %= MOD

    for b > 0 {
        if b&1 == 1 {
            res = (res * a) % MOD
        }
        a = (a * a) % MOD
        b >>= 1
    }

    return res
}

func modInv(x int64) int64 {
    return modPow(x, MOD-2)
}

func Constructor() Fancy {
    return Fancy{[]int64{}, 1, 0}
}

func (f *Fancy) Append(val int) {

    base := (int64(val) - f.add) % MOD
    base = (base + MOD) % MOD

    base = (base * modInv(f.mult)) % MOD

    f.raw = append(f.raw, base)
}

func (f *Fancy) AddAll(inc int) {
    f.add = (f.add + int64(inc)) % MOD
}

func (f *Fancy) MultAll(m int) {
    f.mult = (f.mult * int64(m)) % MOD
    f.add = (f.add * int64(m)) % MOD
}

func (f *Fancy) GetIndex(idx int) int {

    if idx >= len(f.raw) {
        return -1
    }

    val := (f.raw[idx]*f.mult + f.add) % MOD
    return int(val)
}