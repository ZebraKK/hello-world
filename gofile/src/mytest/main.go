package main

import (
    "fmt"
    "time"
    "math/rand"
    "sync"
)

var wg = &sync.WaitGroup{}

func main() {
    fmt.Println("go...")

    que := make(chan int, 5)

    wg.Add(1)
    product(que)
    fmt.Println("working....")

    for i:=0; i < 5; i++ {
        wg.Add(1)
        consume(que, i)
    }
    
    //time.Sleep(10*time.Second)
    wg.Wait()
    fmt.Println("end")
}

func product(que chan int) {
    go func(){
        var index int
        //now := time.Now()
        for {
            que <- index
            fmt.Println("product: ", index)
            index++
            //if time.Since(now) > time.Duration(1)* time.Second {
            //    break
            //}
            if index > 200 {
                break
            }
        }
        //time.Sleep(time.Second)
        wg.Done()
        fmt.Println("product done")
    }()

    fmt.Println("after product goroutine.....")
}

func consume(que chan int, index int) {

    defer func (){
        fmt.Println(index, "done defer defer ....")
    } ()
    
    go func(){
        defer func(){
            fmt.Println(index, " consume done  ....")
            wg.Done()
        }()

        var list []int
        for {
            timeout := false 
            var number int
            select {
            case number = <-que:
                list = append(list, number)
                r := genRandom(5, number)
                //fmt.Println("random :", r)
                fmt.Println("at No.", index , "consume:", list)
                time.Sleep(time.Duration(r)*time.Microsecond)
            case <-time.After(time.Duration(100)*time.Millisecond):
                fmt.Println("at No.", index ," timeout is ", timeout)
                timeout = true
            }
            if timeout {
                break
            }
        }
    }()

    fmt.Println("after consume", index, " goroutine.....")
}

func genRandom(max, num int) int {
    //s := rand.NewSource(time.Now().UnixNano())
    s := rand.NewSource(int64(num))
    r := rand.New(s)

    return r.Intn(max)
}