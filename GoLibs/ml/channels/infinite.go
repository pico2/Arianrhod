package channels

import (
    "ml/array"
    . "fmt"
    "sync"
    "time"
)

func unused() {
    _ = Fprintln
    _ = time.Second
}

type InfiniteChannel struct {
    input   chan interface{}
    output  chan interface{}
    buffer  array.Array
    cond    *sync.Cond
}

func NewInfiniteChannel() *InfiniteChannel {
    ch := &InfiniteChannel{
                input   : make(chan interface{}),
                output  : make(chan interface{}),
                buffer  : *array.NewArray(),
                cond    : sync.NewCond(&sync.Mutex{}),
        }

    go ch.infiniteBuffer()
    return ch
}

func (self *InfiniteChannel) In() chan <- interface{} {
    return self.input
}

func (self *InfiniteChannel) Out() <-chan interface{} {
    return self.output
}

func (self *InfiniteChannel) Length() int {
    return self.buffer.Length()
}

func (self *InfiniteChannel) Close() {
    close(self.input)
    self.cond.L.Lock()
    defer self.cond.L.Unlock()
    self.cond.Wait()
}

func (self *InfiniteChannel) shutdown() {

FLUSH:
    for _, v := range (self.buffer) {
        select {
            case self.output <- v:

            default:
                break FLUSH
        }
    }

    close(self.output)
}

func (self *InfiniteChannel) infiniteBuffer() {

INFINITE_LOOP:
    for {
        switch self.buffer.Length() {
            case 0:
                select {
                    case elem, open := <-self.input:
                        if open == false {
                            break INFINITE_LOOP
                        }
                        self.buffer.Append(elem)

                    default:
                }

            default:
                select {
                    case elem, open := <-self.input:
                        if open == false {
                            break INFINITE_LOOP
                        }
                        self.buffer.Append(elem)

                    case self.output <- self.buffer.Peek(0):
                        self.buffer.Pop(0)
                }
        }
    }

    self.shutdown()
    self.cond.Broadcast()
}
