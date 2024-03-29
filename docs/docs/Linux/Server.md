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

## ZFile搭建

项目地址： [https://docs.zfile.vip/](https://docs.zfile.vip/)

部署
```shell
export ZFILE_INSTALL_PATH=~/zfile                        # 声明安装到的路径
mkdir -p $ZFILE_INSTALL_PATH && cd $ZFILE_INSTALL_PATH   # 创建文件夹并进入
wget --no-check-certificate https://c.jun6.net/ZFILE/zfile-release.war          # 下载 zfile 最新版
unzip zfile-release.war && rm -rf zfile-release.war      # 解压并删除压缩包
chmod +x $ZFILE_INSTALL_PATH/bin/*.sh     
```

启动
```shell
~/zfile/bin/start.sh       # 启动
```

更新
```shell
~/zfile/bin/stop.sh                                                 # 停止程序
rm -rf ~/zfile                                                      # 删除安装文件夹

# 重新下载安装最新版
export ZFILE_INSTALL_PATH=~/zfile                                   # 声明安装到的路径
mkdir -p $ZFILE_INSTALL_PATH && cd $ZFILE_INSTALL_PATH              # 创建文件夹并进入
wget --no-check-certificate https://c.jun6.net/ZFILE/zfile-release.war                     # 下载 zfile 最新版
unzip zfile-release.war && rm -rf zfile-release.war                 # 解压并删除压缩包
chmod +x $ZFILE_INSTALL_PATH/bin/*.sh                               # 授权启动停止脚本

~/zfile/bin/start.sh                                                # 启动项目
```

配置文件
```shell
~/zfile/WEB-INF/classes/application.properties   # 端口号在这里修改
```



## Mysql安装配置

#### 卸载

```bash
sudo apt purge mysql-*
sudo rm -r /etc/mysql
sudo rm -r /var/lib/mysql
sudo apt autoremove
sudo apt autoclean
```

#### 安装

```bash
sudo apt-get update #更新软件源
sudo apt-get install mysql-server -y
sudo apt install mysql-client -y
sudo apt install libmysqlclient-dev -y
```

保证以上步骤无报错

#### 检查是否安装成功

```bash
ps -ef | grep mysql 
```

![image-20231005070317079](./img/image-20231005070317079.png)

#### 使用默认账户登录

```bash
sudo cat /etc/mysql/debian.cnf
```

![image-20231005070450375](./img/image-20231005070450375.png)

```bash
mysql -u debian-sys-maint -p
```

> 如果登录报错
>
> ![image-20231005070635225](./img/image-20231005070635225.png)
>
> ##### 1.设置允许无密码登录
>
> ```bash
> sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf
> ```
>
> 在 `[mysqld]`下添加
>
> ```
> skip-grant-tables
> ```
>
> ![image-20231005070846350](./img/image-20231005070846350.png)
>
> ##### 2.重启 MySQL
>
> ```bash
> service mysql restart
> ```
>
> ##### 3.登录 Mysql
>
> ```bash
> mysql -u root -p   # 输入密码时直接回车就行
> ```
>
> ##### 4.重新设置root账户密码
>
> ```mysql
> # 以下都是在 mysql 的命令行中执行
> use mysql;
> flush privileges;
> UPDATE user SET authentication_string='' WHERE user='root';
> flush privileges;
> alter user 'root'@'localhost' identified with mysql_native_password by 'password';
> quit;
> ```
>
> ##### 5.重启mysql
>
> 首先删除第一步中加入到 mysqld.cnf的那条语句
>
> 然后重启 mysql 服务
>
> ```bash
> service mysql restart
> ```
>
> ##### 6.使用修改后的账号密码登录
>
> ```bash
> mysql -u root -p
> ```