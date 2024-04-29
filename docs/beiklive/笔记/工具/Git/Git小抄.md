---
comments: true
---



## 投机取巧
### add和commit合并成一条命令

`git commit -am "提交描述"`

### add  commit push合并

```bash
git config --global alias.acp '!f() { git add -A && git commit -m "$@" && git push; }; f'
```
使用：
```bash
git asp "xxxxx"
```






## Git介绍

### 一、git是什么？

Git是目前世界上最先进的分布式版本控制系统(没有之一)，什么是版本控制？大白话就是可以控制每个人每一次提交，保证代码互不干扰，可进行历史记录查询、回退版本、分支合并，极大的提高了协同开发的效率

### 二、几大架构？重要

#### 本地缓存

一般指git clone后的状态，即将代码缓存cache到本地

#### 暂存区

一般指git add之后的状态，即将代码添加至暂存区

#### 本地仓库

一般指git commit之后的状态，即将代码提交到本地仓库

#### 远端仓库

一般指git push之后的状态，即将代码推送到在远端仓库





### 三、git命令？场景？

#### 1、查看

查看所有分支

```
git branch -a
```

查看分析信息

```
git branch -v
```

查看本地分支与远程分支关系

```
git branch -vv
```

查看本地与上一次暂存区的差异

```
git status
```

查看文件与上一次暂存区的差异。假设文件为test.py

```
git diff test.py
```

查看本地与远端仓库分支分支映射是否异常

```
git remote show origin
```

查看本地缓存序列

```
git stash list
```

查看stash缓存具体内容，数字0代表序列为0的缓存

```
git stash show stash@{0}
```

查看所在分支历史提交记录

```
git log
```

查看文件在git中的跟踪状态

```
git status -sb
```



#### 2、删除

删除git索引，删除本地文件。假设文件为test.txt

```
git rm test.txt
```

删除git索引，保留本地文件。假设文件为test.txt

```
git rm --cache test.txt
```

删除本地分支(常用)，假设分支为test

```
git branch -d test
```

强制删除本地分支，应用场景一般为合并不完全导致push失败，解决方案一般是强制删除未完全合并分支，重新从远端库拉取分支。假设分支为test

```
git status -D test
```

删除远端分支。假设远端分支为test

```
git push --delete origin test
```

删除某个缓存cache，数字0代表序列为0的缓存

```
git stash drop stash@{0}
```

删除所有缓存

```
git stash clear
```



#### 3、增加

将远端仓库拉取(映射)到本地。假设项目地址为test

```
git clone test
```

拉取远端库最新代码至本地

```
git pull
```

将本地仓库的修改提交到远端仓库

```
git push
```

将某个文件添加到暂存区。假设文件为test.txt

```
git add test.txt
```

将当前路径下的所有文件及目录添加到暂存区

```
git add .
```

新建本地分支(新分支索引模板即当前所在分支)。假设新分支名为test(切记不可与远端分支名重复，否则此操作不再是新建分支，而是拉取远端分支到本地)

```
git branch test
```

新建远程分支。假设本地/远程分支名都为test。分两步：①新建本地分支 ②推送到远端仓库
①`git branch test`
②`git push origin test:test` # 第一个test是本地分支名，第二个是远端分支名
新增cache缓存，数字0代表新增序列为0的缓存

```
git stash save 0
```

提交暂存区代码至本地仓库并添加备注信息。假设备注信息为test

```
git commit -m test
```



#### 4、修改

修改本地分支名字。假设当前分支名为oldName，修改后分支名为newName

```
git branch -m oldName newName
```

修改提交到本地仓库的备注信息

```
git commit --amend
```



#### 5、回退

将本地修改但未提交到缓存区的文件回退到未修改前的状态。假设文件为test.py

```
git restore test.py
```

将某个add(添加)到暂存区的文件回退到本地，但本地所做修改依旧存在。假设文件为test.py

```
git reset head test.py
```

将add(添加)到暂存区的所有文件回退到本地，但本地所做修改依旧存在

```
git restore --staged
```

commit提交回退后所有修改都不保留(慎用)

```
git reset --hard HEAD^
```

commit提交回退到add之前，保留本地修改，一般也用于分支回退(最常用)

```
git reset --mixed HEAD^
```

等同于

```
git reset HEAD^
```

commit提交回退到add之后，commit之前

```
git reset --soft HEAD^
```

将某个保存在缓存区的修改回退到当前分支，而且所有相关文件都变为未缓存状态。假设缓存序列为0

```
git stash apply stash@{0}
```

将某个保存在缓存区的修改回退到当前分支，但不修改已add(添加)到暂存区文件的状态。假设缓存序列为0

```
git stash apply stash@{0} --index
```

将最近的一次缓存区的修改回退到当前分支，相关文件都变为未缓存状态

```
git stash pop
```



#### 6、组合命令

新建本地分支并切换到新建分支。假设新建分支为test

```
git checkout -b test
```

添加本地修改至暂存区&提交到本地仓库。假设备注信息为test
注：本地修改不包含新文件(不在git跟踪范围)

```
git commit -am test
```



#### 7、合并

注：merge合并时，要变更的分支(即当前所处分支)内不应存在未commit的文件，否则会导致这些文件无法恢复到merge前的状态。解决方法是merge之前将其stash到缓存中，merge结束后pop再还原回来

不同分支合并某次commit提交(无需push，有commit号即可合并)。假设commit号为test001

```
git cherry-pick test001
```

单个分支将多次提交记录合并成一个提交记录。假设起始合并的commit号的上一个commit号为test001(包尾不包头)

```
git rebase -i test001
```

将dev分支修改信息合并到master(目前处于master分支中，将会修改master分支内容)

```
git merge dev
```



#### 8、补充

本地关联远程分支。假设本地分支名为test，远端分支名为ogn_test

```
git branch --set-upstream-to=origin/ogn_test test
```



```
git reset --merge
```

 退回merge之前
放弃合并并恢复到合并前的状态。网上有说相同效果如git reset --merge，其实这是老版本的语法，最新的语法合并回退命令如下：

```
git merge --abort
```



#### 9、场景

删除远端分支test
①、先将要删除的远端分支test拉到本地

```
git checkout test
```

②、切换到其它分支以便删除

```
git checkout dev
```

③、执行删除远端分支命令

```
git push --delete origin test
```

，须知，此时只是删除了远端分支，本地分支还存在，只是缺少了上游分支
④、输入账号密码确认删除操作·
删除在本地有但在远程库中已经不存在的分支
①、查看远端分支情况(是否删除)git remote show origin，输入账号密码确认查看
②、更新本地远程仓映射(即保持本地映射与远端仓对应)

```
git remote prune origin
```

远端分支更名
①、切换到其它分支

```
git checkout dev
```

②、先修改本地分支名字

```
git branch -m test newName
```

③、删除远端旧分支

```
git push --delete origin test
```

④、将新分支推远程仓库

```
git push origin newName
```

⑤、把修改后的本地分支与远程分支关联

```
git branch --set-upstream-to origin/newName
```

