---
comments: true
---

# QML笔记

## 变量

#### 类型

```
property type name : value
```

变量类型

* int	   `property int num_value : 1`
* real      `property real real_value : 0.5`
* string   `property string str_value : "hellow QML"`
* color    `property color colorvalue : "black"`
* url         `property url myUrl : "qrc:/1.jpg"`

组件类型

```
property Componet : myComponent
property Rectangle : myRect
```

特殊类型‘

```
property var myVar: ["123", 1, "hello"]
property list<Rectrangle> myList
```

#### 属性

* readyonly 使变量不可被修改

```
readyonly property int num_value : 1
```

* required  变量必须被赋值

```
required property Componet : myComponent
```

* alias 取别名,将属性暴露给调用对象

```
property alias newinnerRect : innerRect
property alias newinnerRectColor : innerRect.color
```

