type ZeroEvenOdd struct {
	n        int
    zeroTurn chan struct{}
    EvenTurn chan struct{}
    OddTurn chan struct{}
}

func NewZeroEvenOdd(n int) *ZeroEvenOdd {
	zeo := &ZeroEvenOdd{
		n:        n,
        zeroTurn: make(chan struct{}, 1),
        EvenTurn: make(chan struct{}, 1),
        OddTurn: make(chan struct{}, 1),
	}

    zeo.zeroTurn <- struct{}{}
	return zeo
}

func (z *ZeroEvenOdd) Zero(printNumber func(int)) {
    for i:=1; i <= z.n; i++{
        <-z.zeroTurn

        printNumber(0)
        
        if i%2 == 1{
            z.OddTurn <- struct{}{}
        } else{
            z.EvenTurn <- struct{}{}
        }
    }
    
}

func (z *ZeroEvenOdd) Even(printNumber func(int)) {
    for i:=2; i <= z.n; i+=2{
        <-z.EvenTurn

        printNumber(i)

        if i < z.n {
            z.zeroTurn <- struct{}{}
        }
    }
    
}

func (z *ZeroEvenOdd) Odd(printNumber func(int)) {
    for i:=1; i <= z.n; i+=2{
        <-z.OddTurn

        printNumber(i)

        z.zeroTurn <- struct{}{}
    }
}