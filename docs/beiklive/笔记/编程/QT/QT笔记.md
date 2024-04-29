---
comments: true
---

## 开机自启动

??? note "宏定义"
```C++
#define AUTO_RUN "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run"
    ```
    
??? note "设置自启动和关闭自启动"

```C++
void PopupClock::SetAutoStart(bool flag) {
	QSettings settings(AUTO_RUN, QSettings::NativeFormat);

	//以程序名称作为注册表中的键,根据键获取对应的值（程序路径）
	QFileInfo fInfo(QApplication::applicationFilePath());
	QString name = fInfo.baseName();    //键-名称

	//如果注册表中的路径和当前程序路径不一样，则表示没有设置自启动或本自启动程序已经更换了路径
	QString oldPath = settings.value(name).toString(); //获取目前的值-绝对路经
	QString newPath = QDir::toNativeSeparators(QApplication::applicationFilePath());    //toNativeSeparators函数将"/"替换为"\"
	if (flag)
	{
		if (oldPath != newPath)
			settings.setValue(name, newPath);
	}
	else {
		settings.remove(name);
	}
	m_pActionAutoStart->setChecked(checkAutoStart());
}
```

??? note "检查是否有自启动"
```C++
bool PopupClock::checkAutoStart() {
	QSettings settings(AUTO_RUN, QSettings::NativeFormat);
	QFileInfo fInfo(QApplication::applicationFilePath());
	QString name = fInfo.baseName();
	QString oldPath = settings.value(name).toString();
	QString newPath = QDir::toNativeSeparators(QApplication::applicationFilePath());
	return (settings.contains(name) && newPath == oldPath);
}
    ```


## linux命令行安装QT
```bash
sudo apt-get install qt5-default qtcreator -y
```



## pro文件解析

直接参考这篇博客：https://blog.csdn.net/wzz953200463/article/details/124107110



## QT的Git Action

仓库 https://github.com/jaredtao/HelloActions-Qt
说明： https://zhuanlan.zhihu.com/p/92733295/

## QT在线安装器下载加速
### 方法一
创建安装器的快捷方式，然后在快捷方式的路径后面添加参数
（推荐）新版本的安装器（4.0.1-1 后）支持 `--mirror` 命令行参数。
### 方法二
在命令行中启动安装器，添加 `--mirror https://mirrors.ustc.edu.cn/qtproject` 参数。
例如 Windows 下执行当前目录的安装器的命令为 
```shell
.\qt-unified-windows-x86-online.exe --mirror https://mirrors.ustc.edu.cn/qtproject
```