# XXXXX智能工业平台快速指导

[TOC]

* 文档说明

|属性         |时间       |
|-------------|-----------|
|编辑/维护    | thomas    |
|文档版本     | 2.0.0     |
|发布日期     | 2021-08   |

**系统要求**

本文档仅适用于XXXXX智慧工业平台2.0 + 以上版本 ！

文档所有权限归属**XXXXX科技（深圳）有限公司**，未经允许，不得外发,转载,抄袭！将保留一切追溯权力。

## 平台简介

我国是工业大国,工业智能化升级既贯彻国家战略又符合时代发展趋势。然而,工业制造领域企业普遍存在技术基础薄弱、数据采集难度大、场景需求多样、部署环境复杂等挑战,限制企业智能化升级的脚步。

XXXXX科技基于前沿人工智能技术及工业制造领域的实际场景需求打造了XXXXX智慧工业平台，一直以来积极推动AI技术在工业领域的创新应用。也广泛应用于3C电子产品、机械装备制造，AIOT，自动驾驶等领域，赋能工业质检和外场巡检场景，内置器件错漏反、OCR识别、异物检测等预训练算法，帮助客户实现智能制造及工业4.0时代的产业升级，提升效率。

支持与自动化系统进行通信，进行自动化设备的联动，如控制机械臂、报警器、PLC等。通过工业视觉软件，也可以将质检数据输送到MES系统，记录质检信息、进行管理与改进工艺等。

![系统框架图](../static/qip-guide/系统框架图.png)

## 业务流程介绍

**AI赋能原有技术生态，助力企业提升质检效率！**

集成数据采集、数据标注、模型开发、模型发布、模型部署、质检应用的一体化解决方案，帮助客户实现智能制造的产业升级，提升效率。解决工业质检中数据持续集成、模型持续优化、边端持续自动化部署、模型持续评估、性能持续监控的问题。

![业务流程](../static/qip-guide/services-flow.png)


## 1. 平台初始化【系统管理员】

用户可以登录平台 https://xxx.xxx.xxx.xxx<:PORT>/  {sysadmin:apulis@123} ，设置用户，资源配额和场景等。

### 创建组织用户和资源配额
首先使用系统默认的超级管理员账号**sysadmin**，创建**虚拟集群**给不同用户划分资源。

![create-vc](../static/qip-guide/create-vc.png)

### 创建用户组的资源配额
平台支持每个用户组都可以再分配资源配额
![create-resorce-quota](../static/qip-guide/create-resorce-quota.png)

### 设置自动标注的资源配额
半自动标注也是一种推理服务，需要相应的NPU,GPU推理资源，以及CPU,MEM等
![half-auto-annotation-resource-setup](../static/qip-guide/half-auto-annotation-resource-setup.png)

### 创建组织和账号

