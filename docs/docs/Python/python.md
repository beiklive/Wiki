---
comments: true
---

## 中文编码支持

```bash
# -*- coding: utf-8 -*-  
```
## PIP相关
**换源**
常用的国内镜像包括：
>（1）阿里云 http://mirrors.aliyun.com/pypi/simple/

>（2）豆瓣http://pypi.douban.com/simple/ 

>（3）清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/

>（4）中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/

>（5）华中科技大学http://pypi.hustunique.com/

临时换源
```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pandas
```
永久换源
```
（a）Linux下，修改 ~/.pip/pip.conf (没有就创建一个文件夹及文件。文件夹要加“.”，表示是隐藏文件夹)
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host = https://pypi.tuna.tsinghua.edu.cn

(b) windows下，直接在user目录中创建一个pip目录，如：C:\Users\xx\pip，然后新建文件pip.ini，即 %HOMEPATH%\pip\pip.ini，在pip.ini文件中输入以下内容：
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host = https://pypi.tuna.tsinghua.edu.cn
```
## selenium使用
安装：
```bash
pip install selenium
```
相关代码
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

# chrome_driver=r"C:\Python310\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"
# driver=webdriver.Chrome(executable_path=chrome_driver)
driver=webdriver.Chrome()
driver.get(url)   #获取当前url   driver.current_url
# 查找元素
userName_tag = driver.find_element(By.ID, 'tbLoginName')
res = driver.find_element(By.XPATH, "//li[text()='导出为']")
# 输入内容
userName_tag.send_keys('100019050')
# 点击
res.click()
```
判断元素存在
```python
from selenium.common.exceptions import NoSuchElementException
# 元素是否存在 is_element_present(driver, By.XPATH, "//div[text()='回收站']")
def is_element_present(driver, type, value):
    try:
        id = driver.find_element(type, value)
    except NoSuchElementException as e:
        return False
    return True
```
双击动作
```python
from  selenium.webdriver.common.action_chains import ActionChains
ActionChains(driver).double_click(driver.find_element_by_name(“name”)).perform()
```
指定缓存目录，保留登陆状态
```python
# 目录路径在：chrome://version/   个人资料路径
option = webdriver.ChromeOptions()
option.add_argument('--user-data-dir=/home/dongjie/.config/google-chrome')
driver = webdriver.Chrome(options = option)
```
## log日志
```python
import logging

logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")
```
日志级别
```python
logging.basicConfig(level=logging.DEBUG)  #默认只显示warning及以上
```
日志格式
```python
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(format=LOG_FORMAT)
#2017-05-08 14:29:53,783 - DEBUG - This is a debug log.
#2017-05-08 14:29:53,784 - INFO - This is a info log.
#2017-05-08 14:29:53,784 - WARNING - This is a warning log.
#2017-05-08 14:29:53,784 - ERROR - This is a error log.
#2017-05-08 14:29:53,784 - CRITICAL - This is a critical log.
```
日期格式
```python
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(datefmt=DATE_FORMAT)
```
输出到文件
```python
logging.basicConfig(filename='my.log')
```
## tornado
命令行参数
```python
from tornado.options import define, options

define("port", default=8011, help="运行端口", type=int)
define("uarg", default='/gitlab-push', help="网页路由", type=str)
define("script", default='./gitlab-hook.sh', help="hook脚本", type=str)
define("isExecute", default='true', help="控制是否执行脚本", type=str)

print(options.port)
```
使用
```bash
python app.py --port=3000 --script="myscript.sh" --uarg="/post" --isExecute="false"
```

## 解析yaml
test.yml如下
```yaml
# 用户名
user_name: tinker

# 日期
date: 2022-02-21

# user_name_list
user_name_list:
 - user_name: Tom
 - user_name: Jack
 - user_name: tinker
```
解析代码如下
```python
#!/usr/bin/python
# vim: set fileencoding:utf-8
import os

import yaml

# 获取yaml文件路径
yamlPath = os.path.join("D:\\test\\", "config.yml")

# open方法打开直接读出来
f = open(yamlPath, 'r', encoding='utf-8')
cfg = f.read()

params = yaml.load(cfg, Loader=yaml.SafeLoader)

user_name = params['user_name']
plan_date = params['date'] if params['date'] is not None else ''
user_name_list = params['user_name_list']

print(user_name)
print(plan_date)

for element in user_name_list:
    print(element.get('user_name'))
