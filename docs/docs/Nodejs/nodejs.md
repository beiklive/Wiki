---
comments: true
---

# 后台运行nodejs应用

```javascript title="创建一个启动程序run.js"
const { exec } = require('child_process')
exec('这里写程序启动的命令',(error, stdout, stderr) => {
if(error){
        console.log('exec error: ${error}')
        return
}
console.log('stdout: ${stdout}');
console.log('stderr: ${stderr}');
})
```
```bash title="启动run.js"
pm2 start run.js
```