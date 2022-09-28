---
comments: true
---

# 创建快捷方式

## 进入图标文件目录
```bash
$ cd /usr/share/applications
```
## 创建图标文件
```bash
$ sudo vim myapp.desktop
```
## 输入图标相关信息
```bash
[Desktop Entry]
Encoding=UTF-8      #应用名称为中文时需要添加此行
Name=AutoScript     # 应用名称，配置完成后图标会显示为此处设置的名字
Comment=to start my app   #应用的解释信息
Exec=/home/ubuntu/tools/myscript.sh    #应用或者脚本的启动命令或目录
Icon=/home/ubuntu/tools/ICON/picacomic_2.png    #应用图标，不要使用ico格式
Terminal=true          # 启动命令行程序时是否显示終端
StartupNotify=true      # 启动通知
Type=Application        # 类型
Categories=Application; # 分类
```


# 分区挂载
## VMware磁盘扩容
[https://www.likecs.com/show-203437057.html](https://www.likecs.com/show-203437057.html)





# Samba配置

## 安装

```bash
sudo apt-get install samba samba-common
```



## 设置共享目录

```bash
mkdir /home/beiklive/share
sudo chmod 777 /home/beiklive/share
```

## 添加用户

```bash
sudo smbpasswd -a beiklive
```

## 修改配置文件

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

## 重启

```bash
sudo service smbd restart
```