```

## 监控文件目录变化
安装
```bash
pip3 install watchdog
```

代码
```python
import sys
import time
import logging

from watchdog.observers import Observer
from watchdog.events import *


# 处理器
class FileEventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)

    def on_created(self, event):
        if event.is_directory:
            pass
        else:
            print("file created:{0}".format(event.src_path))

if __name__=='__main__':
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = FileEventHandler()
    observer = Observer()
    observer.schedule(event_handler,'./test', recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
```

输出
```bash
file created:./test/1/q.txt
```

## 图片处理
使用流行的是 Pillow 模块，可以在下面找到优化图像所需的大部分方法。
```python
# Image Optimizing
# pip install Pillow
import PIL
# Croping 
im = PIL.Image.open("Image1.jpg")
im = im.crop((34, 23, 100, 100))
# Resizing
im = PIL.Image.open("Image1.jpg")
im = im.resize((50, 50))
# Flipping
im = PIL.Image.open("Image1.jpg")
im = im.transpose(PIL.Image.FLIP_LEFT_RIGHT)
# Rotating
im = PIL.Image.open("Image1.jpg")
im = im.rotate(360)
# Compressing
im = PIL.Image.open("Image1.jpg")
im.save("Image1.jpg", optimize=True, quality=90)
# Bluring
im = PIL.Image.open("Image1.jpg")
im = im.filter(PIL.ImageFilter.BLUR)
# Sharpening
im = PIL.Image.open("Image1.jpg")
im = im.filter(PIL.ImageFilter.SHARPEN)
# Set Brightness
im = PIL.Image.open("Image1.jpg")
im = PIL.ImageEnhance.Brightness(im)
im = im.enhance(1.5)
# Set Contrast
im = PIL.Image.open("Image1.jpg")
im = PIL.ImageEnhance.Contrast(im)
im = im.enhance(1.5)
# Adding Filters
im = PIL.Image.open("Image1.jpg")
im = PIL.ImageOps.grayscale(im)
im = PIL.ImageOps.invert(im)
im = PIL.ImageOps.posterize(im, 4)
# Saving
im.save("Image1.jpg")
```
## 视频优化
使用 Moviepy 模块，允许你修剪、添加音频、设置视频速度、添加 VFX 等等。
```python
# Video Optimizer
# pip install moviepy
import moviepy.editor as pyedit
# Load the Video
video = pyedit.VideoFileClip("vid.mp4")
# Trimming
vid1 = video.subclip(0, 10)
vid2 = video.subclip(20, 40)
final_vid = pyedit.concatenate_videoclips([vid1, vid2])
# Speed up the video
final_vid = final_vid.speedx(2)
# Adding Audio to the video
aud = pyedit.AudioFileClip("bg.mp3")
final_vid = final_vid.set_audio(aud)
# Reverse the Video
final_vid = final_vid.fx(pyedit.vfx.time_mirror)
# Merge two videos
vid1 = pyedit.VideoFileClip("vid1.mp4")
vid2 = pyedit.VideoFileClip("vid2.mp4")
final_vid = pyedit.concatenate_videoclips([vid1, vid2])
# Add VFX to Video
vid1 = final_vid.fx(pyedit.vfx.mirror_x)
vid2 = final_vid.fx(pyedit.vfx.invert_colors)
final_vid = pyedit.concatenate_videoclips([vid1, vid2])
# Add Images to Video
img1 = pyedit.ImageClip("img1.jpg")
img2 = pyedit.ImageClip("img2.jpg")
final_vid = pyedit.concatenate_videoclips([img1, img2])
# Save the video
final_vid.write_videofile("final.mp4")
```

## PDF 转图片
使用流行的 PyMuPDF 模块，该模块以其 PDF 文本提取而闻名。
```python
# PDF to Images
# pip install PyMuPDF
import fitz
def pdf_to_images(pdf_file):
    doc = fitz.open(pdf_file)
    for p in doc:
        pix = p.get_pixmap()
        output = f"page{p.number}.png"
        pix.writePNG(output)
pdf_to_images("test.pdf")
```

## 下载器
```python
# Python Downloader
# pip install internetdownloadmanager
import internetdownloadmanager as idm
def Downloader(url, output):
    pydownloader = idm.Downloader(worker=20,
                                part_size=1024*1024*10,
                                resumable=True,)
 
    pydownloader .download(url, output)
Downloader("Link url", "image.jpg")
Downloader("Link url", "video.mp4")
```