点击**系统导航**/**账号管理系统**，在账号管理系统窗口中打开**组织管理**的组织列表，创建新的组织。

![create-organization](../static/qip-guide/create-organization.png)

* 用户角色
    平台预置了以下权限角色（支持定制） 
    + systemAdmin, 拥有管理用户组织，虚拟集群，资源配额的权限。
    + orgAdmin,  可以管理用户， 创建场景和查看任务的权限。
    + developer，拥有除组织和角色外的所有权限。
    + annotator，仅有数据集标注的权限。 

* 用户组

用户组可以直接关联某个角色和组织，这样就继承了组织的资源和角色的权限；比如可以创建开发者用户组，也可创建标注员用户组，管理员用户组。

<!-- ![create-admin-group](../static/qip-guide/create-admin-group.png) -->
<!-- ![create-annotator-group](../static/qip-guide/create-annotator-group.png) -->

![create-developer-group](../static/qip-guide/create-developer-group.png)

* 新建账号

+ 创建管理员账号
![create-admin](../static/qip-guide/create-user-admin.png)
+ 创建开发者账号
![create-developer](../static/qip-guide/create-developer.png)
+ 创建标注员账号
![create-annotator](../static/qip-guide/create-annotator.png)

## 2. 创建场景（组织管理员）

一般由用户组或组织管理员，管理系统设置，资源配额，创建场景，数据集标注任务，审核标注任务，然后也可以发布服务。但部分开发者也可以申请或赋予新建数据集，标注，创建项目等权限。
**以下示例使用管理员角色账号 demo-admin 执行以下操作。**

* 创建场景（管理员）

组织管理员根据实际需要创建场景，主要是根据业务需要组合模型和数据集
![create-sence](../static/qip-guide/create-sence.png)

* [创建新的用户组或用户账号](#创建组织和账号)

## 3. 创建数据集（开发者）

不同类型的检测、识别项目，需要不同类型，格式的数据集；在创建项目之前一定先要创建数据集，及其标注任务，
如果数据集已标注，选择数据集类型为“已标注”就好了。

![create-datasets](../static/qip-guide/create-datasets.png)

* 上传数据集（开发者）

目前支持通过网页上传本地数据（2G以下），选取推理样本作为数据集。
![upload-datasets](../static/qip-guide/upload-localimages.png)

* 创建标注任务（开发者）

需要设置标注的标签，如果是多人标注，需要设置每个人的标注作业量。
![create-annotation-job](../static/qip-guide/create-annotation-job.png)


* 分配标注任务（开发者）

将标注任务支配到具体的标注员，选择后立即生效。
![fenpei-annotation-job](../static/qip-guide/fenpei-annotation-job.png)


* 审核标注任务（开发者）

当标注员提交了标注任务后，开发者可以在标注任务列表中查看到可以“审核”的数据集，可以点击标注任务ID查看标注的情况，如果满足要求，点击审核后确认通过即可，否则打回重新标注。
![shenhe-annotation-job](../static/qip-guide/shenhe-annotation-job.png)


## 4. 标注数据集（标注员）

以下示例使用标注员角色账号 demo-annotator 执行手工标注的操作，半自动标注请参考[半自动标注使用指导](附录A：半自动标注数据)。

* 打开标注任务

标注任务状态分为： 标注中，待审核，已完成；标注中的任务都可以在任务基本信息中查看标注的进度。
![open-annotation-job](../static/qip-guide/open-annotation-job.png)

* 手工标记图像

默认支持手工标注，也可通过右下角提示的快捷键，提升标注效率。
![annotation-img](../static/qip-guide/annotation-img.png)

* 批量标注，复制多帧

当数据集中的目标大致相同时，可以使用右侧标签信息中的复制多帧，将当前图像的标注复制到之后没有标注的图像上，需要注意调整之后图像的标签框，并保存！
![copy-flag-more-img](../static/qip-guide/copy-flag-more-img.png)


## 5. 创建项目（开发者）

以下示例使用开发者角色账号 demo-developer 执行以下操作。

* 在一个场景下可以创建多个项目，支持不同的检测目标，不同的检测模型等；此时需要选择已经发布的数据集。
![create-project](../static/qip-guide/create-project.png)

* 创建训练任务

点击[模型开发]后，可根据需要选择数据集，参数等，创建训练任务
![create-training-job](../static/qip-guide/create-training-job.png)

* 训练数据可视化分析

集成了mindinsight，可辅助分析算法损失函数，参数网络，帮助优化模型。
![visual-training-job](../static/qip-guide/visual-traing.png)

* 创建评估任务

每个模型都需要经过评估，获取评估结果。
![create-eval-job](../static/qip-guide/create-eval-job.png)

* 评估结果可视化分析

支持列表，柱状图，趋势图等分析方法。
![create-eval-job](../static/qip-guide/visual-evil.png)

* [创建云端训练任务（可选）](#附录B：创建云端训练任务)

## 6. 服务部署

如果模型评估结果满足要求，或有相对的提升，可以在服务部署中创建推理服务。

* 创建推理服务

选择已经评估完成的检测和分类模型，根据业务负载配置副本数创建。
![create-infer-services](../static/qip-guide/create-inference-service.png)

* 部署和运行服务

创建服务需要部署到具体推理节点，启用服务。
![create-infer-services](../static/qip-guide/deploy-startup-infer.png)

## 7. 对接产线工控机

我们可以与第三方工控机，AOI设备，视觉软件对接，我们提供以下基础的配置，同时提供深度定制。

* 平台的登陆接口

支持账号登陆，自动获取token。
`https://xxx.xxx.xxx.xxx:<PORT>/iam/api/v1/users/login`

* 获取服务列表接口

可以获取所有创建的服务列表，及服务的状态，从属的场景，项目信息等。
`https://xxx.xxx.xxx.xxx:<PORT>/iqi/ProjectService/V1/projects`

* 获取登陆证书

管理员或开发者可以在运维管理的系统设置窗口下载证书。
![download-htts-key](../static/qip-guide/download-htts-key.png)


* 目标检测推理接口

使用该接口可以post推理请求和数据。
![infer-service-api](../static/qip-guide/infer-service-api.png)

## 8. 服务统计和告警

* 查看服务统计结果

首先会全息展示推理请求的结果和相关信息。
![infer-service-api](../static/qip-guide/services-static-list.png)
其次也支持典型的趋势图分析。
![infer-service-api](../static/qip-guide/services-static-map.png)


* 配置服务策略

支持复杂多样的告警策略
![infer-service-api](../static/qip-guide/create-warning-rule.png)


* 启用告警

支持灵活的选择启用不同的告警
![infer-service-api](../static/qip-guide/runing-service-rule.png)

* 服务告警历史

可以查看，并处理告警信息。
![infer-service-api](../static/qip-guide/warning-recording.png)


## 附录A：半自动标注数据

详细配置可以查看《半自动标注使用指导》

* 创建半自动标注项目

  需要有已经使用小样本训练好的检测类模型。
![create-auto-label-job](../static/qip-guide/create-auto-label-job.png)


* 触发自动标注

  标注员可以尝试点击左侧工具栏的魔法棒，启用半自动标注任务。
![startup-auto-label](../static/qip-guide/startup-auto-label.png)


## 附录B：创建云端训练任务

该训练上云目前仅使用于XXXXX智慧工业平台2.0 + 以上版本 ！仅支持华为云ModelArts。

* 工业质检平台已经部署，且能够执行本地训练和推理，数据集管理
* 平台所在的IT环境能够访问华为云 ModelArts 服务
* 文件，配置，网络端口等规格已经安装调试完毕
* 云训练镜像需要包含训练代码和脚本，兼容平台 manifest 规格
* 训练可视化，训练日志，模型导出，服务部署不在此次范围，具体可以详细讨论

**配置说明**

1. 上传云训练镜像到华为云镜像中心，并将可拉取的链接给平台运维管理员做镜像预置

    华为对接同事需要先将云训练镜像上传到华为云镜像中心（具体以部门而定），并允许可拉取。

* 示例镜像列表
    ```bash
    # 产线A
    [DOMAINNAME].com/ascend-modelarts/modelarts_mindspore1.1.1_cp37_nnae_atc_20.2.rc1:1.0
    # 产线B
    [DOMAINNAME].com/modelarts-image_dcj/modelarts_mindspore1.1.1_cp37_nnae_atc_20.2.rc1:1.1
    ```

2. 配置云上 modelarts 训练云账号

    目前松山湖用的是华为对接同事的个人账号，这个要根据需求申请团队使用账号的训练资源。
    使用开发/测试角色账号登陆平台在 运维管理/系统设置 中配置 云上modelArts账号

    ![cloud-train](../static/CloudTrain-songshanhu/add_modelarts_accounts.png)


3. 创建云训练模板
   
    在项目管理/创建项目/创建训练

    ![cloud-train](../static/CloudTrain-songshanhu/创建云端训练.png)

4. 检查云训练状态

    打开项目列表，可以看到改项目下个训练的详情，以及训练可视化等。

    ![cloud-train](../static/CloudTrain-songshanhu/status-train.png)

