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
   //my_slice() 
   //my_map()
     my_json()
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
    myslice := []int{2:20}
    fmt.Println("cap : ", cap(myslice))

    for i, value := range myslice {
        fmt.Println("myslice, i:", i, " value:", value)
    }
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
