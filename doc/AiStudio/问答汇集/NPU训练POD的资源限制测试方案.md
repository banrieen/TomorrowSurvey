# 资源集群中NPU训练节点的POD资源限制配置的测试方案

* 文档说明

   + 产品: V1.5.0
   + 时间: 2021-01-15
   + 创建者：thomas

## 新增需求相关信息

**类型：** Hotfix

**需求背景：** openlab 客户使用平台（beta验收测试）过程中遇到平台响应有卡顿，推断是管理面与业务面网络没有分层，训练POD没有资源限制；是已知待完善问题。

**实现方案:**

1. 优先实现了NPU环境中worker节点上的POD资源限制；
2. 限制策略为预留系统基础使用的 50G MEM
3. 剩余资源按照节点最大可承载的任务（单卡）数8平均分配： 88G mem, 24核CPU；

**相关影响：** 任务调度，pod的资源初始分配，运行资源限制，资源回收，平台同时可建的任务容量;

**待完善部分：**  GPU节点资源限制（管理），Master节点资源管理，基于NPU卡数或GPU卡数的匹配的资源限制。

## 测试规划设计

**测试特性：** 功能可用性，平台可靠性

**测试环境：** openlab生产环境（1xAmd64 master + 2xArm64x8p NPU worker）

**主要测试方法：** 单机单卡 pod，单机多卡pod，多机pod中模拟资源占用是否（突破）有限制；单个节点的最大pod数(单机多卡pod)的数限制；满负载的pod销毁（stop & delete）;pod,node满负载运行；

**相关测试工具、脚本和数据：** Grafana Jobstatus，Nodestatus; 后台物理机，pod中top，free等；预置模型、数据集和脚本；stress模拟测试脚本

**风险：**

1. openlab 环境仅有2个NPU节点，单机多卡，多机分布式任务不能共存；
2. master节点没有做资源管理，平台访问卡顿的问题还有可能存在；
3. 客户生产环境不便于安装额外的组件工具（无法预估对环境的影响），主要在pod中模拟验证。

## 测试单（测试用例） http://apulis.zentaopm.com/testtask-cases-19.html

1. 创建0卡的代码开发环境，使用脚本模拟100%CPU,MEM占用，通过平台grafana观察 Jobstatus，Nodestatus;在 后台物理机，pod中观察top，free等，观察平台响应，jupyter响应等。
2. 创建1，2，4，8卡的代码开发环境，使用脚本模拟100%CPU,MEM占用，通过平台grafana观察 Jobstatus，Nodestatus;在 后台物理机，pod中观察top，free等，观察平台响应，jupyter响应等。
3. 创建2x8x1的16个单卡，2x4x2的8个2卡，2x2x4的4个4卡代码开发环境，使用脚本模拟100%CPU,MEM占用，通过平台grafana观察 Jobstatus，nodestatus;在 后台物理机，pod中观察top，free等，观察平台响应，jupyter响应等。
4. 创建2x8的双机分布式代码开发环境，使用脚本模拟100%CPU,MEM占用，通过平台grafana观察 Jobstatus，Nodestatus;在 后台物理机，pod中观察top，free等，观察平台响应，jupyter响应等。
5. 按照以上组合在模型训练中执行，使用脚本模拟100%CPU,MEM占用，通过平台grafana观察 Jobstatus，nodestatus;在 后台物理机，pod中观察top，free等，观察平台响应，jupyter响应等。
6. 使用提供的模型、数据和训练脚本执行以上组合，通过平台grafana观察 Jobstatus，nodestatus;在 后台物理机，pod中观察top，free等，观察平台响应，jupyter响应等。
7. 使用客户出现问题的模型、数据和训练脚本执行以上组合，通过平台grafana观察 Jobstatus，nodestatus;在 后台物理机，pod中观察top，free等，观察平台响应，jupyter响应等。
8. 创建2x8x1的16个单卡模型训练或代码开发任务，长时间执行客户训练案例，观察平台响应，jupyter响应等。
9. 在已有node创建1x8个pod，继续创建新的pod，新pod是否在不停止其他pod释放资源前可以被调度执行起来
10. 检查后台restfullapi的配置是否生效

