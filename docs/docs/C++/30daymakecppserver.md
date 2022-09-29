---
comments: true
---
# 30天自制C++服务器

教程的配套网络库：[pine](https://github.com/yuesong-feng/pine)，star and fork!

先说结论：不管使用什么语言，一切后台开发的根基，是面向Linux的C/C++服务器开发。

几乎所有高并发服务器都是运行在Linux环境的，笔者之前也用Java、node写过服务器，但最后发现只是学会了一门技术、一门语言，而并不了解底层的基础原理。一个HTTP请求的过程，为什么可以实现高并发，如何控制TCP连接，如何处理好数据传输的逻辑等等，这些只有面向C/C++编程才能深入了解。

本教程模仿《30天自制操作系统》，面向零经验的新手，教你在30天内入门Linux服务器开发。本教程更偏向实践，将会把重点放在如何写代码上，而不会花太多的篇幅讲解背后的计算机基础原理，涉及到的地方会给出相应书籍的具体章节，但这并不代表这些理论知识不重要，事实上理论基础相当重要，没有理论的支撑，构建出一个高性能服务器是无稽之谈。

本教程希望读者：

- 熟悉C/C++语言
- 熟悉计算机网络基础，如TCP协议、socket原理等
- 了解基本的操作系统基础概念，如进程、线程、内存资源、系统调用等

学完本教程后，你将会很轻松地看懂muduo源码。

C/C++学习的一个难点在于初学时无法做出实际上的东西，没有反馈，程序都在黑乎乎的命令行里运行，不像web开发，可以随时看到自己学习的成果。本教程的代码都放在code文件夹里，每一天学习后都可以得到一个可以编译运行的服务器，不断迭代开发。

在code文件夹里有每一天的代码文件夹，进入该文件夹，使用`make`命令编译，会生成两个可执行文件，输入命令`./server`就能看到今天的学习成果！然后新建一个Terminal，然后输入`./client`运行客户端，与服务器交互。

[day01-从一个最简单的socket开始](https://github.com/yuesong-feng/30dayMakeCppServer/blob/main/day01-从一个最简单的socket开始.md)

[day02-不要放过任何一个错误](https://github.com/yuesong-feng/30dayMakeCppServer/blob/main/day02-不要放过任何一个错误.md)

[day03-高并发还得用epoll](https://github.com/yuesong-feng/30dayMakeCppServer/blob/main/day03-高并发还得用epoll.md)

[day04-来看看我们的第一个类](https://github.com/yuesong-feng/30dayMakeCppServer/blob/main/day04-来看看我们的第一个类.md)

[day05-epoll高级用法-Channel登场](https://github.com/yuesong-feng/30dayMakeCppServer/blob/main/day05-epoll高级用法-Channel登场.md)

[day06-服务器与事件驱动核心类登场](https://github.com/yuesong-feng/30dayMakeCppServer/blob/main/day06-服务器与事件驱动核心类登场.md)

[day07-为我们的服务器添加一个Acceptor](https://github.com/yuesong-feng/30dayMakeCppServer/blob/main/day07-为我们的服务器添加一个Acceptor.md)

[day08-一切皆是类，连TCP连接也不例外](https://github.com/yuesong-feng/30dayMakeCppServer/blob/main/day08-一切皆是类，连TCP连接也不例外.md)

[day09-缓冲区-大作用](https://github.com/yuesong-feng/30dayMakeCppServer/blob/main/day09-缓冲区-大作用.md)

[day10-加入线程池到服务器](https://github.com/yuesong-feng/30dayMakeCppServer/blob/main/day10-加入线程池到服务器.md)

[day11-完善线程池，服务器成型，写测试程序](https://github.com/yuesong-feng/30dayMakeCppServer/blob/main/day11-完善线程池，加入一个简单的测试程序.md)

[day12-将服务器改写为主从Reactor多线程模式](https://github.com/yuesong-feng/30dayMakeCppServer/blob/main/day12-将服务器改写为主从Reactor多线程模式.md)

[day13-C++工程化、代码分析、性能优化](https://github.com/yuesong-feng/30dayMakeCppServer/blob/main/day13-C++工程化、代码分析、性能优化.md)

[day14-支持业务逻辑自定义、完善Connection类](https://github.com/yuesong-feng/30dayMakeCppServer/blob/main/day14-支持业务逻辑自定义、完善Connection类.md)

[day15-macOS、FreeBSD支持](https://github.com/yuesong-feng/30dayMakeCppServer/blob/main/day15-macOS、FreeBSD支持.md)

## todo list:

定时器

日志系统

HTTP协议支持

webbench测试

......

Contribute

能力一般、水平有限，如果发现我的教程有不正确或者值得改进的地方，欢迎提issue或直接PR。

欢迎大家为本项目贡献自己的代码，如果有你觉得更好的代码，请提issue或者直接PR，所有建议都会被考虑。

贡献代码请到[pine](https://github.com/yuesong-feng/pine)项目，这是本教程开发的网络库，也是最新的代码版本。

## day01-从一个最简单的socket开始

如果读者之前有计算机网络的基础知识那就更好了，没有也没关系，socket编程非常容易上手。但本教程主要偏向实践，不会详细讲述计算机网络协议、网络编程原理等。想快速入门可以看以下博客，讲解比较清楚、错误较少：

- [计算机网络基础知识总结](https://www.runoob.com/w3cnote/summary-of-network.html)

要想打好基础，抄近道是不可的，有时间一定要认真学一遍谢希仁的《计算机网络》，要想精通服务器开发，这必不可少。

首先在服务器，我们需要建立一个socket套接字，对外提供一个网络通信接口，在Linux系统中这个套接字竟然仅仅是一个文件描述符，也就是一个`int`类型的值！这个对套接字的所有操作（包括创建）都是最底层的系统调用。

> 在这里读者务必先了解什么是Linux系统调用和文件描述符，《现代操作系统》第四版第一章有详细的讨论。如果你想抄近道看博客，C语言中文网的这篇文章讲了一部分：[socket是什么？套接字是什么？](http://c.biancheng.net/view/2123.html)

> Unix哲学KISS：keep it simple, stupid。在Linux系统里，一切看上去十分复杂的逻辑功能，都用简单到不可思议的方式实现，甚至有些时候看上去很愚蠢。但仔细推敲，人们将会赞叹Linux的精巧设计，或许这就是大智若愚。

```c
#include <sys/socket.h>
int sockfd = socket(AF_INET, SOCK_STREAM, 0);
```

- 第一个参数：IP地址类型，AF_INET表示使用IPv4，如果使用IPv6请使用AF_INET6。
- 第二个参数：数据传输方式，SOCK_STREAM表示流格式、面向连接，多用于TCP。SOCK_DGRAM表示数据报格式、无连接，多用于UDP。
- 第三个参数：协议，0表示根据前面的两个参数自动推导协议类型。设置为IPPROTO_TCP和IPPTOTO_UDP，分别表示TCP和UDP。

对于客户端，服务器存在的唯一标识是一个IP地址和端口，这时候我们需要将这个套接字绑定到一个IP地址和端口上。首先创建一个sockaddr_in结构体

```c
#include <arpa/inet.h>  //这个头文件包含了<netinet/in.h>，不用再次包含了
struct sockaddr_in serv_addr;
bzero(&serv_addr, sizeof(serv_addr));
```

然后使用`bzero`初始化这个结构体，这个函数在头文件`<string.h>`或`<cstring>`中。这里用到了两条《Effective C++》的准则：

> 条款04: 确定对象被使用前已先被初始化。如果不清空，使用gdb调试器查看addr内的变量，会是一些随机值，未来可能会导致意想不到的问题。

> 条款01: 视C++为一个语言联邦。把C和C++看作两种语言，写代码时需要清楚地知道自己在写C还是C++。如果在写C，请包含头文件`<string.h>`。如果在写C++，请包含`<cstring>`。

设置地址族、IP地址和端口：

```c
serv_addr.sin_family = AF_INET;
serv_addr.sin_addr.s_addr = inet_addr("127.0.0.1");
serv_addr.sin_port = htons(8888);
```

然后将socket地址与文件描述符绑定：

```c
bind(sockfd, (sockaddr*)&serv_addr, sizeof(serv_addr));
```

!!!
    为什么定义的时候使用专用socket地址（sockaddr_in）而绑定的时候要转化为通用socket地址（sockaddr），以及转化IP地址和端口号为网络字节序的`inet_addr`和`htons`等函数及其必要性

    #### 为什么使用 sockaddr_in 而不使用 sockaddr

    bind() 第二个参数的类型为 sockaddr，而代码中却使用 sockaddr_in，然后再强制转换为 sockaddr，这是为什么呢？

    sockaddr 结构体的定义如下：

    ```c
    struct sockaddr{    
     sa_family_t  sin_family;   //地址族（Address Family），也就是地址类型    
     char         sa_data[14];  //IP地址和端口号
    };
    ```

    下图是 sockaddr 与 sockaddr_in 的对比（括号中的数字表示所占用的字节数）：

    ![1](img/1.jpg)

    sockaddr 和 sockaddr_in 的长度相同，都是16字节，只是将IP地址和端口号合并到一起，用一个成员 sa_data 表示。要想给 sa_data 赋值，必须同时指明IP地址和端口号，例如”127.0.0.1:80“，遗憾的是，没有相关函数将这个字符串转换成需要的形式，也就很难给 sockaddr 类型的变量赋值，所以使用 sockaddr_in 来代替。这两个结构体的长度相同，强制转换类型时不会丢失字节，也没有多余的字节。
    
    可以认为，sockaddr 是一种通用的结构体，可以用来保存多种类型的IP地址和端口号，而 sockaddr_in 是专门用来保存 IPv4 地址的结构体。另外还有 sockaddr_in6，用来保存 IPv6 地址，它的定义如下：

    ```c
    struct sockaddr_in6 { 
     sa_family_t sin6_family;  //(2)地址类型，取值为AF_INET6
     in_port_t sin6_port;  //(2)16位端口号
     uint32_t sin6_flowinfo;  //(4)IPv6流信息
     struct in6_addr sin6_addr;  //(4)具体的IPv6地址
     uint32_t sin6_scope_id;  //(4)接口范围ID
    };
    ```

    正是由于通用结构体 sockaddr 使用不便，才针对不同的地址类型定义了不同的结构体。

最后我们需要使用`listen`函数监听这个socket端口，这个函数的第二个参数是listen函数的最大监听队列长度，系统建议的最大值`SOMAXCONN`被定义为128。

```c
listen(sockfd, SOMAXCONN);
```

要接受一个客户端连接，需要使用`accept`函数。对于每一个客户端，我们在接受连接时也需要保存客户端的socket地址信息，于是有以下代码：

```c
struct sockaddr_in clnt_addr;
socklen_t clnt_addr_len = sizeof(clnt_addr);
bzero(&clnt_addr, sizeof(clnt_addr));
int clnt_sockfd = accept(sockfd, (sockaddr*)&clnt_addr, &clnt_addr_len);
printf("new client fd %d! IP: %s Port: %d\n", clnt_sockfd, inet_ntoa(clnt_addr.sin_addr), ntohs(clnt_addr.sin_port));
```

要注意和`accept`和`bind`的第三个参数有一点区别，对于`bind`只需要传入serv_addr的大小即可，而`accept`需要写入客户端socket长度，所以需要定义一个类型为`socklen_t`的变量，并传入这个变量的地址。另外，`accept`函数会阻塞当前程序，直到有一个客户端socket被接受后程序才会往下运行。

到现在，客户端已经可以通过IP地址和端口号连接到这个socket端口了，让我们写一个测试客户端连接试试：

```c
int sockfd = socket(AF_INET, SOCK_STREAM, 0);
struct sockaddr_in serv_addr;
bzero(&serv_addr, sizeof(serv_addr));
serv_addr.sin_family = AF_INET;
serv_addr.sin_addr.s_addr = inet_addr("127.0.0.1");
serv_addr.sin_port = htons(8888);
connect(sockfd, (sockaddr*)&serv_addr, sizeof(serv_addr));  
```

代码和服务器代码几乎一样：创建一个socket文件描述符，与一个IP地址和端口绑定，最后并不是监听这个端口，而是使用`connect`函数尝试连接这个服务器。

至此，day01的教程已经结束了，进入`code/day01`文件夹，使用make命令编译，将会得到`server`和`client`。输入命令`./server`开始运行，直到`accept`函数，程序阻塞、等待客户端连接。然后在一个新终端输入命令`./client`运行客户端，可以看到服务器接收到了客户端的连接请求，并成功连接。

```
new client fd 3! IP: 127.0.0.1 Port: 53505
```

但如果我们先运行客户端、后运行服务器，在客户端一侧无任何区别，却并没有连接服务器成功，因为我们day01的程序没有任何的错误处理。

事实上对于如`socket`,`bind`,`listen`,`accept`,`connect`等函数，通过返回值以及`errno`可以确定程序运行的状态、是否发生错误。在day02的教程中，我们会进一步完善整个服务器，处理所有可能的错误，并实现一个echo服务器（客户端发送给服务器一个字符串，服务器收到后返回相同的内容）。

完整源代码：[https://github.com/yuesong-feng/30dayMakeCppServer/tree/main/code/day01](https://github.com/yuesong-feng/30dayMakeCppServer/tree/main/code/day01)



## day02-不要放过任何一个错误

在上一天，我们写了一个客户端发起socket连接和一个服务器接受socket连接。然而对于`socket`,`bind`,`listen`,`accept`,`connect`等函数，我们都设想程序完美地、没有任何异常地运行，而这显然是不可能的，不管写代码水平多高，就算你是林纳斯，也会在程序里写出bug。

在《Effective C++》中条款08讲到，别让异常逃离析构函数。在这里我拓展一下，我们不应该放过每一个异常，否则在大型项目开发中一定会遇到很难定位的bug！

> 具体信息可以参考《Effective C++》原书条款08，这里不再赘述。

对于Linux系统调用，常见的错误提示方式是使用返回值和设置errno来说明错误类型。

> 详细的C++语言异常处理请参考《C++ Primer》第五版第五章第六节

通常来讲，当一个系统调用返回-1，说明有error发生。我们来看看socket编程最常见的错误处理模版：

```c
int sockfd = socket(AF_INET, SOCK_STREAM, 0);
if(sockfd == -1)
{
    print("socket create error");
    exit(-1);
}
```

为了处理一个错误，需要至少占用五行代码，这使编程十分繁琐，程序也不好看，异常处理所占篇幅比程序本身都多。

为了方便编码以及代码的可读性，可以封装一个错误处理函数：

```c
void errif(bool condition, const char *errmsg){
    if(condition){
        perror(errmsg);
        exit(EXIT_FAILURE);
    }
}
```

第一个参数是是否发生错误，如果为真，则表示有错误发生，会调用`<stdio.h>`头文件中的`perror`，这个函数会打印出`errno`的实际意义，还会打印出我们传入的字符串，也就是第函数第二个参数，让我们很方便定位到程序出现错误的地方。然后使用`<stdlib.h>`中的`exit`函数让程序退出并返回一个预定义常量`EXIT_FAILURE`。

在使用的时候:

```c
int sockfd = socket(AF_INET, SOCK_STREAM, 0);
errif(sockfd == -1, "socket create error");
```

这样我们只需要使用一行进行错误处理，写起来方便简单，也输出了自定义信息，用于定位bug。

对于所有的函数，我们都使用这种方式处理错误：

```c
errif(bind(sockfd, (sockaddr*)&serv_addr, sizeof(serv_addr)) == -1, "socket bind error");
errif(listen(sockfd, SOMAXCONN) == -1, "socket listen error");
int clnt_sockfd = accept(sockfd, (sockaddr*)&clnt_addr, &clnt_addr_len);
errif(clnt_sockfd == -1, "socket accept error");
errif(connect(sockfd, (sockaddr*)&serv_addr, sizeof(serv_addr)) == -1, "socket connect error");
```

到现在最简单的错误处理函数已经封装好了，但这仅仅用于本教程的开发，在真实的服务器开发中，错误绝不是一个如此简单的话题。

当我们建立一个socket连接后，就可以使用`<unistd.h>`头文件中`read`和`write`来进行网络接口的数据读写操作了。

> 这两个函数用于TCP连接。如果是UDP，需要使用`sendto`和`recvfrom`，这些函数的详细用法可以参考游双《Linux高性能服务器编程》第五章第八节。

接下来的教程用注释的形式写在代码中，先来看服务器代码：

```c
while (true) {
    char buf[1024];     //定义缓冲区
    bzero(&buf, sizeof(buf));       //清空缓冲区
    ssize_t read_bytes = read(clnt_sockfd, buf, sizeof(buf)); //从客户端socket读到缓冲区，返回已读数据大小
    if(read_bytes > 0){
        printf("message from client fd %d: %s\n", clnt_sockfd, buf);  
        write(clnt_sockfd, buf, sizeof(buf));           //将相同的数据写回到客户端
    } else if(read_bytes == 0){             //read返回0，表示EOF
        printf("client fd %d disconnected\n", clnt_sockfd);
        close(clnt_sockfd);
        break;
    } else if(read_bytes == -1){        //read返回-1，表示发生错误，按照上文方法进行错误处理
        close(clnt_sockfd);
        errif(true, "socket read error");
    }
}
```

客户端代码逻辑是一样的：

```c
while(true){
    char buf[1024];     //定义缓冲区
    bzero(&buf, sizeof(buf));       //清空缓冲区
    scanf("%s", buf);             //从键盘输入要传到服务器的数据
    ssize_t write_bytes = write(sockfd, buf, sizeof(buf));      //发送缓冲区中的数据到服务器socket，返回已发送数据大小
    if(write_bytes == -1){          //write返回-1，表示发生错误
        printf("socket already disconnected, can't write any more!\n");
        break;
    }
    bzero(&buf, sizeof(buf));       //清空缓冲区 
    ssize_t read_bytes = read(sockfd, buf, sizeof(buf));    //从服务器socket读到缓冲区，返回已读数据大小
    if(read_bytes > 0){
        printf("message from server: %s\n", buf);
    }else if(read_bytes == 0){      //read返回0，表示EOF，通常是服务器断开链接，等会儿进行测试
        printf("server socket disconnected!\n");
        break;
    }else if(read_bytes == -1){     //read返回-1，表示发生错误，按照上文方法进行错误处理
        close(sockfd);
        errif(true, "socket read error");
    }
}
```

> 一个小细节，Linux系统的文件描述符理论上是有限的，在使用完一个fd之后，需要使用头文件`<unistd.h>`中的`close`函数关闭。更多内核相关知识可以参考Robert Love《Linux内核设计与实现》的第三版。

至此，day02的主要教程已经结束了，完整源代码请在`code/day02`文件夹，接下来看看今天的学习成果以及测试我们的服务器！

进入`code/day02`文件夹，使用make命令编译，将会得到`server`和`client`。输入命令`./server`开始运行，直到`accept`函数，程序阻塞、等待客户端连接。然后在一个新终端输入命令`./client`运行客户端，可以看到服务器接收到了客户端的连接请求，并成功连接。现在客户端阻塞在`scanf`函数，等待我们键盘输入，我们可以输入一句话，然后回车。在服务器终端，我们可以看到:

```
message from client fd 4: Hello!
```

然后在客户端，也能接受到服务器的消息：

```
message from server: Hello!
```

> 由于是一个`while(true)`循环，客户端可以一直输入，服务器也会一直echo我们的消息。由于`scanf`函数的特性，输入的语句遇到空格时，会当成多行进行处理，我们可以试试。

接下来在客户端使用`control+c`终止程序，可以看到服务器也退出了程序并显示：

```
client fd 4 disconnected
```

再次运行两个程序，这次我们使用`control+c`终止掉服务器，再试图从客户端发送信息，可以看到客户端输出：

```
server socket disconnected!
```

至此，我们已经完整地开发了一个echo服务器，并且有最基本的错误处理！

但现在，我们的服务器只能处理一个客户端，我们可以试试两个客户端同时连接服务器，看程序将会如何运行。在day03的教程里，我们将会讲解Linux系统高并发的基石--epoll，并编程实现一个可以支持无数客户端同时连接的echo服务器！

完整源代码：[https://github.com/yuesong-feng/30dayMakeCppServer/tree/main/code/day02](https://github.com/yuesong-feng/30dayMakeCppServer/tree/main/code/day02)



## day03-高并发还得用epoll

在上一天，我们写了一个简单的echo服务器，但只能同时处理一个客户端的连接。但在这个连接的生命周期中，绝大部分时间都是空闲的，活跃时间（发送数据和接收数据的时间）占比极少，这样独占一个服务器是严重的资源浪费。事实上所有的服务器都是高并发的，可以同时为成千上万个客户端提供服务，这一技术又被称为IO复用。

> IO复用和多线程有相似之处，但绝不是一个概念。IO复用是针对IO接口，而多线程是针对CPU。

IO复用的基本思想是事件驱动，服务器同时保持多个客户端IO连接，当这个IO上有可读或可写事件发生时，表示这个IO对应的客户端在请求服务器的某项服务，此时服务器响应该服务。在Linux系统中，IO复用使用select, poll和epoll来实现。epoll改进了前两者，更加高效、性能更好，是目前几乎所有高并发服务器的基石。请读者务必先掌握epoll的原理再进行编码开发。

> select, poll与epoll的详细原理和区别请参考《UNIX网络编程：卷1》第二部分第六章，游双《Linux高性能服务器编程》第九章

epoll主要由三个系统调用组成：

```c
//int epfd = epoll_create(1024);  //参数表示监听事件的大小，如超过内核会自动调整，已经被舍弃，无实际意义，传入一个大于0的数即可
int epfd = epoll_create1(0);       //参数是一个flag，一般设为0，详细参考man epoll
```

创建一个epoll文件描述符并返回，失败则返回-1。

epoll监听事件的描述符会放在一颗红黑树上，我们将要监听的IO口放入epoll红黑树中，就可以监听该IO上的事件。

```c
epoll_ctl(epfd, EPOLL_CTL_ADD, sockfd, &ev);    //添加事件到epoll
epoll_ctl(epfd, EPOLL_CTL_MOD, sockfd, &ev);    //修改epoll红黑树上的事件
epoll_ctl(epfd, EPOLL_CTL_DEL, sockfd, NULL);   //删除事件
```

其中sockfd表示我们要添加的IO文件描述符，ev是一个epoll_event结构体，其中的events表示事件，如EPOLLIN等，data是一个用户数据union:

```c
typedef union epoll_data {
  void *ptr;
  int fd;
  uint32_t u32;
  uint64_t u64;
} epoll_data_t;
struct epoll_event {
  uint32_t events;	/* Epoll events */
  epoll_data_t data;	/* User data variable */
} __EPOLL_PACKED;
```

epoll默认采用LT触发模式，即水平触发，只要fd上有事件，就会一直通知内核。这样可以保证所有事件都得到处理、不容易丢失，但可能发生的大量重复通知也会影响epoll的性能。如使用ET模式，即边缘触法，fd从无事件到有事件的变化会通知内核一次，之后就不会再次通知内核。这种方式十分高效，可以大大提高支持的并发度，但程序逻辑必须一次性很好地处理该fd上的事件，编程比LT更繁琐。注意ET模式必须搭配非阻塞式socket使用。

> 非阻塞式socket和阻塞式有很大的不同，请参考《UNIX网络编程：卷1》第三部分第16章。

我们可以随时使用`epoll_wait`获取有事件发生的fd：

```c
int nfds = epoll_wait(epfd, events, maxevents, timeout);
```

其中events是一个epoll_event结构体数组，maxevents是可供返回的最大事件大小，一般是events的大小，timeout表示最大等待时间，设置为-1表示一直等待。

接下来将day02的服务器改写成epoll版本，基本思想为：在创建了服务器socket fd后，将这个fd添加到epoll，只要这个fd上发生可读事件，表示有一个新的客户端连接。然后accept这个客户端并将客户端的socket fd添加到epoll，epoll会监听客户端socket fd是否有事件发生，如果发生则处理事件。

接下来的教程在伪代码中：

```c
int sockfd = socket(...);   //创建服务器socket fd
bind(sockfd...);
listen(sockfd...);
int epfd = epoll_create1(0);
struct epoll_event events[MAX_EVENTS], ev;
ev.events = EPOLLIN;    //在代码中使用了ET模式，且未处理错误，在day12进行了修复，实际上接受连接最好不要用ET模式
ev.data.fd = sockfd;    //该IO口为服务器socket fd
epoll_ctl(epfd, EPOLL_CTL_ADD, sockfd, &ev);    //将服务器socket fd添加到epoll
while(true){    // 不断监听epoll上的事件并处理
    int nfds = epoll_wait(epfd, events, MAX_EVENTS, -1);   //有nfds个fd发生事件
    for(int i = 0; i < nfds; ++i){  //处理这nfds个事件
        if(events[i].data.fd == sockfd){    //发生事件的fd是服务器socket fd，表示有新客户端连接
            int clnt_sockfd = accept(sockfd, (sockaddr*)&clnt_addr, &clnt_addr_len);
            ev.data.fd = clnt_sockfd;   
            ev.events = EPOLLIN | EPOLLET;  //对于客户端连接，使用ET模式，可以让epoll更加高效，支持更多并发
            setnonblocking(clnt_sockfd);    //ET需要搭配非阻塞式socket使用
            epoll_ctl(epfd, EPOLL_CTL_ADD, clnt_sockfd, &ev);   //将该客户端的socket fd添加到epoll
        } else if(events[i].events & EPOLLIN){      //发生事件的是客户端，并且是可读事件（EPOLLIN）
            handleEvent(events[i].data.fd);         //处理该fd上发生的事件
        }
    }
}
```

从一个非阻塞式socket fd上读取数据时：

```c
while(true){    //由于使用非阻塞IO，需要不断读取，直到全部读取完毕
    ssize_t bytes_read = read(events[i].data.fd, buf, sizeof(buf));
    if(bytes_read > 0){
      //保存读取到的bytes_read大小的数据
    } else if(bytes_read == -1 && errno == EINTR){  //客户端正常中断、继续读取
        continue;
    } else if(bytes_read == -1 && ((errno == EAGAIN) || (errno == EWOULDBLOCK))){//非阻塞IO，这个条件表示数据全部读取完毕
        //该fd上数据读取完毕
        break;
    } else if(bytes_read == 0){  //EOF事件，一般表示客户端断开连接
        close(events[i].data.fd);   //关闭socket会自动将文件描述符从epoll树上移除
        break;
    } //剩下的bytes_read == -1的情况表示其他错误，这里没有处理
}
```

至此，day03的主要教程已经结束了，完整源代码请在`code/day03`文件夹，接下来看看今天的学习成果以及测试我们的服务器！

进入`code/day03`文件夹，使用make命令编译，将会得到`server`和`client`，输入命令`./server`开始运行服务器。然后在一个新终端输入命令`./client`运行客户端，可以看到服务器接收到了客户端的连接请求，并成功连接。再新开一个或多个终端，运行client，可以看到这些客户端也同时连接到了服务器。此时我们在任意一个client输入一条信息，服务器都显示并发送到该客户端。如使用`control+c`终止掉某个client，服务器回显示这个client已经断开连接，但其他client并不受影响。

至此，我们已经完整地开发了一个echo服务器，并且支持多个客户端同时连接，为他们提供服务！

完整源代码：[https://github.com/yuesong-feng/30dayMakeCppServer/tree/main/code/day03](https://github.com/yuesong-feng/30dayMakeCppServer/tree/main/code/day03)

## day04-来看看我们的第一个类

在上一天，我们开发了一个支持多个客户端连接的服务器，但到目前为止，虽然我们的程序以`.cpp`结尾，本质上我们写的仍然是C语言程序。虽然C++语言完全兼容C语言并且大部分程序中都是混用，但一个很好的习惯是把C和C++看作两种语言，写代码时需要清楚地知道自己在写C还是C++。

另一点是我们的程序会变得越来越长、越来越庞大，虽然现在才不到100行代码，但把所有逻辑放在一个程序里显然是一种错误的做法，我们需要对程序进行模块化，每一个模块专门处理一个任务，这样可以增加程序的可读性，也可以写出更大庞大、功能更加复杂的程序。不仅如此，还可以很方便地进行代码复用，也就是造轮子。

C++是一门面向对象的语言，最低级的模块化的方式就是构建一个类。举个例子，我们的程序有新建服务器socket、绑定IP地址、监听、接受客户端连接等任务，代码如下：

```c
int sockfd = socket(AF_INET, SOCK_STREAM, 0);
errif(sockfd == -1, "socket create error");

struct sockaddr_in serv_addr;
bzero(&serv_addr, sizeof(serv_addr));
serv_addr.sin_family = AF_INET;
serv_addr.sin_addr.s_addr = inet_addr("127.0.0.1");
serv_addr.sin_port = htons(8888);

errif(bind(sockfd, (sockaddr*)&serv_addr, sizeof(serv_addr)) == -1, "socket bind error");

errif(listen(sockfd, SOMAXCONN) == -1, "socket listen error");

struct sockaddr_in clnt_addr;
bzero(&clnt_addr, sizeof(clnt_addr));
socklen_t clnt_addr_len = sizeof(clnt_addr);

int clnt_sockfd = accept(sockfd, (sockaddr*)&clnt_addr, &clnt_addr_len);
errif(clnt_sockfd == -1, "socket accept error");
```

可以看到代码有19行，这已经是使用socket最精简的代码。在服务器开发中，我们或许会建立多个socket口，或许会处理多个客户端连接，但我们并不希望每次都重复编写这么多行代码，我们希望这样使用：

```c
Socket *serv_sock = new Socket();
InetAddress *serv_addr = new InetAddress("127.0.0.1", 8888);
serv_sock->bind(serv_addr);
serv_sock->listen();   
InetAddress *clnt_addr = new InetAddress();  
Socket *clnt_sock = new Socket(serv_sock->accept(clnt_addr));    
```

仅仅六行代码就可以实现和之前一样的功能，这样的使用方式忽略了底层的语言细节，不用在程序中考虑错误处理，更简单、更加专注于程序的自然逻辑，大家毫无疑问也肯定希望以这样简单的方式使用socket。

类似的还有epoll，最精简的使用方式为：

```c
int epfd = epoll_create1(0);
errif(epfd == -1, "epoll create error");

struct epoll_event events[MAX_EVENTS], ev;
bzero(&events, sizeof(events) * MAX_EVENTS);

bzero(&ev, sizeof(ev));
ev.data.fd = sockfd;
ev.events = EPOLLIN | EPOLLET;

epoll_ctl(epfd, EPOLL_CTL_ADD, sockfd, &ev);

while(true){
    int nfds = epoll_wait(epfd, events, MAX_EVENTS, -1);
    errif(nfds == -1, "epoll wait error");
    for(int i = 0; i < nfds; ++i){
        // handle event
    }
}
```

而我们更希望这样来使用：

```c
Epoll *ep = new Epoll();
ep->addFd(serv_sock->getFd(), EPOLLIN | EPOLLET);
while(true){
    vector<epoll_event> events = ep->poll();
    for(int i = 0; i < events.size(); ++i){
        // handle event
    }
}
```

同样完全忽略了如错误处理之类的底层细节，大大简化了编程，增加了程序的可读性。

在今天的代码中，程序的功能和昨天一样，仅仅将`Socket`、`InetAddress`和`Epoll`封装成类，这也是面向对象编程的最核心、最基本的思想。现在我们的目录结构为：

```
client.cpp
Epoll.cpp
Epoll.h
InetAddress.cpp
InetAddress.h
Makefile
server.cpp
Socket.cpp
Socket.h
util.cpp
util.h
```

注意在编译程序的使用，需要编译`Socket`、`InetAddress`和`Epoll`类的`.cpp`文件，然后进行链接，因为`.h`文件里只是类的定义，并未实现。

> C/C++程序编译、链接是一个很复杂的事情，具体原理请参考《深入理解计算机系统（第三版）》第七章。

至此，day04的主要教程已经结束了，完整源代码请在`code/day04`文件夹，服务器的功能和昨天一样。

进入`code/day04`文件夹，使用make命令编译，将会得到`server`和`client`，输入命令`./server`开始运行服务器。然后在一个新终端输入命令`./client`运行客户端，可以看到服务器接收到了客户端的连接请求，并成功连接。再新开一个或多个终端，运行client，可以看到这些客户端也同时连接到了服务器。此时我们在任意一个client输入一条信息，服务器都显示并发送到该客户端。如使用`control+c`终止掉某个client，服务器回显示这个client已经断开连接，但其他client并不受影响。

至此，我们已经完整地开发了一个echo服务器，并且引入面向对象编程的思想，初步封装了`Socket`、`InetAddress`和`Epoll`，大大精简了主程序，隐藏了底层语言实现细节、增加了可读性。

完整源代码：[https://github.com/yuesong-feng/30dayMakeCppServer/tree/main/code/day04](https://github.com/yuesong-feng/30dayMakeCppServer/tree/main/code/day04)



## day05-epoll高级用法-Channel登场

在上一天，我们已经完整地开发了一个echo服务器，并且引入面向对象编程的思想，初步封装了`Socket`、`InetAddress`和`Epoll`，大大精简了主程序，隐藏了底层语言实现细节、增加了可读性。

让我们来回顾一下我们是如何使用`epoll`：将一个文件描述符添加到`epoll`红黑树，当该文件描述符上有事件发生时，拿到它、处理事件，这样我们每次只能拿到一个文件描述符，也就是一个`int`类型的整型值。试想，如果一个服务器同时提供不同的服务，如HTTP、FTP等，那么就算文件描述符上发生的事件都是可读事件，不同的连接类型也将决定不同的处理逻辑，仅仅通过一个文件描述符来区分显然会很麻烦，我们更加希望拿到关于这个文件描述符更多的信息。

在day03介绍`epoll`时，曾讲过`epoll_event`结构体：

```c
typedef union epoll_data {
  void *ptr;
  int fd;
  uint32_t u32;
  uint64_t u64;
} epoll_data_t;
struct epoll_event {
  uint32_t events;	/* Epoll events */
  epoll_data_t data;	/* User data variable */
} __EPOLL_PACKED;
```

可以看到，epoll中的`data`其实是一个联合类型，可以储存一个指针。而通过指针，理论上我们可以指向任何一个地址块的内容，可以是一个类的对象，这样就可以将一个文件描述符封装成一个`Channel`类，一个Channel类自始至终只负责一个文件描述符，对不同的服务、不同的事件类型，都可以在类中进行不同的处理，而不是仅仅拿到一个`int`类型的文件描述符。

> 这里读者务必先了解C++中的枚举类型，在《C++ Primer（第五版）》第十九章第六节有详细说明。

`Channel`类的核心成员如下：

```c
class Channel{
private:
    Epoll *ep;
    int fd;
    uint32_t events;
    uint32_t revents;
    bool inEpoll;
};
```

显然每个文件描述符会被分发到一个`Epoll`类，用一个`ep`指针来指向。类中还有这个`Channel`负责的文件描述符。另外是两个事件变量，`events`表示希望监听这个文件描述符的哪些事件，因为不同事件的处理方式不一样。`revents`表示在`epoll`返回该`Channel`时文件描述符正在发生的事件。`inEpoll`表示当前`Channel`是否已经在`epoll`红黑树中，为了注册`Channel`的时候方便区分使用`EPOLL_CTL_ADD`还是`EPOLL_CTL_MOD`。

接下来以`Channel`的方式使用epoll：
新建一个`Channel`时，必须说明该`Channel`与哪个`epoll`和`fd`绑定：

```c
Channel *servChannel = new Channel(ep, serv_sock->getFd());
```

这时该`Channel`还没有被添加到epoll红黑树，因为`events`没有被设置，不会监听该`Channel`上的任何事件发生。如果我们希望监听该`Channel`上发生的读事件，需要调用一个`enableReading`函数：

```c
servChannel->enableReading();
```

调用这个函数后，如`Channel`不在epoll红黑树中，则添加，否则直接更新`Channel`、打开允许读事件。`enableReading`函数如下：

```c
void Channel::enableReading(){
    events = EPOLLIN | EPOLLET;
    ep->updateChannel(this);
}
```

可以看到该函数做了两件事，将要监听的事件`events`设置为读事件并采用ET模式，然后在ep指针指向的Epoll红黑树中更新该`Channel`，`updateChannel`函数的实现如下：

```c
void Epoll::updateChannel(Channel *channel){
    int fd = channel->getFd();  //拿到Channel的文件描述符
    struct epoll_event ev;
    bzero(&ev, sizeof(ev));
    ev.data.ptr = channel;
    ev.events = channel->getEvents();   //拿到Channel希望监听的事件
    if(!channel->getInEpoll()){
        errif(epoll_ctl(epfd, EPOLL_CTL_ADD, fd, &ev) == -1, "epoll add error");//添加Channel中的fd到epoll
        channel->setInEpoll();
    } else{
        errif(epoll_ctl(epfd, EPOLL_CTL_MOD, fd, &ev) == -1, "epoll modify error");//已存在，则修改
    }
}
```

在使用时，我们可以通过`Epoll`类中的`poll()`函数获取当前有事件发生的`Channel`：

```c
while(true){
    vector<Channel*> activeChannels = ep->poll();
    // activeChannels是所有有事件发生的Channel
}
```

注：在今天教程的源代码中，并没有将事件处理改为使用`Channel`回调函数的方式，仍然使用了之前对文件描述符进行处理的方法，这是错误的，将在明天的教程中进行改写。

至此，day05的主要教程已经结束了，完整源代码请在`code/day05`文件夹。服务器的功能和昨天一样，添加了`Channel`类，可以让我们更加方便简单、多样化地处理epoll中发生的事件。同时脱离了底层，将epoll、文件描述符和事件进行了抽象，形成了事件分发的模型，这也是Reactor模式的核心，将在明天的教程进行讲解。

进入`code/day05`文件夹，使用make命令编译，将会得到`server`和`client`，输入命令`./server`开始运行服务器。然后在一个新终端输入命令`./client`运行客户端，可以看到服务器接收到了客户端的连接请求，并成功连接。再新开一个或多个终端，运行client，可以看到这些客户端也同时连接到了服务器。此时我们在任意一个client输入一条信息，服务器都显示并发送到该客户端。如使用`control+c`终止掉某个client，服务器回显示这个client已经断开连接，但其他client并不受影响。

完整源代码：[https://github.com/yuesong-feng/30dayMakeCppServer/tree/main/code/day05](https://github.com/yuesong-feng/30dayMakeCppServer/tree/main/code/day05)

## day06-服务器与事件驱动核心类登场

在上一天，我们为每一个添加到epoll的文件描述符都添加了一个`Channel`，用户可以自由注册各种事件、很方便地根据不同事件类型设置不同回调函数（在当前的源代码中只支持了目前所需的可读事件，将在之后逐渐进行完善）。我们的服务器已经基本成型，但目前从新建socket、接受客户端连接到处理客户端事件，整个程序结构是顺序化、流程化的，我们甚至可以使用一个单一的流程图来表示整个程序。而流程化程序设计的缺点之一是不够抽象，当我们的服务器结构越来越庞大、功能越来越复杂、模块越来越多，这种顺序程序设计的思想显然是不能满足需求的。

对于服务器开发，我们需要用到更抽象的设计模式。从代码中我们可以看到，不管是接受客户端连接还是处理客户端事件，都是围绕epoll来编程，可以说epoll是整个程序的核心，服务器做的事情就是监听epoll上的事件，然后对不同事件类型进行不同的处理。这种以事件为核心的模式又叫事件驱动，事实上几乎所有的现代服务器都是事件驱动的。和传统的请求驱动模型有很大不同，事件的捕获、通信、处理和持久保留是解决方案的核心结构。libevent就是一个著名的C语言事件驱动库。

需要注意的是，事件驱动不是服务器开发的专利。事件驱动是一种设计应用的思想、开发模式，而服务器是根据客户端的不同请求提供不同的服务的一个实体应用，服务器开发可以采用事件驱动模型、也可以不采用。事件驱动模型也可以在服务器之外的其他类型应用中出现，如进程通信、k8s调度、V8引擎、Node.js等。

理解了以上的概念，就能容易理解服务器开发的两种经典模式——Reactor和Proactor模式。详细请参考游双《Linux高性能服务器编程》第八章第四节、陈硕《Linux多线程服务器编程》第六章第六节。

> 如何深刻理解Reactor和Proactor？ - 小林coding的回答 - 知乎
> https://www.zhihu.com/question/26943938/answer/1856426252

由于Linux内核系统调用的设计更加符合Reactor模式，所以绝大部分高性能服务器都采用Reactor模式进行开发，我们的服务器也使用这种模式。

接下来我们要将服务器改造成Reactor模式。首先我们将整个服务器抽象成一个`Server`类，这个类中有一个main-Reactor（在这个版本没有sub-Reactor），里面的核心是一个`EventLoop`（libevent中叫做EventBase），这是一个事件循环，我们添加需要监听的事务到这个事件循环内，每次有事件发生时就会通知（在程序中返回给我们`Channel`），然后根据不同的描述符、事件类型进行处理（以回调函数的方式）。

> 如果你不太清楚这个自然段在讲什么，请先看一看前面提到的两本书的具体章节。

EventLoop类的定义如下：

```c
class EventLoop {
private:
    Epoll *ep;
    bool quit;
public:
    EventLoop();
    ~EventLoop();
    void loop();
    void updateChannel(Channel*);
};
```

调用`loop()`函数可以开始事件驱动，实际上就是原来的程序中调用`epoll_wait()`函数的死循环：

```c
void EventLoop::loop(){
    while(!quit){
    std::vector<Channel*> chs;
        chs = ep->poll();
        for(auto it = chs.begin(); it != chs.end(); ++it){
            (*it)->handleEvent();
        }
    }
}
```

现在我们可以以这种方式来启动服务器，和muduo的代码已经很接近了：

```c
EventLoop *loop = new EventLoop();
Server *server = new Server(loop);
loop->loop();
```

服务器定义如下：

```c
class Server {
private:
    EventLoop *loop;
public:
    Server(EventLoop*);
    ~Server();
    void handleReadEvent(int);
    void newConnection(Socket *serv_sock);
};
```

这个版本服务器内只有一个`EventLoop`，当其中有可读事件发生时，我们可以拿到该描述符对应的`Channel`。在新建`Channel`时，根据`Channel`描述符的不同分别绑定了两个回调函数，`newConnection()`函数被绑定到服务器socket上，`handlrReadEvent()`被绑定到新接受的客户端socket上。这样如果服务器socket有可读事件，`Channel`里的`handleEvent()`函数实际上会调用`Server`类的`newConnection()`新建连接。如果客户端socket有可读事件，`Channel`里的`handleEvent()`函数实际上会调用`Server`类的`handlrReadEvent()`响应客户端请求。

至此，我们已经抽象出了`EventLoop`和`Channel`，构成了事件驱动模型。这两个类和服务器核心`Server`已经没有任何关系，经过完善后可以被任何程序复用，达到了事件驱动的设计思想，现在我们的服务器也可以看成一个最简易的Reactor模式服务器。

当然，这个Reactor模式并不是一个完整的Reactor模式，如处理事件请求仍然在事件驱动的线程里，这显然违背了Reactor的概念。我们还需要做很多工作，在接下来几天的教程里会进一步完善。


完整源代码：[https://github.com/yuesong-feng/30dayMakeCppServer/tree/main/code/day06](https://github.com/yuesong-feng/30dayMakeCppServer/tree/main/code/day06)

## day07-为我们的服务器添加一个Acceptor

在上一天，我们分离了服务器类和事件驱动类，将服务器逐渐开发成Reactor模式。至此，所有服务器逻辑（目前只有接受新连接和echo客户端发来的数据）都写在`Server`类里。但很显然，`Server`作为一个服务器类，应该更抽象、更通用，我们应该对服务器进行进一步的模块化。

仔细分析可发现，对于每一个事件，不管提供什么样的服务，首先需要做的事都是调用`accept()`函数接受这个TCP连接，然后将socket文件描述符添加到epoll。当这个IO口有事件发生的时候，再对此TCP连接提供相应的服务。

> 在这里务必先理解TCP的面向连接这一特性，在谢希仁《计算机网络》里有详细的讨论。

因此我们可以分离接受连接这一模块，添加一个`Acceptor`类，这个类有以下几个特点：

- 类存在于事件驱动`EventLoop`类中，也就是Reactor模式的main-Reactor
- 类中的socket fd就是服务器监听的socket fd，每一个Acceptor对应一个socket fd
- 这个类也通过一个独有的`Channel`负责分发到epoll，该Channel的事件处理函数`handleEvent()`会调用Acceptor中的接受连接函数来新建一个TCP连接

根据分析，Acceptor类定义如下：

```c
class Acceptor{
private:
    EventLoop *loop;
    Socket *sock;
    InetAddress *addr;
    Channel *acceptChannel;
public:
    Acceptor(EventLoop *_loop);
    ~Acceptor();
    void acceptConnection();
};
```

这样一来，新建连接的逻辑就在`Acceptor`类中。但逻辑上新socket建立后就和之前监听的服务器socket没有任何关系了，TCP连接和`Acceptor`一样，拥有以上提到的三个特点，这两个类之间应该是平行关系。所以新的TCP连接应该由`Server`类来创建并管理生命周期，而不是`Acceptor`。并且将这一部分代码放在`Server`类里也并没有打破服务器的通用性，因为对于所有的服务，都要使用`Acceptor`来建立连接。

为了实现这一设计，我们可以用两种方式：

1. 使用传统的虚类、虚函数来设计一个接口
2. C++11的特性：std::function、std::bind、右值引用、std::move等实现函数回调

虚函数使用起来比较繁琐，程序的可读性也不够清晰明朗，而std::function、std::bind等新标准的出现可以完全替代虚函数，所以本教程采用第二种方式。

> 关于虚函数，在《C++ Primer》第十五章第三节有详细讨论，而C++11后的新标准可以参考欧长坤《现代 C++ 教程》

首先我们需要在Acceptor中定义一个新建连接的回调函数：

```c
std::function<void(Socket*)> newConnectionCallback;
```

在新建连接时，只需要调用这个回调函数：

```c
void Acceptor::acceptConnection(){
    newConnectionCallback(sock);
}
```

而这个回调函数本身的实现在`Server`类中：

```c
void Server::newConnection(Socket *serv_sock){
    // 接受serv_sock上的客户端连接
}
```

> 在今天的代码中，Acceptor的Channel使用了ET模式，事实上使用LT模式更合适，将在之后修复

新建Acceptor时通过std::bind进行绑定:

```c
acceptor = new Acceptor(loop);
std::function<void(Socket*)> cb = std::bind(&Server::newConnection, this, std::placeholders::_1);
acceptor->setNewConnectionCallback(cb);
```

这样一来，尽管我们抽象分离出了`Acceptor`，新建连接的工作任然由`Server`类来完成。

> 请确保清楚地知道为什么要这么做再进行之后的学习。

至此，今天的教程已经结束了。在今天，我们设计了服务器接受新连接的`Acceptor`类。测试方法和之前一样，使用`make`得到服务器和客户端程序并运行。虽然服务器功能已经好几天没有变化了，但每一天我们都在不断抽象、不断完善，从结构化、流程化的程序设计，到面向对象程序设计，再到面向设计模式的程序设计，逐渐学习服务器开发的思想与精髓。

完整源代码：[https://github.com/yuesong-feng/30dayMakeCppServer/tree/main/code/day07](https://github.com/yuesong-feng/30dayMakeCppServer/tree/main/code/day07)

## day08-一切皆是类，连TCP连接也不例外

在上一天，我们分离了用于接受连接的`Acceptor`类，并把新建连接的逻辑放在了`Server`类中。在上一天我们还提到了`Acceptor`类最主要的三个特点：

- 类存在于事件驱动`EventLoop`类中，也就是Reactor模式的main-Reactor
- 类中的socket fd就是服务器监听的socket fd，每一个Acceptor对应一个socket fd
- 这个类也通过一个独有的`Channel`负责分发到epoll，该Channel的事件处理函数`handleEvent()`会调用Acceptor中的接受连接函数来新建一个TCP连接

对于TCP协议，三次握手新建连接后，这个连接将会一直存在，直到我们四次挥手断开连接。因此，我们也可以把TCP连接抽象成一个`Connection`类，这个类也有以下几个特点：

- 类存在于事件驱动`EventLoop`类中，也就是Reactor模式的main-Reactor
- 类中的socket fd就是客户端的socket fd，每一个Connection对应一个socket fd
- 每一个类的实例通过一个独有的`Channel`负责分发到epoll，该Channel的事件处理函数`handleEvent()`会调用Connection中的事件处理函数来响应客户端请求

可以看到，`Connection`类和`Acceptor`类是平行关系、十分相似，他们都直接由`Server`管理，由一个`Channel`分发到epoll，通过回调函数处理相应事件。唯一的不同在于，`Acceptor`类的处理事件函数（也就是新建连接功能）被放到了`Server`类中，具体原因在上一天的教程中已经详细说明。而`Connection`类则没有必要这么做，处理事件的逻辑应该由`Connection`类本身来完成。

另外，一个高并发服务器一般只会有一个`Acceptor`用于接受连接（也可以有多个），但可能会同时拥有成千上万个TCP连接，也就是成千上万个`Connection`类的实例，我们需要把这些TCP连接都保存起来。现在我们可以改写服务器核心`Server`类，定义如下：

```c
class Server {
private:
    EventLoop *loop;    //事件循环
    Acceptor *acceptor; //用于接受TCP连接
    std::map<int, Connection*> connections; //所有TCP连接
public:
    Server(EventLoop*);
    ~Server();

    void handleReadEvent(int);  //处理客户端请求
    void newConnection(Socket *sock);   //新建TCP连接
    void deleteConnection(Socket *sock);   //断开TCP连接
};
```

在接受连接后，服务器把该TCP连接保存在一个`map`中，键为该连接客户端的socket fd，值为指向该连接的指针。该连接客户端的socket fd通过一个`Channel`类分发到epoll，该`Channel`的事件处理回调函数`handleEvent()`绑定为`Connection`的业务处理函数，这样每当该连接的socket fd上发生事件，就会通过`Channel`调用具体连接类的业务处理函数，伪代码如下：

```c
void Connection::echo(int sockfd){
    // 回显sockfd发来的数据
}
Connection::Connection(EventLoop *_loop, Socket *_sock) : loop(_loop), sock(_sock), channel(nullptr){
    channel = new Channel(loop, sock->getFd()); //该连接的Channel
    std::function<void()> cb = std::bind(&Connection::echo, this, sock->getFd()); 
    channel->setCallback(cb); //绑定回调函数
    channel->enableReading(); //打开读事件监听
}
```

对于断开TCP连接操作，也就是销毁一个`Connection`类的实例。由于`Connection`的生命周期由`Server`进行管理，所以也应该由`Server`来删除连接。如果在`Connection`业务中需要断开连接操作，也应该和之前一样使用回调函数来实现，在`Server`新建每一个连接时绑定删除该连接的回调函数：

```c
Connection *conn = new Connection(loop, sock);
std::function<void(Socket*)> cb = std::bind(&Server::deleteConnection, this, std::placeholders::_1);
conn->setDeleteConnectionCallback(cb);  // 绑定删除连接的回调函数

void Server::deleteConnection(Socket * sock){
    // 删除连接
}
```

至此，今天的教程已经结束，我们将TCP连接抽象成一个类，服务器模型更加成型。测试方法和之前一样，使用`make`得到服务器和客户端程序并运行。

这个版本是一个比较重要的版本，服务器最核心的几个模块都已经抽象出来，Reactor事件驱动大体成型（除了线程池），各个类的生命周期也大体上合适了，一个完整的单线程服务器设计模式已经编码完成了，读者应该完全理解今天的服务器代码后再继续后面的学习。

完整源代码：[https://github.com/yuesong-feng/30dayMakeCppServer/tree/main/code/day08](https://github.com/yuesong-feng/30dayMakeCppServer/tree/main/code/day08)

## day09-缓冲区-大作用

在之前的教程中，一个完整的单线程服务器设计模式已经编码完成了。在进入多线程编程之前，应该完全理解单线程服务器的工作原理，因为多线程更加复杂、更加困难，开发难度远大于之前的单线程模式。不仅如此，读者也应根据自己的理解进行二次开发，完善服务器，比如非阻塞式socket模块就值得细细研究。

今天的教程和之前几天的不同，引入了一个最简单、最基本的的缓冲区，可以看作一个完善、改进服务器的例子，更加偏向于细节而不是架构。除了这一细节，读者也可以按照自己的理解完善服务器。

同时，我们已经封装了socket、epoll等基础组件，这些组件都可以复用。现在我们完全可以使用这个网络库来改写客户端程序，让程序更加简单明了，读者可以自己尝试用这些组件写一个客户端，然后和源代码中的对照。

在没有缓冲区的时候，服务器回送客户端消息的代码如下：

```c
#define READ_BUFFER 1024
void Connection::echo(int sockfd){
    char buf[READ_BUFFER];
    while(true){    //由于使用非阻塞IO，读取客户端buffer，一次读取buf大小数据，直到全部读取完毕
        bzero(&buf, sizeof(buf));
        ssize_t bytes_read = read(sockfd, buf, sizeof(buf));
        if(bytes_read > 0){
            printf("message from client fd %d: %s\n", sockfd, buf);
            write(sockfd, buf, sizeof(buf));   // 发送给客户端
        } else if(bytes_read == -1 && errno == EINTR){  //客户端正常中断、继续读取
            printf("continue reading");
            continue;
        } else if(bytes_read == -1 && ((errno == EAGAIN) || (errno == EWOULDBLOCK))){//非阻塞IO，这个条件表示数据全部读取完毕
            printf("finish reading once, errno: %d\n", errno);
            break;
        } else if(bytes_read == 0){  //EOF，客户端断开连接
            printf("EOF, client fd %d disconnected\n", sockfd);
            deleteConnectionCallback(sock);
            break;
        }
    }
}
```

这是非阻塞式socket IO的读取，可以看到使用的读缓冲区大小为1024，每次从TCP缓冲区读取1024大小的数据到读缓冲区，然后发送给客户端。这是最底层C语言的编码，在逻辑上有很多不合适的地方。比如我们不知道客户端信息的真正大小是多少，只能以1024的读缓冲区去读TCP缓冲区（就算TCP缓冲区的数据没有1024，也会把后面的用空值补满）；也不能一次性读取所有客户端数据，再统一发给客户端。

> 关于TCP缓冲区、socket IO读取的细节，在《UNIX网络编程》卷一中有详细说明，想要精通网络编程几乎是必看的

虽然以上提到的缺点以C语言编程的方式都可以解决，但我们仍然希望以一种更加优美的方式读写socket上的数据，和其他模块一样，脱离底层，让我们使用的时候不用在意太多底层细节。所以封装一个缓冲区是很有必要的，为每一个`Connection`类分配一个读缓冲区和写缓冲区，从客户端读取来的数据都存放在读缓冲区里，这样`Connection`类就不再直接使用`char buf[]`这种最笨的缓冲区来处理读写操作。

缓冲区类的定义如下：

```c
class Buffer {
private:
    std::string buf;
public:
    void append(const char* _str, int _size);
    ssize_t size();
    const char* c_str();
    void clear();
    ......
};
```

> 这个缓冲区类使用`std::string`来储存数据，也可以使用`std::vector<char>`，有兴趣可以比较一下这两者的性能。

为每一个TCP连接分配一个读缓冲区后，就可以把客户端的信息读取到这个缓冲区内，缓冲区大小就是客户端发送的报文真实大小，代码如下：

```c
void Connection::echo(int sockfd){
    char buf[1024];     //这个buf大小无所谓
    while(true){    //由于使用非阻塞IO，读取客户端buffer，一次读取buf大小数据，直到全部读取完毕
        bzero(&buf, sizeof(buf));
        ssize_t bytes_read = read(sockfd, buf, sizeof(buf));
        if(bytes_read > 0){
            readBuffer->append(buf, bytes_read);
        } else if(bytes_read == -1 && errno == EINTR){  //客户端正常中断、继续读取
            printf("continue reading");
            continue;
        } else if(bytes_read == -1 && ((errno == EAGAIN) || (errno == EWOULDBLOCK))){//非阻塞IO，这个条件表示数据全部读取完毕
            printf("message from client fd %d: %s\n", sockfd, readBuffer->c_str());
            errif(write(sockfd, readBuffer->c_str(), readBuffer->size()) == -1, "socket write error");
            readBuffer->clear();
            break;
        } else if(bytes_read == 0){  //EOF，客户端断开连接
            printf("EOF, client fd %d disconnected\n", sockfd);
            deleteConnectionCallback(sock);
            break;
        }
    }
}
```

在这里依然有一个`char buf[]`缓冲区，用于系统调用`read()`的读取，这个缓冲区大小无所谓，但太大或太小都可能对性能有影响（太小读取次数增多，太大资源浪费、单次读取速度慢），设置为1到设备TCP缓冲区的大小都可以。以上代码会把socket IO上的可读数据全部读取到缓冲区，缓冲区大小就等于客户端发送的数据大小。全部读取完成之后，可以构造一个写缓冲区、填好数据发送给客户端。由于是echo服务器，所以这里使用了相同的缓冲区。

至此，今天的教程已经结束，这个缓冲区只是为了满足当前的服务器功能而构造的一个最简单的`Buffer`类，还需要进一步完善，读者可以按照自己的方式构建缓冲区类，完善其他细节，为后续的多线程服务器做准备。

完整源代码：[https://github.com/yuesong-feng/30dayMakeCppServer/tree/main/code/day09](https://github.com/yuesong-feng/30dayMakeCppServer/tree/main/code/day09)

## day10-加入线程池到服务器

今天是本教程的第十天，在之前，我们已经编码完成了一个完整的单线程服务器，最核心的几个模块都已经抽象出来，Reactor事件驱动大体成型（除了线程池），各个类的生命周期也大体上合适了，读者应该完全理解之前的服务器代码后再开始今天的学习。

观察当前的服务器架构，不难发现我们的Reactor模型少了最关键、最重要的一个模块：线程池。当发现socket fd有事件时，我们应该分发给一个工作线程，由这个工作线程处理fd上面的事件。而当前我们的代码是单线程模式，所有fd上的事件都由主线程（也就是EventLoop线程）处理，这是大错特错的，试想如果每一个事件相应需要1秒时间，那么当1000个事件同时到来，EventLoop线程将会至少花费1000秒来传输数据，还有函数调用等其他开销，服务器将直接宕机。

在之前的教程已经讲过，每一个Reactor只应该负责事件分发而不应该负责事件处理。今天我们将构建一个最简单的线程池，用于事件处理。

线程池有许多种实现方法，最容易想到的一种是每有一个新任务、就开一个新线程执行。这种方式最大的缺点是线程数不固定，试想如果在某一时刻有1000个并发请求，那么就需要开1000个线程，如果CPU只有8核或16核，物理上不能支持这么高的并发，那么线程切换会耗费大量的资源。为了避免服务器负载不稳定，这里采用了固定线程数的方法，即启动固定数量的工作线程，一般是CPU核数（物理支持的最大并发数），然后将任务添加到任务队列，工作线程不断主动取出任务队列的任务执行。

关于线程池，需要特别注意的有两点，一是在多线程环境下任务队列的读写操作都应该考虑互斥锁，二是当任务队列为空时CPU不应该不断轮询耗费CPU资源。为了解决第一点，这里使用`std::mutex`来对任务队列进行加锁解锁。为了解决第二个问题，使用了条件变量`std::condition_variable`。

> 关于`std::function`、`std::mutex`和`std::condition_variable`基本使用方法本教程不会涉及到，但读者应当先熟知，可以参考欧长坤《现代 C++ 教程》

线程池定义如下：

```c
class ThreadPoll {
private:
    std::vector<std::thread> threads;
    std::queue<std::function<void()>> tasks;
    std::mutex tasks_mtx;
    std::condition_variable cv;
    bool stop;
public:
    ThreadPoll(int size = 10);  // 默认size最好设置为std::thread::hardware_concurrency()
    ~ThreadPoll();
    void add(std::function<void()>);
};
```

当线程池被构造时：

```c
ThreadPoll::ThreadPoll(int size) : stop(false){
    for(int i = 0; i < size; ++i){  //  启动size个线程
        threads.emplace_back(std::thread([this](){  //定义每个线程的工作函数
            while(true){    
                std::function<void()> task;
                {   //在这个{}作用域内对std::mutex加锁，出了作用域会自动解锁，不需要调用unlock()
                    std::unique_lock<std::mutex> lock(tasks_mtx);
                    cv.wait(lock, [this](){     //等待条件变量，条件为任务队列不为空或线程池停止
                        return stop || !tasks.empty();
                    });
                    if(stop && tasks.empty()) return;   //任务队列为空并且线程池停止，退出线程
                    task = tasks.front();   //从任务队列头取出一个任务
                    tasks.pop();
                }
                task();     //执行任务
            }
        }));
    }
}
```

当我们需要添加任务时，只需要将任务添加到任务队列：

```c
void ThreadPoll::add(std::function<void()> func){
    { //在这个{}作用域内对std::mutex加锁，出了作用域会自动解锁，不需要调用unlock()
        std::unique_lock<std::mutex> lock(tasks_mtx);
        if(stop)
            throw std::runtime_error("ThreadPoll already stop, can't add task any more");
        tasks.emplace(func);
    }
    cv.notify_one();    //通知一次条件变量
}
```

在线程池析构时，需要注意将已经添加的所有任务执行完，最好不采用外部的暴力kill、而是让每个线程从内部自动退出，具体实现参考源代码。

这样一个最简单的线程池就写好了，在源代码中，当`Channel`类有事件需要处理时，将这个事件处理添加到线程池，主线程`EventLoop`就可以继续进行事件循环，而不在乎某个socket fd上的事件处理。

至此，今天的教程已经结束，一个完整的Reactor模式才正式成型。这个线程池只是为了满足我们的需要构建出的最简单的线程池，存在很多问题。比如，由于任务队列的添加、取出都存在拷贝操作，线程池不会有太好的性能，只能用来学习，正确做法是使用右值移动、完美转发等阻止拷贝。另外线程池只能接受`std::function<void()>`类型的参数，所以函数参数需要事先使用`std::bind()`，并且无法得到返回值。针对这些缺点，将会在明天的教程进行修复。

完整源代码：[https://github.com/yuesong-feng/30dayMakeCppServer/tree/main/code/day10](https://github.com/yuesong-feng/30dayMakeCppServer/tree/main/code/day10)

## day11-完善线程池，加入一个简单的测试程序

在昨天的教程里，我们添加了一个最简单的线程池到服务器，一个完整的Reactor模式正式成型。这个线程池只是为了满足我们的需要构建出的最简单的线程池，存在很多问题。比如，由于任务队列的添加、取出都存在拷贝操作，线程池不会有太好的性能，只能用来学习，正确做法是使用右值移动、完美转发等阻止拷贝。另外线程池只能接受`std::function<void()>`类型的参数，所以函数参数需要事先使用`std::bind()`，并且无法得到返回值。

为了解决以上提到的问题，线程池的构造函数和析构函数都不会有太大变化，唯一需要改变的是将任务添加到任务队列的`add`函数。我们希望使用`add`函数前不需要手动绑定参数，而是直接传递，并且可以得到任务的返回值。新的实现代码如下：

```c
template<class F, class... Args>
auto ThreadPool::add(F&& f, Args&&... args) -> std::future<typename std::result_of<F(Args...)>::type> {
    using return_type = typename std::result_of<F(Args...)>::type;  //返回值类型

    auto task = std::make_shared< std::packaged_task<return_type()> >(  //使用智能指针
            std::bind(std::forward<F>(f), std::forward<Args>(args)...)  //完美转发参数
        );  
        
    std::future<return_type> res = task->get_future();  // 使用期约
    {   //队列锁作用域
        std::unique_lock<std::mutex> lock(tasks_mtx);   //加锁

        if(stop)
            throw std::runtime_error("enqueue on stopped ThreadPool");

        tasks.emplace([task](){ (*task)(); });  //将任务添加到任务队列
    }
    cv.notify_one();    //通知一次条件变量
    return res;     //返回一个期约
}
```

这里使用了大量C++11之后的新标准，具体使用方法可以参考欧长坤《现代 C++ 教程》。另外这里使用了模版，所以不能放在cpp文件，因为C++编译器不支持模版的分离编译

> 这是一个复杂的问题，具体细节请参考《深入理解计算机系统》有关编译、链接的章节

此外，我们希望对现在的服务器进行多线程、高并发的测试，所以需要使用网络库写一个简单的多线程高并发测试程序，具体实现请参考源代码，使用方式如下：

```bash
./test -t 10000 -m 10 (-w 100)
# 10000个线程，每个线程回显10次，建立连接后等待100秒开始发送消息（可用于测试服务器能同时保持的最大连接数）。不指定w参数，则建立连接后开始马上发送消息。
```

注意Makefile文件也已重写，现在使用make只能编译服务器，客户端、测试程序的编译指令请参考Makefile文件，服务器程序编译后可以使用vscode调试。也可以使用gdb调试：

```bash
gdb server  #使用gdb调试
r           #执行
where / bt  #查看调用栈
```

今天还发现了之前版本的一个缺点：对于`Acceptor`，接受连接的处理时间较短、报文数据极小，并且一般不会有特别多的新连接在同一时间到达，所以`Acceptor`没有必要采用epoll ET模式，也没有必要用线程池。由于不会成为性能瓶颈，为了简单最好使用阻塞式socket，故今天的源代码中做了以下改变：

1. Acceptor socket fd（服务器监听socket）使用阻塞式
2. Acceptor使用LT模式，建立好连接后处理事件fd读写用ET模式
3. Acceptor建立连接不使用线程池，建立好连接后处理事件用线程池

至此，今天的教程已经结束了。使用测试程序来测试我们的服务器，可以发现并发轻松上万。这种设计架构最容易想到、也最容易实现，但有很多缺点，具体请参考陈硕《Linux多线程服务器编程》第三章，在明天的教程中将使用one loop per thread模式改写。

此外，多线程系统编程是一件极其复杂的事情，比此教程中的设计复杂得多，由于这是入门教程，故不会涉及到太多细节，作者也还没有水平讲好这个问题。但要想成为一名合格的C++程序员，高并发编程是必备技能，还需要年复一年地阅读大量书籍、进行大量实践。

> 路漫漫其修远兮，吾将上下而求索    ———屈原《离骚》

完整源代码：[https://github.com/yuesong-feng/30dayMakeCppServer/tree/main/code/day11](https://github.com/yuesong-feng/30dayMakeCppServer/tree/main/code/day11)

## day12-将服务器改写为主从Reactor多线程模式

在上一天的教程，我们实现了一种最容易想到的多线程Reactor模式，即将每一个Channel的任务分配给一个线程执行。这种模式有很多缺点，逻辑上也有不合理的地方。比如当前版本线程池对象被`EventLoop`所持有，这显然是不合理的，线程池显然应该由服务器类来管理，不应该和事件驱动产生任何关系。如果强行将线程池放进`Server`类中，由于`Channel`类只有`EventLoop`对象成员，使用线程池则需要注册回调函数，十分麻烦。

> 更多比较可以参考陈硕《Linux多线程服务器编程》第三章

今天我们将采用主从Reactor多线程模式，也是大多数高性能服务器采用的模式，即陈硕《Linux多线程服务器编程》书中的one loop per thread模式。

此模式的特点为：

1. 服务器一般只有一个main Reactor，有很多个sub Reactor。
2. 服务器管理一个线程池，每一个sub Reactor由一个线程来负责`Connection`上的事件循环，事件执行也在这个线程中完成。
3. main Reactor只负责`Acceptor`建立新连接，然后将这个连接分配给一个sub Reactor。

此时，服务器有如下成员：

```c
class Server {
private:
    EventLoop *mainReactor;     //只负责接受连接，然后分发给一个subReactor
    Acceptor *acceptor;                     //连接接受器
    std::map<int, Connection*> connections; //TCP连接
    std::vector<EventLoop*> subReactors;    //负责处理事件循环
    ThreadPool *thpool;     //线程池
};
```

在构造服务器时：

```c
Server::Server(EventLoop *_loop) : mainReactor(_loop), acceptor(nullptr){ 
    acceptor = new Acceptor(mainReactor);   //Acceptor由且只由mainReactor负责
    std::function<void(Socket*)> cb = std::bind(&Server::newConnection, this, std::placeholders::_1);
    acceptor->setNewConnectionCallback(cb);

    int size = std::thread::hardware_concurrency();     //线程数量，也是subReactor数量
    thpool = new ThreadPool(size);      //新建线程池
    for(int i = 0; i < size; ++i){
        subReactors.push_back(new EventLoop());     //每一个线程是一个EventLoop
    }

    for(int i = 0; i < size; ++i){
        std::function<void()> sub_loop = std::bind(&EventLoop::loop, subReactors[i]);
        thpool->add(sub_loop);      //开启所有线程的事件循环
    }
}
```

在新连接到来时，我们需要将这个连接的socket描述符添加到一个subReactor中：

```c
int random = sock->getFd() % subReactors.size();    //调度策略：全随机
Connection *conn = new Connection(subReactors[random], sock);   //分配给一个subReactor
```

这里有一个很值得研究的问题：当新连接到来时应该分发给哪个subReactor，这会直接影响服务器效率和性能。这里采用了最简单的hash算法实现全随机调度，即将新连接随机分配给一个subReactor。由于socket fd是一个`int`类型的整数，只需要用fd余subReactor数，即可以实现全随机调度。

这种调度算法适用于每个socket上的任务处理时间基本相同，可以让每个线程均匀负载。但事实上，不同的业务传输的数据极有可能不一样，也可能受到网络条件等因素的影响，极有可能会造成一些subReactor线程十分繁忙，而另一些subReactor线程空空如也。此时需要使用更高级的调度算法，如根据繁忙度分配，或支持动态转移连接到另一个空闲subReactor等，读者可以尝试自己设计一种比较好的调度算法。

至此，今天的教程就结束了。在今天，一个简易服务器的所有核心模块已经开发完成，采用主从Reactor多线程模式。在这个模式中，服务器以事件驱动作为核心，服务器线程只负责mainReactor的新建连接任务，同时维护一个线程池，每一个线程也是一个事件循环，新连接建立后分发给一个subReactor开始事件监听，有事件发生则在当前线程处理。这种模式几乎是目前最先进、最好的服务器设计模式，本教程之后也会一直采用此模式。

虽然架构上已经完全开发完毕了，但现在我们还不算拥有一个完整的网络库，因为网络库的业务是写死的`echo`服务，十分单一，如果要提供其他服务，如HTTP服务、FTP服务等，需要重新开发、重新写代码，这打破了通用性原则。我们希望将服务器业务处理也进一步抽象，实现用户特例化，即在`main`函数新建`Server`的时候，可以自己设计、绑定相应的业务，在之后的教程将会实现这一功能。

完整源代码：[https://github.com/yuesong-feng/30dayMakeCppServer/tree/main/code/day12](https://github.com/yuesong-feng/30dayMakeCppServer/tree/main/code/day12)

## day13-C++工程化、代码分析、性能优化

在之前的教程里，我们已经完整开发了一个主从Reactor多线程的服务器的核心架构，接下来的开发重心应该从架构转移到细节。在这之前，将整个项目现代化、工程化是必要的，也是必须的。

C++项目工程化的第一步，一定是使用CMake。目前将所有文件都放在一个文件夹，并且没有分类。随着项目越来越复杂、模块越来越多，开发者需要考虑这座屎山的可读性，如将模块拆分到不同文件夹，将头文件统一放在一起等。对于这样复杂的项目，如果手写复杂的Makefile来编译链接，那么将会相当负责繁琐。我们应当使用CMake来管理我们的项目，CMake的使用非常简单、功能强大，会帮我们自动生成Makefile文件，使项目的编译链接更加容易，程序员可以将更多的精力放在写代码上。

> C++的编译、链接看似简单，实际上相当繁琐复杂，具体原理请参考《深入理解计算机系统（第三版）》第七章。如果没有CMake，开发一个大型C++项目，一半的时间会用在编译链接上。

我们将核心库放在`src`目录下，使用网络库的测试程序放在`test`目录下，所有的头文件放在`/include`目录下：

```
set(PINE_SRC_INCLUDE_DIR ${PROJECT_SOURCE_DIR}/src/include)
set(PINE_TEST_INCLUDE_DIR ${PROJECT_SOURCE_DIR}/test/include)
include_directories(${PINE_SRC_INCLUDE_DIR} ${PINE_TEST_INCLUDE_DIR})
```

实现头文件的`.cpp`文件则按照模块放在`src`目录（这个版本还未拆分模块到不同文件夹）。

`src`目录是网络库，并没有可执行的程序，我们只需要将这个网络库的`.cpp`文件编译链接成多个目标文件，然后链接到一个共享库中：

```
file(GLOB_RECURSE pine_sources ${PROJECT_SOURCE_DIR}/src/*.cpp)
add_library(pine_shared SHARED ${pine_sources})
```

在编译时，根据不同环境设置编译参数也很方便：

```
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fPIC -Wall -Wextra -std=c++17 -pthread")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wno-unused-parameter -Wno-attributes") #TODO: remove
set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -O0 -ggdb -fsanitize=address -fno-omit-frame-pointer -fno-optimize-sibling-calls")
set(CMAKE_EXE_LINKER_FLAGS  "${CMAKE_EXE_LINKER_FLAGS} -fPIC")
```

使用`test`目录下的`.cpp`文件创建可执行文件的代码：

```
foreach (pine_test_source ${PINE_TEST_SOURCES})
    get_filename_component(pine_test_filename ${pine_test_source} NAME)
    string(REPLACE ".cpp" "" pine_test_name ${pine_test_filename})

    add_executable(${pine_test_name} EXCLUDE_FROM_ALL ${pine_test_source})
    add_dependencies(build-tests ${pine_test_name})
    add_dependencies(check-tests ${pine_test_name})

    target_link_libraries(${pine_test_name} pine_shared)

    set_target_properties(${pine_test_name}
        PROPERTIES
        RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin"
        COMMAND ${pine_test_name}
    )
endforeach(pine_test_source ${PINE_TEST_SOURCES})
```

注意我们切换到了更强大更好用的clang编译器（之前是GCC）。

配置好CMake和clang后，还需要做以下三件事：

1. format：作为一个大型C++项目，可能有许多程序员共同开发，每个人的编码习惯风格都不同，整个项目可能风格杂乱，可读性差，不利于项目维护。所以在写C++代码时应该遵守一些约定，使代码的风格统一。目前比较流行的C++代码风格有google、llvm等，本项目采用google风格。
2. cpplint：基于google C++编码规范的静态代码分析工具，可以查找代码中错误、违反约定、建议修改的地方。
3. clang-tidy：clang编译器的代码分析工具，功能十分强大。既可以查找代码中的各种静态错误，还可以提示可能会在运行时发生的问题。不仅如此，还可以通过代码分析给出可以提升程序性能的建议。

这三件事可以保证我们写出风格一致、bug较少、性能较好、遵守google编码规范的项目，是开发大型C++项目必备的利器。

为了很方便地自动一键运行，这三个工具都已经以`python`脚本的格式保存在了`build_support`目录：

```
build_support
    - clang_format_exclusions.txt     // 不需要格式化的代码
    - run_clang_format.py             // format
    - cpplint.py                      // cpplint
    - run_clang_tidy_extra.py         // 帮助文件，不直接运行
    - run_clang_tidy.py               // clang-tidy
.clang-format                         // format配置
.clang-tidy                           // clang-tidy配置
```

format在CMakeLists.txt中的配置：

```
# runs clang format and updates files in place.
add_custom_target(format ${PINE_BUILD_SUPPORT_DIR}/run_clang_format.py
        ${CLANG_FORMAT_BIN}
        ${PINE_BUILD_SUPPORT_DIR}/clang_format_exclusions.txt
        --source_dirs
        ${PINE_FORMAT_DIRS}
        --fix
        --quiet
        )
```

cpplint在CMakeLists.txt中的配置：

```
add_custom_target(cpplint echo '${PINE_LINT_FILES}' | xargs -n12 -P8
        ${CPPLINT_BIN}
        --verbose=2 --quiet
        --linelength=120
        --filter=-legal/copyright,-build/include_subdir,-readability/casting
        )
```

clang-tidy在CMakeLists.txt中的配置：    

```
add_custom_target(clang-tidy
        ${PINE_BUILD_SUPPORT_DIR}/run_clang_tidy.py # run LLVM's clang-tidy script
        -clang-tidy-binary ${CLANG_TIDY_BIN}        # using our clang-tidy binary
        -p ${CMAKE_BINARY_DIR}                      # using cmake's generated compile commands
        )
```

这里省略了文件夹定义等很多信息，完整配置在源代码中。

接下来尝试编译我们的项目，首先创建一个`build`文件夹，防止文件和项目混在一起：

```
mkdir build
cd build
```

然后使用CMake生成Makefile：

```
cmake ..
```

生成Makefile后，使用以下命令进行代码格式化:

```
make format
```

然后用cpplint检查代码:

```
make cpplint
```

最后使用clang-tidy进行代码分析：

```
make clang-tidy
```

将所有的警告都修改好，重新运行这三个命令直到全部通过。然后使用`make`指令即可编译整个网络库，会被保存到`lib`文件夹中，但这里没有可执行文件。如果我们需要编译可执行服务器，需要编译`test`目录下相应的源文件:

```
make server
make multiple_client
make single_client
```

生成的可执行文件在`build/test`目录下，这时使用`./test/server`即可运行服务器。

至此，今天的教程已经结束了。今天我们将整个项目工程化，使用了CMake、format、cpplint、clang-tidy，代码的风格变成了google-style，修复了之前版本的许多bug，应用了这些工具给我们提供的现代C++项目建议，性能也提高了。在今天的版本，所有的类也都被声明为不可拷贝、不可移动。clang-tidy提示的按值传参也被修改为引用传参，减少了大量的复制操作。这些工具建议的修改都大大降低了bug发生的几率、提高了服务器性能，虽然还没有用任何的性能测试工具，服务器的处理速度、吞吐量、并发支持度都明显提高了。

完整源代码：[https://github.com/yuesong-feng/30dayMakeCppServer/tree/main/code/day13](https://github.com/yuesong-feng/30dayMakeCppServer/tree/main/code/day13)

## day14-支持业务逻辑自定义、完善Connection类

回顾之前的教程，可以看到服务器Echo业务的逻辑在`Connection`类中。如果我们需要不同的业务逻辑，如搭建一个HTTP服务器，或是一个FTP服务器，则需要改动`Connection`中的代码，这显然是不合理的。`Connection`类作为网络库的一部分，不应该和业务逻辑产生联系，业务逻辑应该由网络库用户自定义，写在`server.cpp`中。同时，作为一个通用网络库，客户端也可以使用网络库来编写相应的业务逻辑。今天我们需要完善`Connection`类，支持业务逻辑自定义。

首先来看看我们希望如何自定义业务逻辑，这是一个echo服务器的完整代码：

```c
int main() {
  EventLoop *loop = new EventLoop();
  Server *server = new Server(loop);
  server->OnConnect([](Connection *conn) {  // 业务逻辑
    conn->Read();
    std::cout << "Message from client " << conn->GetSocket()->GetFd() << ": " << conn->ReadBuffer() << std::endl;
    if (conn->GetState() == Connection::State::Closed) {
      conn->Close();
      return;
    }
    conn->SetSendBuffer(conn->ReadBuffer());
    conn->Write();
  });
  loop->Loop(); // 开始事件循环
  delete server;
  delete loop;
  return 0;
}
```

这里新建了一个服务器和事件循环，然后以回调函数的方式编写业务逻辑。通过`Server`类的`OnConnection`设置lambda回调函数，回调函数的参数是一个`Connection`指针，代表服务器到客户端的连接，在函数体中可以书写业务逻辑。这个函数最终会绑定到`Connection`类的`on_connect_callback_`，也就是`Channel`类处理的事件（这个版本只考虑了可读事件）。这样每次有事件发生，事件处理实际上都在执行用户在这里写的代码逻辑。

关于`Connection`类的使用，提供了两个函数，分别是`Write()`和`Read()`。`Write()`函数表示将`write_buffer_`里的内容发送到该`Connection`的socket，发送后会清空写缓冲区；而`Read()`函数表示清空`read_buffer_`，然后将TCP缓冲区内的数据读取到读缓冲区。

在业务逻辑中，`conn->Read()`表示从客户端读取数据到读缓冲区。在发送回客户端之前，客户端有可能会关闭连接，所以需要先判断`Connection`的状态是否为`Closed`。然后将写缓冲区设置为和读缓冲区一样的内容`conn->SetSendBuffer(conn->ReadBuffer())`，最后调用`conn->Write()`将写缓冲区的数据发送给客户端。

可以看到，现在`Connection`类只有从socket读写数据的逻辑，与具体业务没有任何关系，业务完全由用户自定义。

在客户端我们也希望使用网络库来写业务逻辑，首先来看看客户端的代码：

```c
int main() {
  Socket *sock = new Socket();
  sock->Connect("127.0.0.1", 1234);
  Connection *conn = new Connection(nullptr, sock);
  while (true) {
    conn->GetlineSendBuffer();
    conn->Write();
    if (conn->GetState() == Connection::State::Closed) {
      conn->Close();
      break;
    }
    conn->Read();
    std::cout << "Message from server: " << conn->ReadBuffer() << std::endl;
  }
  delete conn;
  return 0;
}
```

注意这里和服务器有很大的不同，之前设计的`Connection`类显然不能满足要求，所以需要完善`Connection`。

首先，这里没有服务器和事件循环，仅仅使用了一个裸的`Connection`类来表示从客户端到服务器的连接。所以此时`Read()`表示从服务器读取到客户端，而`Write()`表示从客户端写入到服务器，和之前服务器的`Conneciont`类方向完全相反。这样`Connection`就可以同时表示Server->Client或者Client->Server的连接，不需要新建一个类来区分，大大提高了通用性和代码复用。

其次，客户端`Connection`没有绑定事件循环，所以将第一个参数设置为`nullptr`表示不使用事件循环，这时将不会有`Channel`类创建来分配到`EventLoop`，表示使用一个裸的`Connection`。因此业务逻辑也不用设置服务器回调函数，而是直接写在客户端代码中。

另外，虽然服务器到客户端（Server->Client）的连接都使用非阻塞式socket IO（为了搭配epoll ET模式），但客户端到服务器（Client->Server）的连接却不一定，很多业务都需要使用阻塞式socket IO，比如我们当前的echo客户端。之前`Connection`类的读写逻辑都是非阻塞式socket IO，在这个版本支持了非阻塞式读写，代码如下：

```c
void Connection::Read() {
  ASSERT(state_ == State::Connected, "connection state is disconnected!");
  read_buffer_->Clear();
  if (sock_->IsNonBlocking()) {
    ReadNonBlocking();
  } else {
    ReadBlocking();
  }
}
void Connection::Write() {
  ASSERT(state_ == State::Connected, "connection state is disconnected!");
  if (sock_->IsNonBlocking()) {
    WriteNonBlocking();
  } else {
    WriteBlocking();
  }
  send_buffer_->Clear();
}
```

ps.如果连接是从服务器到客户端，所有的读写都应采用非阻塞式IO，阻塞式读写是提供给客户端使用的。

至此，今天的教程已经结束了。教程里只会包含极小一部分内容，大量的工作都在代码里，请务必结合源代码阅读。在今天的教程中，我们完善了`Connection`类，将`Connection`类与业务逻辑完全分离，业务逻辑完全由用户自定义。至此，我们的网络库核心代码已经完全脱离了业务，成为一个真正意义上的网络库。今天我们也将`Connection`通用化，同时支持Server->Client和Client->Server，使其可以在客户端脱离`EventLoop`单独绑定socket使用，读写操作也都支持了阻塞式和非阻塞式两种模式。

到今天，本教程已经进行了一半，我们开发了一个真正意义上的网络库，使用这个网络库，只需要不到20行代码，就可以搭建一个echo服务器、客户端（完整程序在`test`目录）。但这只是一个最简单的玩具型网络库，需要做的工作还很多，在今后的教程里，我们会对这个网络库不断完善、不断提升性能，使其可以在生产环境中使用。

完整源代码：[https://github.com/yuesong-feng/30dayMakeCppServer/tree/main/code/day14](https://github.com/yuesong-feng/30dayMakeCppServer/tree/main/code/day14)

## day15-macOS、FreeBSD支持

作为程序员，使用MacBook电脑作为开发机很常见，本质和Linux几乎没有区别。本教程的EventLoop中使用Linux系统支持的epoll，然而macOS里并没有epoll，取而代之的是FreeBSD的kqueue，功能和使用都和epoll很相似。Windows系统使用WSL可以完美编译运行源代码，但MacBook则需要Docker、云服务器、或是虚拟机，很麻烦。在今天，我们将支持使用kqueue作为`EventLoop`类的Poller，使网络库可以在macOS等FreeBSD系统上原生运行。

在网络库已有的类当中，`Socket`和`Epoll`类是最底层的、需要和操作系统打交道，而上一层的`EventLoop`类只是使用`Epoll`提供的接口，而不关心`Epoll`类的底层实现。所以在考虑支持不同的操作系统时，只应该改变最底层的`Epoll`类，而不需要改动上层的`EventLoop`类。至于分发`fd`的`Channel`类，可以自定义epoll和kqueue的读、写、ET模式等事件，在`Channel`类中只需要注册好我们自定义的事件，然后在`Poller`类中将事件注册到epoll或kqueue。

```c
const int Channel::READ_EVENT = 1;
const int Channel::WRITE_EVENT = 2;
const int Channel::ET = 4;
```

需要注意`Channel`的用户自定义事件必须是1、2、4、8、16等十进制数，因为在`Poller`中判断、更新事件时需要用到按位与、按位或等操作，这里实际上是将16位二进制数的每一位用作标志位。如果这里理解有困难，可以先学一遍《深入理解计算机系统（第三版）》.

在`Poller`类中使用宏定义的形式判断当前操作系统，从而使用不同的代码:

```c
#ifdef OS_LINUX
// linux平台的代码
#endif

#ifdef OS_MACOS
// FreeBSD平台的代码
#endif
```

操作系统宏在CMakeLists.txt中定义：

```
if (CMAKE_SYSTEM_NAME MATCHES "Darwin")
    message(STATUS "Platform: macOS")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -DOS_MACOS")
elseif (CMAKE_SYSTEM_NAME MATCHES "Linux")
    message(STATUS "Platform: Linux")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -DOS_LINUX")
endif()
```

这样就可以在不同的操作系统使用不同的代码。如注册/更新`Channel`，在Linux系统下会编译以下代码：

```c
void Poller::UpdateChannel(Channel *ch) {
  int sockfd = ch->GetSocket()->GetFd();
  struct epoll_event ev {};
  ev.data.ptr = ch;
  if (ch->GetListenEvents() & Channel::READ_EVENT) {
    ev.events |= EPOLLIN | EPOLLPRI;
  }
  if (ch->GetListenEvents() & Channel::WRITE_EVENT) {
    ev.events |= EPOLLOUT;
  }
  if (ch->GetListenEvents() & Channel::ET) {
    ev.events |= EPOLLET;
  }
  if (!ch->GetExist()) {
    ErrorIf(epoll_ctl(fd_, EPOLL_CTL_ADD, sockfd, &ev) == -1, "epoll add error");
    ch->SetExist();
  } else {
    ErrorIf(epoll_ctl(fd_, EPOLL_CTL_MOD, sockfd, &ev) == -1, "epoll modify error");
  }
}
```

而在macOS系统下会编译以下代码：

```c
void Poller::UpdateChannel(Channel *ch) {
  struct kevent ev[2];
  memset(ev, 0, sizeof(*ev) * 2);
  int n = 0;
  int fd = ch->GetSocket()->GetFd();
  int op = EV_ADD;
  if (ch->GetListenEvents() & ch->ET) {
    op |= EV_CLEAR;
  }
  if (ch->GetListenEvents() & ch->READ_EVENT) {
    EV_SET(&ev[n++], fd, EVFILT_READ, op, 0, 0, ch);
  }
  if (ch->GetListenEvents() & ch->WRITE_EVENT) {
    EV_SET(&ev[n++], fd, EVFILT_WRITE, op, 0, 0, ch);
  }
  int r = kevent(fd_, ev, n, NULL, 0, NULL);
  ErrorIf(r == -1, "kqueue add event error");
}
```

在今天的教程中，我们支持了MacOS、FreeBSD平台。在代码中去掉了`Epoll`类，改为通用的`Poller`，在不同的平台会自适应地编译不同的代码。同时我们将`Channel`类和操作系统脱离开来，通过用户自定义事件来表示监听、发生的事件。现在在Linux和macOS系统中，网络库都可以原生编译运行。但具体功能可能会根据操作系统的不同有细微差异，如在macOS平台下的并发支持度明显没有Linux平台高，在后面的开发中会不断完善。

完整源代码：[https://github.com/yuesong-feng/30dayMakeCppServer/tree/main/code/day15](https://github.com/yuesong-feng/30dayMakeCppServer/tree/main/code/day15)