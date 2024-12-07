# 微软小冰-人工智能平台使用指导和问答（Guide & Solution）

* CustomerPlatform: AiArts v1.6 +
* Date: 2021-07+ 
* Supportor: Thomas.Bian
* Environment: 微软小冰
* Process: 开发调试-训练
* Host: http://47.93.5.220/
* Account: "admin/XXXXXX"
* RemoteConnection: ""
* Environment:
    - 阿里云GPU服务器
    - 阿里云NAS
    
## 客户需求(Customer-Requirements):
* 组内用户资源和权限管理
* 管理员任务监控和调度
* 2021-0922 【xiaohang】当2个节点分别有8卡，7卡空闲时，新任务是随机占用某个机器的卡，希望新任务优先选用7卡的节点

## 遗留问题(Legacy-Issues): 
* 当单机没有足够GPU,多机足够时，选择“非分布式训练”。平台进行调度，但一直调度不成功。希望此时提示用户单机卡不足够，应选择“分布式训练”
* 你们遇到是CPU,MEM利用不起来，还是个别训练任务CPU,MEM使用量奇高？你们现在开发或训练任务使用CPU，或内存有没有一些经验值，现在可以做全局的使用上限限制？
    - 内存这个主要还是看数据集，cpu需求主要看数据增强了，这个真不好给所有任务一个具体限制。  按照我以前用的平台经验，1 cpu对应10g内存，一般申请8-15cpu
    - 我们不同的任务，数据集大小不同。像我这边处理视频的话，就是有多少用多少，当然会限制dataloader的长度。我目前在跑的任务，一般来说num_worker=0的时候， 能够让GPU高效利用起来的batch_size只有16
* 2021-0922 【pengfei】有2个节点的卡用用户自己保存的image起GPU任务，报错： ImagePullBackOFF！ 
    - 这2个节点是他人任务结束后释放出来，已经在集群中，但是该节点的harbor host配置丢失，不能访问集群内的harbor
* 2021-0922 【pengfei】创建的模型训练任务，偶现没有日志打印；
    - 在后台进入pod查看有训练日志，但是WEB没有输出 
* 2021-0922 【yingying】启动文件为软链接时，报错找不到启动文件
    - 软连接的启动脚本在linux终端是可以执行，但是在平台创建训练任务窗口则报文件找不到
* 2021-0923 使用已保存的且用过的镜像，创建开发环境耗时14min
* 2021-0923 关于镜像环境的CPU申请
    - 之前应该有几位同事在跑pytorch dataloader时都遇到 “It is possible that dataloader's workers are out of shared memory. Please try to raise your shared memory limit.” 这类报错，原因是docker镜像中默认限制了shm（shared memory）解决办法是在Dataloader中将num_worker设置为0，但更好的解决办法是起Docker容器时，设置 --ipc=host 或 --shm-size
    - 因为在Dataloader中将num_worker设置为0 处理大量数据时，batch_size设大一点的话，GPU就要等CPU ，GPU的功耗就不能跑满
    - 没限制？那可能是因为CPU资源共享的，那这样的话，就算用docker的cpus选项做隔离也没用的，它不是物理层面的cpus隔离；但从平台登陆的话，直接就加载镜像了，不能人为设置shm-size。有什么办法在创建开发任务或者镜像环境时申请多核么 这样既不浪费我们本来挺好的CPU 又能把GPU功耗跑满
    - 我们不同的任务，数据集大小不同。像我这边处理视频的话，就是有多少用多少，当然会限制dataloader的长度。我目前在跑的任务，一般来说num_worker=0的时候， 能够让GPU高效利用起来的batch_size只有16
    - 内存这个主要还是看数据集，cpu需求主要看数据增强了，这个真不好给所有任务一个具体限制。  按照我以前用的平台经验，1 cpu对应10g内存，一般申请8-15cpu
* 平台没有部署完整：docker-hub镜像不能正常使用
* 用户保存大镜像2个59G的导致平台不能访问，
* 用户希望合并VC， 现在可以热扩容，修改数据库即可，不影响现在执行的任务
* 用户停止或删除任务，出现后台pod挂死的情况，需要后台手工处理
* 了解更详细的一些系统日志：看看你们那边的log能不能有更多信息；比如，为什么会调度不成功？ 是因为资源不够吗
* 急需扩容docker缓存空间，当用户增加时，存储空间占用会显著增加
* 监控告警没有配置和使用起来
* docker hub 镜像即使run起来，也因为缺少权限不能使用

