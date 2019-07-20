package mygrpool

import "sync"


/*
 *  原包，是pool中的worker把自己加入到dispatcher 的workerpool channel中
 *  此处为什么要多做这个动作呢。这个实现，worker起来后，就一起到jobQueue channel中获取。
 */

type Pool struct {
	JobQueue chan Job
	WorkerPool map[int]*worker
	Stop chan struct{}
}

type PoolMgr struct {
	Dispatcher *dispatcher
	Pool *Pool
	wg  sync.WaitGroup
}


func NewPool(numWorkers int, jobQueueLen int) *Pool {
	jobQueue := make(chan Job, jobQueueLen)
	//workerPool := make(chan *worker, numWorkers)

	workerPool := make(map[int]*worker, numWorkers)

	pool = &Pool {
		JobQueue: make(chan Job, jobQueueLen),
		workerPool: make(map[int]*worker, numWorkers),
	}

	_, err := newDispatcher(pool.JobQueue, numWorkers)
	if err != nil {
		return nil
	}

	return pool
}



type dispatcher struct {
	JobQueue chan Job
	WorkerQueue chan int
	Stop chan struct{}
}

func newDispatch(jobQueue chan Job, size int) (*dispatcher, error) {
	if p == nil {
		return errors.New("")
	}

	d := &dispatcher {
		JobQueue: jobQueue,
		WorkerQueue: make(chan int, size),
		Stop: make(chan struct{}),
	}

    //go worker
	for i := 0; i < size; i++ {
		w := newWorker(i)
		w.start()
		d.WorkerQueue <- i        	//worker的分发，是排队拿任务，worker完成了任务，把自己再贡献出来
									//为什么不是，直接n个worker从 jobqueue拿去做好了？
	}

	//go dispatcher
	d.dispatch()

	return d, nil
}


//拿 worker 
//拿 job
func (d *dispatcher) dispatch() {
	go func () {
		for {
			select {
			case:
			case:
			}
		}	
	}()

	go func () {
		
	}()
}

type worker struct {
	CacheJob chan Job     //worker 需要有自己的 chan么？ 可以公用 dispathcer的 queue么。线程安全？随机拿取么
	Index int
	Stop chan struct{}
	Todo chan struct{}    //标志自己可以继续做下一份job
}

func newWorker(index int) *worker {
	w := &worker{
		CacheJob: make(chan Job),
		Index: index,
		Stop: make(chan struct{}),
	}
	return w
}

func (w *worker) start() {
	go func(){
		for {                           // for循环形式，不用单次执行完，重新起，go开销
			select {
			case job <-w.CacheJob:
				job()
				w.Todo <- struct {}{}
			case <-w.Stop:
				w.Stop <- struct{}{}  //todo 自己加入 防止其他人来操作
				return
			}
		}
		}()
}


