---
comments: true
---

## 与 MkDocs 联动使用

### obsidian存储库初始化
初始化位置需要选在 `MkDocs` 项目的 `docs` 目录下

![](asserts/Pasted%20image%2020240506094757.png)

之后按照自己的需要的目录结构，在 存储库中创建文件夹，并在 `mkdocs.yml` 中配置页面路由

![](asserts/Pasted%20image%2020240506095340.png)

### obsidian设置

在 `文件与链接` 中进行如下修改

![](asserts/Pasted%20image%2020240506095552.png)


1. 内部链接类型修改为 `基于当前笔记的相对路径`
2. 使用 Wiki 链接项 设置为关闭， 否则会使用obsidian的语法导致mkdocs找不到文件
3. 附件默认存放路径改为 `当前文件苏哟在文件夹下的指定子文件夹`，子文件夹名称我这里设置为了 `asserts`

![](asserts/Pasted%20image%2020240506095623.png)
![](asserts/Pasted%20image%2020240506095628.png)