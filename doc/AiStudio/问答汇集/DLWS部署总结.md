# 南京平台部署总结

这次在用户现场部署开放平台，得到了各位领导和相关同事的大力支持，海思生态组对接同事也非常配合我们协调华为研发帮忙调试问题，大家都是尽力
做好项目。但是我们没有预先沟通详细的设备和网络情况，海思同事对这块也了解不多，关键的多级多卡业务因缺少网络设备及相关局域网配置阻塞，
tensorflow训练任务由于NPU驱动更新镜像不可用阻塞；也花费了比较长的时间。其中有很多需要我们继续完善和借鉴，记录和总结如下，请大家参考，如有遗漏和
不正确的地方烦请指正下。


## 平台部署遇到的问题

1. 客户现场准备物料不足，导致多机环境无法部署

   + 建议后续进场部署前预先了解现场网络环境设备等信息，核对网络配置的 [Checklist](#网络预先确认项)。
   
   ```
   Review: Task 017
   跟踪和完善多级多卡业务的Checklist.
   ```

2. 没有预备系统，驱动等关键因素的变化措施，导致后续要重新编译镜像等，耗费一定时间

   1. 标准化镜像编译方法和流程
   2. 建立公司内使用的镜像库，完善镜像更新流程
   3. 支持客户端私有镜像库
   4. 同客户方预先沟通[系统版本配置](#集群基本信息预先确认项)和准备镜像

   ```
   Review: FeatureRequest 055
   标准化镜像编译的方法指导手册，运维（测试）团队接手；公司的镜像库区分开源和商业版本；提供客户自定以的镜像库（额外支持！）。
   ```

3. 公司组网较单一，各种(企业)网络环境考虑不周全，导致现场需手动调整安装部署K8s集群服务

   1. 维护公司的镜像库，和私有镜像库；
   2. 部署脚本能够优先同步本地私有镜像库->公司镜像库->公共docker hub
   ```
   Review: FeatureRequest 056
   1. 内网部署：SSD安装盘
   2. 本地镜像库，公司镜像库 ——天慧
   3. 调研国内公共镜像库的性能，网络稳定性 ——测试组
   ```
4. 码云代码管理不规范,尚有不确定的配置，或重复文件难以同步更新

   **代码中散落的文件,必须确认和梳理**

   1. 疑似重复文件：

        + src/dashboard/src/Job 与 src/dashboard/src/Jobs 与  src/dashboard/src/JobsV2 与  + src/dashboard/src/JobV2; 
        + src/dashboard 与  src/user-dashboard；
        + src/WebUI 与  src/WebUI2；  
        + src/docker-images/RepairManager 与  src/docker-images/RepairManager2 与  src/docker-images/RepairManagerEtcd；
        + src/docker-images/restfulAPI 与  src/docker-images/restfulapi2；
        + src/docker-images/WebUI 与  src/docker-images/WebUI 与  src/docker-images/webui3；

   2. dockerfile: 

        + devenv.arm/dockerfile; 
        + devenv/dockerfile; 
        + src/dashboard/dockerfile; 
        + src/user-synchronizer/dockerfile; 
        + src/dashboard/.dockerignore; 
        + src/docker-images/a910-device-plugin/example/resnet50/dockerfile; 
        + src/docker-images/a910-device-plugin/**/dockerfile <dockerfile.bak><.dockerignore>;
        + src/docker-images/**/dockerfile;
        + src/Jobs_Templete/user-synchronizer/dockerfile; 
        
   3. readme: 

        + src/ARM/readme.md；
        + src/ClusterManager/readme.md；
        + src/dashboard/readme.md; 
        + src/user-synchronizer/readme.md; 
        + src/docker-images/a910-device-plugin/readme.md; 
        + src/docker-images/cloudinit/readme.md; 
        + src/docker-images/openresty/readme.md; 
        + src/docker-images/RepairManager/readme.md; 
        + src/docker-images/RepairManager2/readme.md; 
        + src/docker-images/restfulapi2/readme.md; 
        + src/docker-images/WebUI/readme.md; 
        + src/docker-images/WebUI2/readme.md; 
        + src/docker-images/WebUI2/readme.md; 
        + src/Jobs_Templete/restfulapi/readme.md; 
        + src/Jobs_Templete/user-dashboard/readme.md; 
        + src/Jobs_Templete/WebUI/dotnet/readme.md; 
        + src/Jobs_Templete/WebUI2/dotnet/readme.md; 
        + src/RepairManager/readme.md; 
        + src/RestAPI/readme.md; 
        
    4. requirments: 

        + src/ClusterManager/requirments.txt; 
        + src/ClusterPortal/requirments.md; 
        + src/docker-images/init-container/requirments.md; 
        + src/Jobs_Templete/RepairManager/requirments.txt; 
        + src/RepairManager/requirments.txt;

    5. .gitignore: 

        + src/dashboard/.gitignore; 
        + src/dashboard/config/.gitignore; 
        + src/user-synchronizer/.gitignore; 
        + src/dashboard/src/configuration/.gitignore; 
        + src/docker-images/a910-device-plugin/example/resnet50/.gitignore;
        + src/docker-images/a910-device-plugin/.gitignore; 
        + src/docker-images/a910-device-plugin/azure-blob-adapter/.gitignore; 
        + src/Jobs_Templete/user-synchronizer/.gitignore; 
        
    6. bash脚本不加后缀： 

        + src/dashboard/dev-utils/intoj; 
        + src/dashboard/dev-utils/dlts_get_cmd; 
        + src/docker-images/influxdb/start; 
        + src/docker-images/init-container/ss-config/ssh; src/docker-images/init-container/ss-config/sshd;src/docker-images/init-container/ss-config/ssh-config; 
       ...

    7. 其他文件： src/ClusterManager/job_status.pdf; src/docker-images/binstore/000-default.conf ...

   ```
   Review: FeatureRequest 057
   9月4号，代码清洗，重新覆盖测试一遍。——后端，前端，测试

   ```
5. 训练/推理任务构建、任务启动都需要拉取公网资源，在网络条件受限情况下，影响启用Job
   
   + 建议增加客户环境的私有镜像库服务，预置经典模型镜像；参看 BugID: [634](https://apulis.zentaopm.com/bug-view-634.html),[633](https://apulis.zentaopm.com/bug-view-633.html)
   ```
   Review: Task 013
   内网部署，提交Job,训练模型能否全程执行完，要严格测试完成。——测试组

   ```
   

6. 部署过程，错误，警告提示太多，没有相应的状态提示

   + 建议优化安装部署脚本输出; 参看 BugId: [28](https://apulis.zentaopm.com/bug-view-28.html),[78](https://apulis.zentaopm.com/bug-view-78.html),[79](https://apulis.zentaopm.com/bug-view-79.html),[81](https://apulis.zentaopm.com/bug-view-81.html),[165](https://apulis.zentaopm.com/bug-view-165.html)
   ```
   Review: Task 012
   部署更新过程，确认哪一个镜像或步骤log多，梳理出来排查解决。——测试组

   ```
7. 不支持部署时配置安装依赖的镜像源

   **当前的安装源，和镜像源配置散落在各个组件的配置 *.yaml 和 dockerfile中；如jobmanager2, restfullAPI中的安装源和镜像源都在其dockerfile中指定。**
   
   + 配置过程应该有统一的位置：`指定安装源和镜像源`；
   + 应该有独立的配置步骤：`配置或更新安装源和镜像源`；
   ```
   Review: FeatureRequest 058，Task 013
   9月代码清洗release后，将docker hub封掉验证安装部署 ——测试组

   ```
8. 配置脚本的SSH端口默认22，用户默认root，不支持自定义

   
   * 配置脚本 `deploy.py, utils.py` 中`ssh`, 或`sshpass`使用默认22端口，且没有端口配置项；
   
   * 现在脚本中在加了 `global ssh_port` 配置项；但最好可以在命令行中指定port；

   * 脚本中使用root；配置时如果是普通用户加sudo；k8s相关配置默认在`/root/.kube/`等目录，且归属为`root`；即使同步配置路径，仍有用户归属权限的问题，实则不支持普通用户部署。
   ```
   Review: FeatureRequest 059
   增加判断是22端口是否可访问，（内网，外网环境）支持ssh_port自定义 ——后端组，测试组

   ```

9. 目前平台的python、容器OS、gcc与华为建议的版本不一致，不便于问题定位
   
   |组件   | 客户支持或要求的版本                                      |我方使用版本|
   |:-----|:---------------------------------------------------------|:----------|
   |Python|3.7.5                                                     | 3.7.7     |
   |容器OS|Ubuntu 18.04<br>EulerOS 2.8<br>CentOS 7.6<br>BC_Linux 7.6 |debian 8.3  |
   |gcc   |7.3.0                                                    |7.5.0       |
   |cmake |3.5.2                                                    |3.10.2      |

   ```
   Review: FeatureRequest 060
   可以匹配配置和更新 ——后端组

   ```
10. 平台半自动化部署过程各组件（mysql，前后端配置，jobmanager, nginx)及服务pod配置文件散落系统各处

    **平台部署后散落的配置，为方便仅有运维必须统一规划配置**
    1. nginx配置： /etc/nginx/conf.other/default.conf 
    2. mysql配置： 在容器中
    3. WebUI配置：/etc/WebUI/local.yaml 
    4. prometheus配置：/data/prometheus/data/
    5. 集群ID： apulis_platform/src/ClusterBootstrap/deploy/clusterID.yml 
    6. 集群账号证书：apulis_platform/src/ClusterBootstrap/deploy/sshkey/
    7. 集群pod的配置：apulis_platform/src/ClusterBootstrap/services/
    8. 部署过程更新的脚本： apulis_platform/src/ClusterBootstrap/scripts/  ## 不同环境下以下配置后脚本都会被变更
 
        + modified:   scripts/README.md
        + modified:   scripts/check_docker_ready.sh
        + modified:   scripts/check_machine.sh
        + modified:   scripts/check_node_ready.sh
        + modified:   scripts/cloud_init_infra.sh
        + modified:   scripts/cloud_init_nfs.sh
        + modified:   scripts/cloud_init_worker.sh
        + modified:   scripts/disable_kernel_auto_updates.sh
        + modified:   scripts/disable_mlocate.sh
        + modified:   scripts/disable_networkmanager.sh
        + modified:   scripts/dns.sh
        + modified:   scripts/docker_network_gc_setup.sh
        + modified:   scripts/fileshare_install.sh
        + modified:   scripts/inituser.sh.template
        + modified:   scripts/install-blobfuse.sh
        + modified:   scripts/install-python-on-coreos.sh
        + modified:   scripts/install_ib_on_sriov_az_cluster.sh
        + modified:   scripts/install_kubeadm.sh
        + modified:   scripts/install_mlnx_ofed-5.0.sh
        + modified:   scripts/install_nfs.sh
        + modified:   scripts/install_nv_peer_mem.sh
        + modified:   scripts/kubeadm_init.sh
        + modified:   scripts/mkdir_and_cp.sh
        + modified:   scripts/mnt_fs_svc.sh
        + modified:   scripts/move_keys_into_db.py
        + modified:   scripts/npu/npu_info_gen.py
        + modified:   scripts/platform/aws/README.md
        + modified:   scripts/platform/gce/README.md
        + modified:   scripts/platform/gce/configure-vm.sh
        + modified:   scripts/platform/gce/prepare_gce.sh
        + modified:   scripts/prepare_acs.sh
        + modified:   scripts/prepare_ubuntu.sh
        + modified:   scripts/prepare_ubuntu_cn.sh
        + modified:   scripts/prepare_ubuntu_container_kit.sh
        + modified:   scripts/prepare_ubuntu_dev.sh
        + modified:   scripts/prepare_vm_disk.sh
        + modified:   scripts/pscp_role.sh
        + modified:   scripts/pssh_role.sh
        + modified:   scripts/remove_nvidia_docker1.sh
        + modified:   scripts/render_env_vars.sh
        + modified:   scripts/requirements.txt
        + modified:   scripts/resolve_ip.sh
        + modified:   scripts/set_config.sh
        + modified:   scripts/timed_check.sh
        + modified:   scripts/verify_deployment.sh
        + modified:   services/README.md
        + modified:   services/a910-device-plugin/a910-device-plugin.yaml
        + modified:   services/a910-device-plugin/launch_order
        + modified:   services/cAdvisor/cAdvisor.yaml
        + modified:   services/cloudlogging/fluentd-configmap.yaml
        + modified:   services/cloudlogging/fluentd.yaml
        + modified:   services/cloudlogging/launch_order
        + modified:   services/cloudmonitor/collectd.yaml
        + modified:   services/clusterroles/clusterrolebindings.yaml
        + modified:   services/clusterroles/clusterroles.yaml
        + modified:   services/coredns/dns.yaml
        + modified:   services/custom-user-dashboard/custom-user-dashboard-backend-arm64.yaml
        + modified:   services/custom-user-dashboard/custom-user-dashboard-backend.yaml
        + modified:   services/custom-user-dashboard/custom-user-dashboard-frontend-arm64.yaml
        + modified:   services/custom-user-dashboard/custom-user-dashboard-frontend.yaml
        + modified:   services/custom-user-dashboard/launch_order
        + modified:   services/custommetrics/custom_metrics.yaml
        + modified:   services/custommetrics/launch_order
        + modified:   services/custommetrics/prometheus_instance.yaml
        + modified:   services/custommetrics/prometheus_operator.yaml
        + modified:   services/custommetrics/sample-metrics-app.yaml
        + modified:   services/dashboard/dashboard.yaml
        + modified:   services/device-plugin/a910-device-plugin.yaml
        + modified:   services/device-plugin/launch_order
        + modified:   services/flexvolume/flexvolume.yaml
        + modified:   services/freeflow/freeflow.yaml
        + modified:   services/heapster/grafana.yaml
        + modified:   services/heapster/heapster-rbac.yaml
        + modified:   services/heapster/heapster.yaml
        + modified:   services/heapster/influxdb.yaml
        + modified:   services/helm/tiller-rbac.yaml
        + modified:   services/jobmanager/jobmanager.yaml
        + modified:   services/jobmanager/launch_order
        + modified:   services/jobmanager/pre-render.sh
        + modified:   services/jobmanager2/jobmanager2-arm64.yaml
        + modified:   services/jobmanager2/jobmanager2.yaml
        + modified:   services/jobmanager2/launch_order
        + modified:   services/jobmanager2/launch_order_arm64
        + modified:   services/jobmanager2/pre-render.sh
        + modified:   services/launcher/launcher.yaml
        + modified:   services/logging/elasticsearch.yaml
        + modified:   services/logging/fluent-bit-config.yaml
        + modified:   services/logging/fluent-bit.yaml
        + modified:   services/logging/kibana.yaml
        + modified:   services/logging/launch_order
        + modified:   services/metricsServer/auth-delegator.yaml
        + modified:   services/metricsServer/auth-reader.yaml
        + modified:   services/metricsServer/metrics-apiservice.yaml
        + modified:   services/metricsServer/metrics-server-deployment.yaml
        + modified:   services/metricsServer/metrics-server-service.yaml
        + modified:   services/metricsServer/resource-reader.yaml
        + modified:   services/monitor/alert-manager.yaml
        + modified:   services/monitor/alert-templates/email.tmpl
        + modified:   services/monitor/alert-templates/idle-gpu.tmpl
        + modified:   services/monitor/alert-templates/job_state.tmpl
        + modified:   services/monitor/alert-templates/kill-idle.tmpl
        + modified:   services/monitor/alerting/gpu.rules
        + modified:   services/monitor/alerting/jobs.rules
        + modified:   services/monitor/alerting/k8s.rules
        + modified:   services/monitor/alerting/node.rules
        + modified:   services/monitor/alerting/services.rules
        + modified:   services/monitor/config_alerting.py
        + modified:   services/monitor/gen_grafana-config.py
        + modified:   services/monitor/grafana-arm64.yaml
        + modified:   services/monitor/grafana-config-raw/dlts-cluster-jobs-dashboard.json
        + modified:   services/monitor/grafana-config-raw/dlts-cluster-statistics-dashboard.json
        + modified:   services/monitor/grafana-config-raw/dlts-job-statistics-dashboard.json
        + modified:   services/monitor/grafana-config-raw/dlts-user-statistics-dashboard.json
        + modified:   services/monitor/grafana-config-raw/dlts-vc-statistics-dashboard.json
        + modified:   services/monitor/grafana-config/cluster-status-dashboard.json
        + modified:   services/monitor/grafana-config/dlts-cluster-jobs-dashboard.json
        + modified:   services/monitor/grafana-config/dlts-cluster-statistics-dashboard.json
        + modified:   services/monitor/grafana-config/dlts-job-statistics-dashboard.json
        + modified:   services/monitor/grafana-config/dlts-user-statistics-dashboard.json
        + modified:   services/monitor/grafana-config/dlts-vc-statistics-dashboard.json
        + modified:   services/monitor/grafana-config/job-dcgm-metrics-dashboard.json
        + modified:   services/monitor/grafana-config/node-status-dashboard.json
        + modified:   services/monitor/grafana.yaml
        + modified:   services/monitor/job-exporter-arm64.yaml
        + modified:   services/monitor/job-exporter.yaml
        + modified:   services/monitor/launch_order
        + modified:   services/monitor/launch_order_arm64
        + modified:   services/monitor/node-exporter.yaml
        + modified:   services/monitor/pre-render.sh
        + modified:   services/monitor/prometheus-arm64.yaml
        + modified:   services/monitor/prometheus.yaml
        + modified:   services/monitor/watchdog-arm64.yaml
        + modified:   services/monitor/watchdog.yaml
        + modified:   services/mysql/launch_order
        + modified:   services/mysql/mysql.yaml
        + modified:   services/mysql/phpmyadmin.yaml
        + modified:   services/nginx/default.conf
        + modified:   services/nginx/launch_order
        + modified:   services/nginx/launch_order_arm64
        + modified:   services/nginx/nginx-arm64.yaml
        + modified:   services/nginx/nginx.yaml
        + modified:   services/nvidia-device-plugin/launch_order
        + modified:   services/nvidia-device-plugin/nvidia-device-plugin.yaml
        + modified:   services/openresty/launch_order
        + modified:   services/openresty/launch_order_arm64
        + modified:   services/openresty/openresty-arm64.yaml
        + modified:   services/openresty/openresty.yaml
        + modified:   services/repairmanager/launch_order
        + modified:   services/repairmanager/pre-render.sh
        + modified:   services/repairmanager/repairmanager.yaml
        + modified:   services/repairmanager2/launch_order
        + modified:   services/repairmanager2/launch_order_arm64
        + modified:   services/repairmanager2/pre-render.sh
        + modified:   services/repairmanager2/repairmanager2-arm64.yaml
        + modified:   services/repairmanager2/repairmanager2.yaml
        + modified:   services/restfulapi/restfulapi.yaml
        + modified:   services/restfulapi2/launch_order
        + modified:   services/restfulapi2/launch_order_arm64
        + modified:   services/restfulapi2/restfulapi2-arm64.yaml
        + modified:   services/restfulapi2/restfulapi2.yaml
        + modified:   services/storagemanager/storagemanager.yaml
        + modified:   services/user-synchronizer/domain-offset-configmap.yaml
        + modified:   services/user-synchronizer/launch_order
        + modified:   services/user-synchronizer/user-synchronizer-cronjob.yaml
        + modified:   services/webportal/webportal.yaml
        + modified:   services/webui2/webui2.yaml
        + modified:   services/webui3/launch_order
        + modified:   services/webui3/launch_order_arm64
        + modified:   services/webui3/webui3-arm64.yaml
        + modified:   services/webui3/webui3.yaml

    9. 部署过程渲染的配置： apulis_platform/src/ClusterBootstrap/deploy/  

        + modified:   deploy/bin
        + modified:   deploy/clusterID.yml
        + modified:   deploy/dashboard
        + modified:   deploy/docker-images  ## 编译镜像渲染的配置，其中webui3的配置还会在启用webui3时用到
        + modified:   deploy/etcd
        + modified:   deploy/kube-addons
        + modified:   deploy/kubelet
        + modified:   deploy/master
        + modified:   deploy/RestfulAPI
        + modified:   deploy/services
        + modified:   deploy/sshkey
        + modified:   deploy/UserDashboard
        + modified:   deploy/web-docker
        + modified:   deploy/WebUI
    
    10. 平台运行中与Job相关配置和log 

        */dlwsdata -> /mntdlws*

        + jobfiles -> /mntdlws/jobfiles  ## pod， job运行配置
        + namenodeshare -> /mntdlws/namenodeshare
        + storage -> /mntdlws/storage   ## 镜像，示例运行路径
        + work -> /mntdlws/work
        + host系统log：/var/log/
    
    11. 当前临时的文件备份路径
        
        + /mnt/ClusterConfiguration # 备份平台相关配置
        + /mnt/fuse   ## 备份镜像
        + /mnt/local  ## 备份job，pod相关配置
   ```
   Review: FeatureRequest 061 ,Task 015
   1. 清理配置，将权限也checkpoint 到github repo，避免后续变更 ——后端组
   2. 验证配置的备份和恢复 ——测试组
   ```
11. 平台config.yaml 还有多余不确认的配置等,发布平台版本时应该确认发布的组件，清理组件配置

    1. k8s集群和平台主要配置 config.yaml 中的 dns_server（应该是无效配置），告警邮箱,微软认证，微信认证(非此次交付内容)，要确定清理后有无影响？
    2. 各组件目录下的配置文件yaml或dockerfile中被注释的配置，应该清理；
   
   ```
   Review: FeatureRequest 062， Task 016
   1. 清理注释配置 ——后端组
   2. 验证清理配置后，平台是否可以运行 ——测试组
   ```   
    
12. 缺少初始化数据和示例

    *建议增加初始化数据，如：*

    1. 预置普通用户，用户组；用户管理中的初始的管理员是从前端配置中读取的，没有平台默认的admin，
    2. 预置普通用户的Virtual Cluster 
    3. 提交Job窗口建议增加一些典型示例的模板
    4. 建议预先加载一些典型示例的镜像
    5. 建议将演示示例预先配置

    可以避免一些空数据引起的问题，也便于用户快速熟悉平台。
   ```
   Review: Bug 690
   提交Bug跟踪处理 ——测试组
   ```  
13. WEB页面缺少用户引导，版本，版权等相关说明
   ```
   Review: FeatureRequest 063 
   调研版权 ——老蔡
   ``` 
14. 用户权限管理规划不全，管理员和普通用户权限不明晰
    
    + 参看 BugId: [636](https://apulis.zentaopm.com/bug-view-636.html),[408](https://apulis.zentaopm.com/bug-view-408.html),[409](https://apulis.zentaopm.com/bug-view-409.html)
   ```
   Review: 
   待详细沟通和确认。
   ``` 
15. 相关训练（GPU,NPU）示例准备不足，依赖环境镜像制作、参数配置没有明确的说明
   ```
   Review: FeatureRequest 064
   商业版补充，开源版增加部分示例测试 —— 测试组，算法组、齐博
   ```     
16. 模型（NPU）训练示例脚本中写死绑定的device id号和NPU ip，场景很受限，

    + 建议模型训练的资源应该完全基于平台资源分配、调度；不应透过平台占用资源。参看 BugId：[640](https://apulis.zentaopm.com/bug-view-640.html)
   ```
   Review: 
   单机多卡，华为的配置文件 —— 进文，
   补充单机多卡模型的deviceid配置json文件 —— 后端组、碧峰
   ```
---

## 今后部署和运维需要注意的事项(Checklist)


### 集群基本信息预先确认项

1. 硬件基本信息
   
   * 节点硬件架构 
      - 示例： AMD64 GPU，intelx86-CPU，ARM64-NPU

   * 设备数量
      - 示例：单机，同构多机，异构多机

   * 关键资源配置（NPU,GPU，网卡）
      - 路由器配置   <需支持DNS Maping, DHCP Server，IP-MAC-Band>
      - 交换机配置   <100G, 10G, 流控，自适应>
      - 每个节点（node）资源配置：<芯片数量>
      - 每个节点依赖资源：
         + 网卡：   <驱动版本，支持接口数>
         + 网络接口：<名称，IP配置>

2. <span id="sysenv">操作系统、驱动和组件版本 </span>
   * 主机操作系统：  <Ubuntu 18.04.1>
   * Docker 版本：  <19.03.12, build 48a6621>
   * k8s 版本：     <v1.18.0>
   * Mysql Server:  <8.0.20 (mysql Ver 14.14 Distrib 5.7.30)>
   * 容器系统和版本：<Ubuntu 18.04>
   * Python:        <3.7.5>
   * 芯片驱动：
      - Nvidia GPU：<xxxxxx>
      - Huawei NPU: <C73B035>
   * 网卡驱动：      <TM210网卡驱动 v1.0.1>

### 网络预先确认项


1. <span id="checklist">预先确认网络配置清单 </span>


   | 序号 |         类目         |   确认信息                                                            |  备注                                   |
   |:----|:--------------------|:-----------------------------------------------------------------------|:---------------------------------------|
   |   1  |       网络限制       | 内网or互联网：<br>互联网带宽：                                          | 　                                     |
   |   2  |          GPU         | 服务器OS：<br>GPU板卡型号： <br>驱动版本：                              | 　                                     |
   |   3  |          NPU         | 服务器OS： <br>NPU驱动版本：                                           | HUAWEI   Ascend910                     |
   |   4  |        交换机        | 交换机型号：<br>交换机带宽：                                            | 1GE   or 10GE      或更高               |
   |   5  |       网关配置       | DHCP-Server：<br>DNS Local Maping：<br>IP-MAC绑定：                    | 　                                      |
   |   6  |       网络配置       | 集群各服务器通信网段：<br>服务器hostname：<br>域名解析<公网访问域名，私网通信域名>： | 　                             |
   |   7  |       网络端口       | 端口开放<80,443,22,30000~32767>：                                      | 　                                      |
   |   8  |      存储服务器      | 容量： <br>NFS or Ceph：                                               | 单独的服务器还是复用集群服务器中的存储     |
   |   9  | 集群各服务器配置信息  | Master节点配置：<br>GPU服务器配置：                                     | 为了保障集群稳定及易维护性，Master节点建议采用通用服务器（物理机），非VM |
   |  10  |     安装/镜像源     | 是否需要私有docker镜像库：<br>是否可访问阿里云/华为云源<Ubuntu/Python>：  | 　                                      | 	


2. 组网规划

   **节点组网规划**
   | 主机名       | 公网IP        | mask        | gateway       |DNS            |iBMC公网IP     |私网IP         |
   |:----------- |:--------------|:------------|:--------------|:--------------|:--------------|:--------------|
   | node01     |xxx.xxx.xxx.xxx|255.255.255.0|xxx.xxx.xxx.xxx|114.114.114.114|xxx.xxx.xxx.xxx|xxx.xxx.xxx.xxx|
   | node02     |xxx.xxx.xxx.xxx|255.255.255.0|xxx.xxx.xxx.xxx|114.114.114.114|xxx.xxx.xxx.xxx|xxx.xxx.xxx.xxx|
   | node03     |xxx.xxx.xxx.xxx|255.255.255.0|xxx.xxx.xxx.xxx|114.114.114.114|xxx.xxx.xxx.xxx|xxx.xxx.xxx.xxx|

   **特殊资源（NPU）组网规划：**
   | node   | npu_id | address       | netmask       |
   |--------|--------|---------------|---------------|
   | node01 | NPU0   | 192.168.10.11 | 255.255.255.0 |
   | node01 | NPU1   | 192.168.20.11 | 255.255.255.0 |
   | node01 | NPU2   | 192.168.30.11 | 255.255.255.0 |
   | node01 | NPU3   | 192.168.40.11 | 255.255.255.0 |
   | node01 | NPU4   | 192.168.10.12 | 255.255.255.0 |
   | node01 | NPU5   | 192.168.20.12 | 255.255.255.0 |
   | node01 | NPU6   | 192.168.30.12 | 255.255.255.0 |
   | node01 | NPU7   | 192.168.40.12 | 255.255.255.0 |
   | node02 | NPU0   | 192.168.10.21 | 255.255.255.0 |
   | node02 | NPU1   | 192.168.20.21 | 255.255.255.0 |
   | node02 | NPU2   | 192.168.30.21 | 255.255.255.0 |
   | node02 | NPU3   | 192.168.40.21 | 255.255.255.0 |
   | node02 | NPU4   | 192.168.10.22 | 255.255.255.0 |
   | node02 | NPU5   | 192.168.20.22 | 255.255.255.0 |
   | node02 | NPU6   | 192.168.30.22 | 255.255.255.0 |
   | node02 | NPU7   | 192.168.40.22 | 255.255.255.0 |

2. 网络拓扑

   ![集群整体组网](satic/node集群拓扑图.png)

### 部署确认项

1. 基础网络配置，参考部署文档

   * 各节点机器主机名（hostname）
   * 资源节点（GPU,NPU,CPU,TPU）接入交换机局域网配置，流控配置
   * 节点接入交换机局域网配置
   * 本地域名解析配置
   * 公网域名解析配置
   * 路由网关或接入网关的DHCP Server，IP-MAC绑定配置
   * 路由网关或接入网关的DNS Local Maping配置

2. 集群和平台部署项

   * 更新集群配置
   * 配置通用账号和同步访问证书
   * 安装初始化系统依赖
   * 安装kubeadm
   * 初始化 k8s
   * 加入k8s 节点
   * 生成平台配置
   * 编译和启用平台服务组件pod

3. 集群状态检查

   * k8s 集群状态
   * k8s 节点状态
   * 平台服务组件pod状态
   * 关键资源（NPU,GPU）状态
   * 平台外网访问状态
   * 节点资源空闲状态
   * 存储使用率
   * 主要业务流 (VC->vc Status->Submit Job->Job List->Job Status->Job Debug)
