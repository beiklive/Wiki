---
comments: true
---

## 使用systemctl启动服务

创建service文件
```shell
sudo vim /lib/systemd/system/xxx.service
```
写入以下内容
```
[Unit]
Description=fraps service
After=network.target syslog.target
Wants=network.target

[Service]
Type=simple
#启动服务的命令,使用绝对路径， 此处以frp为例
ExecStart=/your/path/frps -c /your/path/frps.ini

[Install]
WantedBy=multi-user.target
```
启动
```shell
sudo systemctl start xxx
```
打开自启动
```
sudo systemctl enable xxx
```

* 重启应用 `sudo systemctl restart xxx`

* 停止应用 `sudo systemctl stop xxx`

* 查看应用的日志 `sudo systemctl status xxx`


其他服务后台运行方法
[https://blog.csdn.net/x7418520/article/details/81077652](https://blog.csdn.net/x7418520/article/details/81077652)

***


## Code Server搭建

项目地址: [https://github.com/cdr/code-server](https://github.com/cdr/code-server)

下载
```shell
wget https://github.com/cdr/code-server/releases/download/v3.10.2/code-server-3.10.2-linux-amd64.tar.gz
```

解压
```shell
tar -xvf code-server-3.10.2-linux-amd64.tar.gz
```

运行
1. 设置密码的环境变量
    ```shell
    export PASSWORD="xxxxxxx"
    ```
2. 进入`bin`目录，运行
    ```shell
    cd bin/
    ./code-server --port 8888 --host 0.0.0.0 --auth password 
    ```
    8888是端口,可以修改,注意要到服务器控制台打开相应端口,0.0.0.0是代表可以被所有ip访问

后台运行
```shell
nohup ./code-server --port 8888 --host 0.0.0.0 --auth password > ser.log 2>&1 &
```


## Samba配置

### 安装

```bash
sudo apt-get install samba samba-common
```



### 设置共享目录

```bash
mkdir /home/beiklive/share
sudo chmod 777 /home/beiklive/share
```

### 添加用户

```bash
sudo smbpasswd -a beiklive
```

### 修改配置文件

```bash
sudo vim /etc/samba/smb.conf
```

尾部添加

```
[share]
comment = share folder
browseable = yes
path = /home/beiklive/share
create mask = 0700
directory mask = 0700
valid users = beiklive
force user = beiklive
force group = beiklive
public = yes
available = yes
writable = yes
```

### 重启

```bash
sudo service smbd restart
```