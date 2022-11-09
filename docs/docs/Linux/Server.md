---
comments: true
---

## Code Server搭建

项目地址: [https://github.com/cdr/code-server](https://github.com/cdr/code-server)

下载
```
wget https://github.com/cdr/code-server/releases/download/v3.10.2/code-server-3.10.2-linux-amd64.tar.gz
```

解压
```
tar -xvf code-server-3.10.2-linux-amd64.tar.gz
```

运行
1. 设置密码的环境变量
    ```
    export PASSWORD="xxxxxxx"
    ```
2. 进入`bin`目录，运行
    ```
    cd bin/
    ./code-server --port 8888 --host 0.0.0.0 --auth password 
    ```
    8888是端口,可以修改,注意要到服务器控制台打开相应端口,0.0.0.0是代表可以被所有ip访问

后台运行
```
nohup ./code-server --port 8888 --host 0.0.0.0 --auth password > ser.log 2>&1 &
```