* 镜像中vscode server 不能正常安装： 验证镜像，并更新一个最新的镜像 
    + 已经验证可用的镜像
        - tensorflow:1.14.0
        - horovod:0.20.0
        - mindpore-gpu:1.1.1
        - pytorch:1.5
        - pytorch/torchserve:latest
    + 基础镜像：nvcr.io/nvidia/pytorch:20.03-py3 
    + 使用镜像：xixiao/cudagl10.2-conda-torch:v0.4
* 环境出现任务偶尔失败，网络时尔中断的情况；排查使用的磁盘满了，训练IO比较大
    - 扩容master系统磁盘，增加定时数据集清理；凌飞今天还在处理，引导他们查看阿里云控制台，可以看到服务器的IO比较高，磁盘使用超过了80%；这个对数据库，镜像仓库，docker 和平台影响比较大，处理起来比较复杂，尤其是当清理docker缓存时可能会导致任务失败或平台不可访问
* 提供基础镜像问题
    - https://docs.nvidia.com/deeplearning/frameworks/pytorch-release-notes/index.html 他们的组合搭配 可以参考
    - 你们的预置镜像可以考虑常用深度学习框架+CUDA+Ubuntu 选较新的稳定版本
    框架
    - 我这里有一个干净的相对比较全的镜像可以用：zhongyingying_yyz_adnerf:0.4 (镜像ID：d8136a5a8e) cuda:11.1.1-cudnn8-devel-ubuntu18.04 + conda (conda env ad-nerf里装了pytorch 1.8.1和很全的cv的各种包, 不需要可以把这个虚拟环境删掉，只用前面的基础镜像）cuda:11.1.1-cudnn8-devel-ubuntu18.04-pytorch1.8.1
    - Nvidia 发布镜像
        + Refer: https://docs.nvidia.com/deeplearning/frameworks/pytorch-release-notes/rel_21-02.html#rel_21.02
        + docker pull nvcr.io/nvidia/pytorch:21.07-py3
        + ubuntu 20.04 启用ssh

## 现场已解决问题(Resolved-Problem):
* 每隔3天左右会有僵死任务占用卡 （后台清理）
* 模型开发案例
* 用户使用cuda官方镜像，反复多次不能正常启用
* 平台访问出现502， 后台数据库fail；恢复数据库后可访问了

* jupyter装了不同的conda环境 但是在建notebook时没有对应kernel可选
    + Anwser: 把kernel 加到/usr/local/就可以选了；之前在/root/.local下
* 用户文件挂载使用/mnt不能共享
* 怎么查看容器的资源使用率
* zhongyingying 个人镜像， 是否可以直接使用保存镜像的ID创建新的训练
* 你们现在开发或训练任务使用CPU，或内存有没有一些经验值，现在可以做全局的使用上限限制
    - 内存这个主要还是看数据集，cpu需求主要看数据增强了，这个真不好给所有任务一个具体限制。  按照我以前用的平台经验，1 cpu对应10g内存，一般申请8-15cpu



**BUG:**

没有平台所在系统盘，docker 缓存目录相关存储监控，和告警; 平台宕机后才能定位!!
postgres写日志异常!!
宕机，2个节点的kubelet异常
环境被黑，删除了数据

无意义的排队
资源监控信息不一致
后提交的任务反而跑起来了
服务器反复出现不可用状态
VC剩余GPU卡数一直在跳跃
Share_MEM限制
有3张没被占用的卡监控显示一直占用中
平台访问出现502， 
postgres down
ImagePullBackOFF
僵死任务占用卡，或
harbordown
后台清理harbor
新任务是随意占用某个机器的卡
找不到启动文件
没有执行权限
没有创建文件权限
偶现没有日志打印

**用户期望**
管理员可以批量管理所有人的任务
资源监控的展示面板
准确及时稳定的监控信息
能够按人，服务器顺序，卡顺序分配算力
数据，模型等完整的文件管理
单机多卡，多机多卡的执行性能，充分利用CPU,MEM，GPU
多人任务的碎片GPU归集
Remote SSH, Jupyter要稳定，顺畅
个人用户查看容器的资源使用率
在WEB释放僵死任务占用的GPU
拉取cuda镜像，拉取docker-hub镜像，超大镜像50G左右的
个人保存的镜像可以通过ID或名称共享给其他同事使用
可以直接使用的通用镜像
平台稳定性尽量不要出现502,不可访问等异常报错
模型训练可以重新执行
模型的导出
NAS的复用，可以挂在用户自己的在线存储
存储的监控告警和定时清理
直观简单的教程文档

AiStudio 更新优劣势：
AAA
组织管理
项目编排
数据仓库
镜像可视化管理组织管理
模型Hub
Jupyter Lab 
模型训练模板
模型评估
模型发布
模型部署：中心推理、边缘推理
AutoDL
大数据处理
机器学习案例


