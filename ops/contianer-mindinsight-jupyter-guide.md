# 在代码开发环境使用mindinsight工具指导

```
##====================================================
## Update： 2022/03/28
## Dependence： Mindpsore <= v1.6, MindInsight <= v1.6.1
## License: Apulis License (MIT)
##====================================================
```

## Step 1. 创建代码开发环境
 
可以按需求创建 Arm 代码开发环境。（具体操作略）

## Step 2. 更新配置mindinsight

对于MindInsight 1.6.1 及以上版本，默认host为`127.0.0.1`，不支持k8s pod, 需更新`HOST = '0.0.0.0'`

```
#!/bin/bash
# license port
HOSTPORT=8080
# summary log path
OUTPUTPATH=$HOME/outputs
# reload interval time
INTERVAL=5
pip install -U mindinsight
sed -i "s/HOST = '127.0.0.1'/HOST = '0.0.0.0'/g"  $HOME/.local/lib/python3.7/site-packages/mindinsight/conf/constants.py
mindinsight start --port $HOSTPORT --summary-base-dir $OUTPUTPATH --reload-interval $INTERVAL
```

## Step 3. 访问MindInsight的WEB面板

1. 打开 AIARTS -> 项目 -> [用户代码开发环境]
2. 新增交互式端口 `8080` ， 用户可根据需要指定其他端口
3. 点击操作中的`打开`

即可在新打开的WEB标签页中，浏览MindInsight面板。

## Step 4. 状态确认及维护

当出现以下提示，就表示MindInsight启用成功
```
Workspace: /home/demo-developer/mindinsight
Summary base dir: /home/demo-developer
Web address: http://0.0.0.0:8080
service start state: success
```

### 停止 MindInsight

*port* 号与启动时的保持一致。

`mindinsight stop --port 8080`  

### 指定工作目录，日志加载间隔
```
--reload-interval <RELOAD_INTERVAL> # 默认 3s
--summary-base-dir <LogDIr> # 默认 ~/summary_base
# Example
```
`mindinsight start --port 8080 --summary-base-dir $HOME/output --reload-interval 5`

### 收集日志

**MindInsight 仅支持框架 Mindspore**, 需要在Mindspore的训练脚本中配置callback方法 SummaryCollector自动收集；
或是结合Summary算子和SummaryCollector，自定义收集网络中的数据。

* 详细说明请参考：[收集Summary数据](https://www.mindspore.cn/mindinsight/docs/zh-CN/r1.5/summary_record.html)

## 高阶使用，根据华为的MindInsight镜像配置，其使用了 gunicorn 提供服务。

Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX. It's a pre-fork worker model. The Gunicorn server is broadly compatible with various web frameworks, simply implemented, light on server resources, and fairly speedy.

* 参考链接: [gunicorn](https://gunicorn.org/#deployment)
