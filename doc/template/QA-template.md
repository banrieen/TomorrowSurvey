# XXXXX平台介绍/使用指导/疑难攻关（Intruction/Guide/Solution）

## 综述

## 环境信息

* CustomerPlatform: 平台使用沟通
* Date: 2021-0903
* Supportor: Thomas.Bian
* Environment: XXXXX-330版本
* Process: 采集和标注数据
* Host: 10.8.6.31
* Account: admin/L6B86X
* RemoteConnection: 远程向日葵：663 173 263,远程密钥：O7XUPx

## 客户需求(Customer-Requirements):

+ REQ1: 对接MES系统
+ REQ2: 平台定制，换Logo, 提供集成接口
+ REQ3: 支持AOI设备推理，数据管理

## 遗留问题(Legacy-Issues): 

+ L-Q1: 标注100张图片数据，在达到60、70张之后会出现卡顿不响应
    - L-Q1-AWS1: 初步定位性能问题，或功能Bug, 没有验证大数据集的情况
+ L-Q2: 第三方镜像上传指导
    - L-Q2-AWS1: 提供上传指导文当

## 现场已解决问题(Resolved-Problem):

+ R-Q1: 下载数据集
    - R-Q1-AWS1: 数据集发布之后可以下载，未发布之前不可下载。
+ R-Q2: 标注部分数据集，继续标注
    - R-Q2-AWS1: 先将数据集发布，之后将未标注的图片继续添加到之前的数据集，创建标注子任务，就可以继续标注。
    - R-Q2-AWS2: 如果只有少量标注，也可直接在标注任务窗口"清除"所有标注，重新标注。
+ R-Q3: 删除，剔除无用图片
    - R-Q3-AWS1: 遇到需要剔除的图片，点击左侧工具栏的“禁用”，该图片就变为“不可标注”状态，发布数据集时会被剔除。

