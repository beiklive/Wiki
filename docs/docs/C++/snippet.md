---
comments: true
---

## Socket通信模板
```c title="server.cpp" linenums="1"
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
```c title="client.cpp" linenums="1"
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

## git钩子

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