```bash
# cd /root/install/InstallationYTung/
# cat roles/aiarts-service/templates/restfulapi.yaml.j2
resource_limit:
huawei_npu_arm64:  # device_type
cpu:    24
memory: 88Gi
```

## 测试结果

## 已发现问题

1. BUG 1836【NPU-POD资源限制】平台资源NPU没有占用的情况，批量创建16个开发环境，worker02 节点有3个POD调度失败，vocana异常
2. BUG 1835【NPU-POD资源限制】仅在代码开发环境创建一个POD执行测试脚本，（Jupyter 出现不响应，）平台响应出现卡顿
3. BUG 1837【NPU-POD资源限制】批量创建16个模型训练，和16个模拟测试的（将训练脚本替换为测试脚本）模型训练，出现任务执行失败
4. BUG 1838【NPU-POD资源限制】POD的资源限制为24核CPU,88G内存，实际测试能占用48核CPU，93G 内存
5. BUG 1832【NPU-POD资源限制】在模拟测试之后，专家系统的集群监控不可访问

## 遗留和待确认或存在风险的情况

BUG  1836 待环境释放后跟踪定位。
1. 内存超过上线，（K8S）容器会自动将内存使用最高的用户进程kill掉，不符适合客户使用，但是目前技术有限。
2. 目前是限制POD资源，没有匹配NPU卡数，那么1卡，2卡，4卡，8卡训练的pod的资源限制都是24cores,88Gi
3. 周末验证中满16 POD场景，会将节点CPU,MEM资源全部占尽，会影响平台运转！

## **附录**

### **openlab管理信息**

* WEB: http://183.129.171.130:8461

  ACCOUNT: admin > PASSWD: 70aiYt

支持账号： apulisops apulisops@18c

```bash
sshpass -p 39hjxfJ/     ssh root@183.129.171.130 -p 7448  
sshpass -p qUu8/u-o     ssh root@183.129.171.130 -p 7449  
sshpass -p Atlas@12#$   ssh root@192.168.88.23  
```

* 更新配置：
    ```bash
    cd /root/install/InstallationYTung/
    vim roles/aiarts-service/templates/restfulapi.yaml.j2
    resource_limit:
    huawei_npu_arm64:  # device_type
        cpu:    1
        memory: 88Gi

    # 重启相关组件
    ./service_ctl.sh restart  restfulapi2
    ./service_ctl.sh restart  jobmanager2
    #渲染后的配置：
    cat /root/build/restfulapi2/config.yaml 
    ```
* worker节点的资源配置，**POD能够看到的裸机全部资源**

**CPU Cores：**

lscpu | egrep 'Model name|Socket|Thread|NUMA|CPU\(s\)'
CPU(s):              192
On-line CPU(s) list: 0-191
Thread(s) per core:  1
Socket(s):           4
NUMA node(s):        8
NUMA node0 CPU(s):   0-23
NUMA node1 CPU(s):   24-47
NUMA node2 CPU(s):   48-71
NUMA node3 CPU(s):   72-95
NUMA node4 CPU(s):   96-119
NUMA node5 CPU(s):   120-143
NUMA node6 CPU(s):   144-167
NUMA node7 CPU(s):   168-191

**MEM：**

free -m
total        used        free      shared  buff/cache   available
Mem:         773739        8490      761357           5        3892      761795
Swap:             0           0           0

free -g
total        used        free      shared  buff/cache   available
Mem:            755           8         743           0           3         743
Swap:             0           0           0

* Pytorch 模型训练问题，还没有顺利执行

**Openlab 上周反馈的5个问题：http://apulis.zentaopm.com/bug-browse-13.html** 

Bug 1840: http://apulis.zentaopm.com/bug-view-1840.html 需待Pytorch训练调试完成后再定位处理
  