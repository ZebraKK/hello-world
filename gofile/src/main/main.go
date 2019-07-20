package main

import (
	"fmt"
    "time"
    "sync"
    "errors"
    "encoding/json"
//	"log"
//	"net/http"
)

func main() {
   my_slice() 
   //my_map()
   //my_json()
   //insert_slice()
}

func insert_slice() {
    ss := []int{1,2,3,4,5,6,7,8,9}

    tmpS := append([]int{}, ss[5:]...)// 新申请了
    fmt.Println("tail:", tmpS)

    fmt.Println("do: ", append(ss[:5], 66))
    fmt.Println("ss: ", ss)
    fmt.Println("tmps:", tmpS)
    fmt.Println("last:", append(ss[:6], tmpS[:]...))

}

type Thello struct {
   Code string
   Err  error
}

func fillvalue(m map[string]Thello) {
     m["first"]=Thello{Code:"One", Err:errors.New("no.1")}
     return
}

func my_json() {
   mymap := make(map[string]Thello, 0)
   fillvalue(mymap)
  fmt.Println(mymap) 
   b, _:= json.Marshal(mymap)
   mystring := string(b)
   fmt.Println(mystring)
}
func my_map() {
    //   mymap := map[int]int{}
    a := [...]int{9:1}
    p := &a 
    fmt.Println(a)
    fmt.Println(*p)
}

func my_slice() {
    //myslice := []int{2:20}
    //fmt.Println("cap : ", cap(myslice))

    //for i, value := range myslice {
    //    fmt.Println("myslice, i:", i, " value:", value)
    //}

    myslice := []int{1,2,3,4,5,6,7,8,9,0}
    a_slice := myslice[:5]
    b_slice := append([]int{}, myslice[:5]...)
    fmt.Println("b_slice: ", append(b_slice, 6666))
    fmt.Println("myslice t:", append(myslice[0:0], 999))
    fmt.Println("myslice b:", myslice)
    fmt.Println("a_slice: ", append(a_slice, 6666))
    fmt.Println("myslice a:", myslice)
}

func my_goroutine() {
/*
	resp, err := http.Get("http://www.baidu.com")
	if err != nil {
		log.Println(err)
	}

	defer resp.Body.Close()

	headers := resp.Header

	for k, v := range headers {
		fmt.Printf("key: %v, value: %v \n", k, v)
	}
*/
	fmt.Println("hello world")

    var wg sync.WaitGroup
    printIndex := func(index int, wg *sync.WaitGroup) {
                        time.Sleep(1*time.Second)
                        fmt.Println("running : ", index)
                        wg.Done()
                    }

    for i:=0; i < 10; i++ {
        wg.Add(1)
        go printIndex(i,&wg)
        fmt.Println("in loop, go index", i)
   } 

    done := make(chan bool)
    go func() {
        fmt.Println("front wait")
        wg.Wait()
        fmt.Println("behind wait")
        done <-true
    }()

    ticker := time.NewTicker(14*time.Second)
    select {
    case <-done:
        fmt.Println("got from channel done")
    case <-ticker.C:
        fmt.Println("ticker 10 s")
    }

    fmt.Println("hello hello world")
}
