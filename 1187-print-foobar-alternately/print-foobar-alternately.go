type FooBar struct {
	n int
    fooTurn chan struct{}
    barTurn chan struct{}
}

func NewFooBar(n int) *FooBar {
	fb := &FooBar{
		n:       n,
		fooTurn: make(chan struct{}, 1),
		barTurn: make(chan struct{}, 1),
	}

	fb.fooTurn <- struct{}{} //prints first foo

	return fb
}

func (fb *FooBar) Foo(printFoo func()) {
	for i := 0; i < fb.n; i++ {
        <-fb.fooTurn
		// printFoo() outputs "foo". Do not change or remove this line.
        printFoo()
        fb.barTurn <- struct{}{}

	}
}

func (fb *FooBar) Bar(printBar func()) {
	for i := 0; i < fb.n; i++ {
        <-fb.barTurn
		// printBar() outputs "bar". Do not change or remove this line.
        printBar()
        fb.fooTurn <- struct{}{}
	}
}