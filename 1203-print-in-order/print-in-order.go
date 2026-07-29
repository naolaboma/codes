type Foo struct {
    firstDone chan struct{}
    secondDone chan struct{}

}

func NewFoo() *Foo {
	return &Foo{
        firstDone: make(chan struct{}, 1),
        secondDone: make(chan struct{}, 1),
	}
}

func (f *Foo) First(printFirst func()) {
	// Do not change this line
	printFirst()
    f.firstDone <- struct{}{}
}

func (f *Foo) Second(printSecond func()) {
	/// Do not change this line
    <-f.firstDone
	printSecond()

    f.secondDone <- struct{}{}

}

func (f *Foo) Third(printThird func()) {
	// Do not change this line
    <-f.secondDone
	printThird()
}