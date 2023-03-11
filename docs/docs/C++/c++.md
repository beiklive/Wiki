---
comments: true
---






## std::unique_lock

unique_lock类里维护了一个mutex对象。在unique_lock类拥有多个构造函数，这里只放两个本文涉及的构造函数。

```c
explicit unique_lock(mutex_type& __m)
: _M_device(std::__addressof(__m)), _M_owns(false)
{
	lock();
	_M_owns = true;
}

```

该构造函数会直接对mutex对象加锁。

```c
      unique_lock(mutex_type& __m, defer_lock_t) noexcept
      : _M_device(std::__addressof(__m)), _M_owns(false)
      { }

```

这个构造函数不进行加锁操作。其中第二个参数defer_lock_t是一个空类。



在unique_lock类的析构函数里，对mutex对象进行了解锁操作。

```c
~unique_lock()
{
	if (_M_owns)
	unlock();
}

```

### 使用方法一

手动加解锁。直接看代码。

```c
// unique_lock::lock/unlock
#include <iostream>       // std::cout
#include <thread>         // std::thread
#include <mutex>          // std::mutex, std::unique_lock, std::defer_lock

std::mutex mtx;           // mutex for critical section

void print_thread_id (int id) {
  std::unique_lock<std::mutex> lck (mtx,std::defer_lock);
  // critical section (exclusive access to std::cout signaled by locking lck):
  lck.lock();
  std::cout << "thread #" << id << '\n';
  lck.unlock();
}

int main ()
{
  std::thread threads[10];
  // spawn 10 threads:
  for (int i=0; i<10; ++i)
    threads[i] = std::thread(print_thread_id,i+1);

  for (auto& th : threads) th.join();

  return 0;
}
```

需要注意的是，这里要加std::defer_lock参数。这样会调用第二个构造函数，不对mutex进行加锁操作。后面由自己手动操作。好处是可以自己选择需要加解锁的代码段。

### 使用方法二

这里做了一些改动，让unique_lock在构造时加锁，析构时解锁。为了确定需要加解锁的代码段，我们用{}花括号把代码段括起来。

```c
// unique_lock::lock/unlock
#include <iostream>       // std::cout
#include <thread>         // std::thread
#include <mutex>          // std::mutex, std::unique_lock, std::defer_lock

std::mutex mtx;           // mutex for critical section

void print_thread_id (int id) {
  
  // critical section (exclusive access to std::cout signaled by locking lck):
  
  {
  	std::unique_lock<std::mutex> lck (mtx);
  	std::cout << "thread #" << id << '\n';
  }
 
}

int main ()
{
  std::thread threads[10];
  // spawn 10 threads:
  for (int i=0; i<10; ++i)
    threads[i] = std::thread(print_thread_id,i+1);

  for (auto& th : threads) th.join();

  return 0;
}

```

## std::condition_variable

条件变量提供了两类操作：wait和notify。这两类操作构成了多线程同步的基础。

使用条件变量可以在任务队列为空时CPU暂停轮询减少耗费CPU资源。

### wait

wait是线程的等待动作，直到其它线程将其唤醒后，才会继续往下执行。

```c
std::mutex mutex;
std::condition_variable cv;

// 条件变量与临界区有关，用来获取和释放一个锁，因此通常会和mutex联用。
std::unique_lock lock(mutex);
// 此处会释放lock，然后在cv上等待，直到其它线程通过cv.notify_xxx来唤醒当前线程，cv被唤醒后会再次对lock进行上锁，然后wait函数才会返回。
// wait返回后可以安全的使用mutex保护的临界区内的数据。此时mutex仍为上锁状态
cv.wait(lock)
```

需要注意的一点是, wait有时会在没有任何线程调用notify的情况下返回，这种情况就是有名的[**spurious wakeup**](https://docs.microsoft.com/zh-cn/windows/desktop/api/synchapi/nf-synchapi-sleepconditionvariablecs)。因此**当wait返回时，你需要再次检查wait的前置条件是否满足**，如果不满足则需要再次wait。wait提供了重载的版本，用于提供前置检查。

```c
template <typename Predicate>
void wait(unique_lock<mutex> &lock, Predicate pred) {
    while(!pred()) {
        wait(lock);
    }
}
```

### notify

了解了wait，notify就简单多了：唤醒wait在该条件变量上的线程。notify有两个版本：notify_one和notify_all。

- notify_one 唤醒等待的一个线程，注意只唤醒一个。
- notify_all 唤醒所有等待的线程。使用该函数时应避免出现[惊群效应](https://blog.csdn.net/lyztyycode/article/details/78648798?locationNum=6&fps=1)。

```c
std::mutex mutex;
std::condition_variable cv;

std::unique_lock lock(mutex);
// 所有等待在cv变量上的线程都会被唤醒。但直到lock释放了mutex，被唤醒的线程才会从wait返回。
cv.notify_all(lock)
```



## 程序通信

进程是系统资源分配的基本单位。

线程是进程的子任务，是CPU调度的最小单位，共享同一片地址空间。

### 进程间通信

1. 管道： 数据是单向的，相互通信需要创建两个管道。无格式的字节流数据。
2. 消息队列：内核中，内存中的消息链表， 
3. 共享内存： 映射一块内存空间到相同的物理空间，进程之间对数据都可见。
4. 信号量： PV操作，
5. 信号： SIGNAL()   异步通信
6. socket： 不同主机间的进程通信

### 线程间通信

1. 互斥量
2. 信号量
3. 临界区： 多线程串行化访问公共资源
4. 等待通知时间
