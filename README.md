# 数学与计算机调研学习

计算机基于量度规则模拟计算，以数据呈现世界声音，图像，文件。

人们在认知环宇的时候，创造了语言符合文字，包含描述性符号和计量符号，用于记录和阐述事物的相关性和计量关系。

语义和计量可以按照已有规则和符号相互表示，人们习惯用语义符合和规则交流沟通，用计量规则符合进行演算预测。

``` 
调研方法框架，调研平台系统：

宣榜-接单 + 地图 + 行业统计数据 + 事务状态

调研归档-文库（数据库和存储）

推荐清单
```
1. 算法训练题，当前以 C/Rust/Python 为主。
2. Mook，参考书籍的源码分别建立了工程目录。
3. 按组件功能分类的对比分析,范例在根目录下。

更新计划：
    1. 将 Cpp 换为linux类 unix 下执行
    2. App, GUI放在具体开源应用
    3. 该 notebook 支持多种解释性语言
    4. 方便期间还是保留了VisualStudio, Xcode 工程

## 目录描述：

    ./AI AI算法和框架
    ./Algorithms 数据结构和算法教程代码目录，对比整理。
    ./CallAnother 不同编程语言接口调用，如python <=> C
    ./Configuration 配置管理如 Yaml, json, configration files等
    ./CookBook jupyter notebooks  案例集锦，面试相关问题(按照 leetcode题型做了基本分类还包含 CoderByte，Kaggle 等)
        ./Algiorithms 案例集锦，面试相关算法题
        ./Scripts bash脚本（awk,sed,grep）
        ./SQL SQL优化
        ./MultProcess 线程进程问题
    ./DataAnalysis 数据处理和分析
    ./DB  Mysql,sqlitter,redis, postgresql, mongodb数据库
    ./DesignPatterns  设计模式
    ./Draw  绘图
    ./Distributed 分布式相关
    ./docs 一些 pdf 文档
    ./FrameworkServices  Web框架
    ./Game 游戏
    ./GUI 图形开发
    ./LanguageSong 语言或语音处理
    ./MicrosoftOffice 文档处理方法，包含VBA宏脚本
    ./NetworkProtocal 网络协议TCP/UDP/HTTP/WEBSOCKETS对比
    ./PicturesVideo 图形和视频处理
    ./MultiProcess 进程线程，协程
    ./Spider 爬虫对比
    ./System 系统操作
    ./VersionDevOps WEB部署CI/CD
    ./Jupyter_notebook_config.py notebook配置
    ./VisualStudioCpp (windows MinGW环境) 汇总编篡《编篡珠玑 Programing Pearls SecindEditon》《编篡之美 Beauty Of Prpgraming》
         《算法基础与在线实践—北京大学“程序设计与算法”慕课》和《算法精讲—C语言描述》C/C++基础算法数据结构的实例。
    ./XcodeCpp (Mac OS Gnu环境) 汇总编篡《算法导论—Third Edition》《Unix/Linux编篡实践教程》和《问题求解和程序设计—第六版》C/C++算法数据结构实例。
    ./Jupyter_notebook_systemd.service 操作系统下使用 systemctl 管理服务  

文档库管理
----------------------------------------------------        
* Jupyter notebook： 同步到github; 

```
# 修改根目录下的 jupyter_notebook_systemd.service 中的 post_save_hook 要同步的 branch，一般是非 master 的。
post_save_hook 同步 github 方式：

* post_save_hook(model=model, os_path=os_path, contents_manager=cm)

# 在 Jupyter notebook 编辑保存后触发

* github webhook 在其他分支有提交或合并时，需要自定义实现扩展 API 支持 
[File save hooks](https://jupyter-notebook.readthedocs.io/en/stable/extending/savehooks.html?highlight=hook)

```

* 设置 systemd service

```
# 将根目录下的 jupyter_notebook_systemd.service 拷贝到 /etc/systemd/system （以 centos 7 为例）路径下

cp -f ./jupyter_notebook_systemd.service /etc/systemd/system/jupyter.service

# systemctl reload config , 这一步系统会自动提示。
# 通过 systemctl start/stop/restart jupyter 

systemctl start jupyter 

```
  *不同系统下 bash 所在路径可能不同，以及登录用户可能不同，需要记得更新！*

* 最后注意，jupyter.service 启动时读取的是根目录下的 jupyter_notebook_config.py, 如果部署环境或路径改变，需要修改其中的 c.NotebookApp.notebook_dir ,当然在配置中我并没有启用它。

*在Github.io 配置页面，不要使用 Jekyll theme。*

* 相关主题会整理发布到CSDN Blog：https://blog.csdn.net/banrieen

* javaascript 扩展安装注意：
    + 在当前非 root 用户（jupyter 也是在非 root 下启动）下，npm 安装包不要使用 sudo ，否则安装在 root 下将无法使用，衍生很多问题；
    + ijskernel 找不到的问题，请执行 ijsinstall  --spec-path=full （不要带 sudo）;
    + 扩展安装信息查询  jupyter kernelspec list --json ;
    + ijavascript 安装提示 zeromq prerbuild问题，请采用这种方式安装 npm install -g  --unsafe-perm ijavascript;
    

参考库索引
---------------------------------------------------- 

1. [算法精解 C语言描述（Mastering-Algorithms-with-C）案例代码库](https://github.com/banrieen/Mastering-Algorithms-with-C

2. [C++ 算法大全](https://github.com/banrieen/The-Algorithms-With-C-Plus-Plus)

3. [Jeff Erickson Algorithms ](https://github.com/jeffgerickson/algorithms)

4. [Python 核心编程第二版](https://github.com/banrieen/Core-Python-Programming-2nd-Edition-Examples-and-Source-Code)

  4.1 [http://corepython.com/cpp3ev2](https://github.com/banrieen/CPAP)

5. [Python 算法实现](https://github.com/TheAlgorithms/Python)

6. [程序员面试笔记](https://github.com/yangshun/tech-interview-handbook)

7. [程序员面试笔记](https://github.com/jwasham/coding-interview-university)

8. [安全扫描-OWASP ZAP](https://github.com/zaproxy/zaproxy)

9. [ERP-ODOO](https://github.com/odoo/odoo)

10. [bitcoin core](https://github.com/banrieen/bitcoin)

11. [微信小程序开发示例](https://github.com/wechat-miniprogram/miniprogram-demo)

12. [阿布量化交易系统](https://github.com/bbfamily/abu)
