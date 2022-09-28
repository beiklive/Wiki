---
comments: true
---





# C++实现线程池

## 需求确认

实现一个线程池，需要明确一下他的功能

1. 具有创建多个线程的能力
2. 能存储任务队列
3. 取出任务队列时，使用锁机制来保证线程之间互不干扰
4. 没有分配到任务的线程要处于等待状态，减少CPU损耗
5. 程序结束时，结束所有线程的等待状态并关闭线程

额外功能：

- 控制线程池的运行与暂停
- 动态扩展和减少线程

## 代码第一版

```C++ title="ThreadPool.h"
#ifndef _BPOOL_H__
#define _BPOOL_H__

#include <thread>
#include <mutex>
#include <vector>       
#include <queue>
#include <functional>
#include <condition_variable>
class bpool
{
private:
    /* data */
    std::vector<std::thread> threads; // 储存线程池中的线程
    std::queue<std::function<void()>> tasks; // 储存任务队列
    std::mutex tasks_mtx;	// 线程锁
    std::condition_variable cv;   //条件变量，让没有任务的线程进入等待状态
    bool stop;

public:
    bpool() = delete;
    bpool(int num_threads);
    ~bpool();

    void add_task(std::function<void()> task);
};

#endif

```

```C++ title="ThreadPool.cpp"
#include "ThreadPool.h"

bpool::bpool(int num_threads) : stop(false)
{
    for (int i = 0; i < num_threads; i++)
    {
        threads.emplace_back([this](){
            while(true){
                std::function<void()> task;
                {
                    std::unique_lock<std::mutex> lock(tasks_mtx);
                    cv.wait(lock, [this](){
                        return stop || !tasks.empty();
                    });
                    if(stop && tasks.empty()) return;
                    task = tasks.front();
                    tasks.pop();
                }
                task();
            }
        });
    }
}

bpool::~bpool()
{
    {
        std::unique_lock<std::mutex> lock(tasks_mtx);
        stop = true;
    }
    cv.notify_all();  // 唤醒所有等待的线程
    for(auto &t : threads)  // 结束所有线程
        if (t.joinable())
        {
            t.join();
        }
}

void add_task(std::function<void()> task)
{
    {
        std::unique_lock<std::mutex> lock(tasks_mtx);
        if (stop)
        {
            throw std::runtime_error("bpool is stopped");
        }
        
        tasks.emplace(task);
    }
    cv.notify_one();
}
```



