# icml-deploy

## 需要更改的部分
在EcnuThread.py文件中，把要运行的程序写在run函数中。

### 说明：
EcnuThread.py文件中定理了全局变量： axioms, symbols, outputs

axioms和symbols运行时是已知的，把生成的定理添加到outputs中即可

## 部署命令：

### 进入scripts目录下
```cd ~/icml-deplpy/scripts```
### 运行部署脚本
```bash setup.sh```

之后将test/目录下的submission.py中的base_url变量，改为本机的ip，只提交submission.py这个文件的zip压缩包即可

## 日志查看：
在imcl-deply/logs中保存着部署时的日志文件