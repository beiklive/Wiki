![5](img/5.jpg)





# makefile项目模板地址
> [https://github.com/beiklive/Linux_CPP_Template](https://github.com/beiklive/Linux_CPP_Template)

# Linux安装高版本gcc,g++
## 添加相应的源
```bash
sudo add-apt-repository ppa:ubuntu-toolchain-r/test
```
## 更新软件源
```bash
sudo apt-get update
```
## 安装
```bash
sudo apt-get install gcc-11 g++-11
```

# TCP
> Server
```c
#include<stdio.h>
#include<string.h>    
#include<stdlib.h>    
#include<sys/socket.h>
#include<arpa/inet.h> 
#include<unistd.h>    
#include<pthread.h> 
 
void *connection_handler(void *socket_desc)
{
    //Get the socket descriptor
    int sock = *(int*)socket_desc;
    int read_size;
    char *message , client_message[2000];
     
    //Receive a message from client
    while( (read_size = recv(sock , client_message , 2000 , 0)) > 0 )
    {
        //Send the message back to client
        write(sock , client_message , strlen(client_message));
    }
     
    if(read_size == 0)
    {
        puts("Client disconnected");
        fflush(stdout);
    }
    else if(read_size == -1)
    {
        perror("recv failed");
    }
         
    //Free the socket pointer
    free(socket_desc);
     
    return 0;
}
 
int main(int argc , char *argv[])
{
    int socket_desc , new_socket , c , *new_sock;
    struct sockaddr_in server , client;
    char *message;
     
    //Create socket
    socket_desc = socket(AF_INET , SOCK_STREAM , 0);
    //Prepare the sockaddr_in structure
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = INADDR_ANY;
    server.sin_port = htons( 2000 );
     
    //Bind
    if( bind(socket_desc,(struct sockaddr *)&server , sizeof(server)) < 0)
    {
        puts("bind failed");
        return 1;
    }
    puts("bind done");
     
    //Listen
    listen(socket_desc , 3);

    puts("Waiting for incoming connections...");
    c = sizeof(struct sockaddr_in);
    while( (new_socket = accept(socket_desc, (struct sockaddr *)&client, (socklen_t*)&c)) )
    {
        puts("Connection accepted");
         

        message = "Hello Client , This is server\n";
        write(new_socket , message , strlen(message));
         
        pthread_t sniffer_thread;
        new_sock = malloc(1);
        *new_sock = new_socket;
         
        if( pthread_create( &sniffer_thread , NULL ,  connection_handler , (void*) new_sock) < 0)
        {
            perror("could not create thread");
            return 1;
        }
        puts("Handler assigned");
    }
     
    if (new_socket<0)
    {
        perror("accept failed");
        return 1;
    }
     
    return 0;
}

```
> Client
```c
#include<stdio.h>
#include<string.h> 
#include <fcntl.h>
#include<sys/socket.h>
#include<arpa/inet.h> 
int main(int argc , char *argv[])
{
	int socket_desc, read_size,fd;
	int file,filelength;
	struct sockaddr_in server;
	char message[1024];
	char servers[2000];
	socket_desc = socket(AF_INET , SOCK_STREAM , 0);
	server.sin_addr.s_addr = inet_addr(argv[1]);
	server.sin_family = AF_INET;
	server.sin_port = htons( 2000 );

	if (connect(socket_desc , (struct sockaddr *)&server ,sizeof(server)) < 0)
	{
		puts("connect error");
		return 1;
	}
	puts("Connected\n");
	file = fopen(argv[2], O_RDONLY);
	if(file < 0)
		perror("open");
	fseek(file, 0, SEEK_END);
	filelength = ftell(file);
	printf("文件大小为:%d", filelength);
	fseek(file, 0, SEEK_SET);
		
	read_size = recv(socket_desc, servers, 2000, 0);
	printf("%s\n",servers);
	// if ( (fd = open("/dev/input/mice", O_RDONLY)) == -1 )
	// {
	// 	perror("cannot open /dev/input/mice");
	// 	return 1;
	// }
	while (1)
	{
		//printf("你想说什么？\n");
		message[1024] = "你想说什么";
		// scanf("%s", message);
		send(socket_desc , message , 1024 , 0);
		// if( send(socket_desc , message , strlen(message) , 0) < 0)
		// {
		// 	puts("Send failed");
		// 	return 1;
		// }
	}
	return 0;
}

```

# git钩子

```c
#include <iostream>
#include <stdlib.h>
#include <spdlog/spdlog.h>
#include <nlohmann/json.hpp>
#include <httplib/httplib.h>
using nlohmann::json;
int main(){
    spdlog::info("app start ~~~");
    httplib::Server ser;
    ser.Post("/enable", [](const httplib::Request& req, httplib::Response& res){
        res.set_content("received", "text/plain");
        spdlog::info("enable: {}", req.get_param_value("data"));
        // system("cd /mnt/sda/WorkSpace/Server/MyWiki && git pull -f");
    });
    ser.Get("/enable", [](const httplib::Request& req, httplib::Response& res){
        res.set_content("Hello World!", "text/plain");
        spdlog::info("enable: {}", req.get_param_value("data"));
    });

    spdlog::info("listen: {}", "localhost:4002");
    ser.listen("0.0.0.0", 4002);

    return 0;
}
```

> 注意listen()里面不能写localhost  ，写0.0.0.0或者127.0.0.1
>
> 运行：nohup ./main 2>&1 &

# std::unique_lock

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

## 使用方法一

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

## 使用方法二

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

# std::condition_variable

条件变量提供了两类操作：wait和notify。这两类操作构成了多线程同步的基础。

使用条件变量可以在任务队列为空时CPU暂停轮询减少耗费CPU资源。

## wait

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

## notify

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



# 面试准备

进程是系统资源分配的基本单位。

线程是进程的子任务，是CPU调度的最小单位，共享同一片地址空间。

## 进程间通信

1. 管道： 数据是单向的，相互通信需要创建两个管道。无格式的字节流数据。
2. 消息队列：内核中，内存中的消息链表， 
3. 共享内存： 映射一块内存空间到相同的物理空间，进程之间对数据都可见。
4. 信号量： PV操作，
5. 信号： SIGNAL()   异步通信
6. socket： 不同主机间的进程通信

## 线程间通信

1. 互斥量
2. 信号量
3. 临界区： 多线程串行化访问公共资源
4. 等待通知时间
