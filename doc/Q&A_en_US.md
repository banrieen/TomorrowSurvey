# Q & A

## Netherlands Customer

2. In regards to point 8: in case of the YOLOv3 model from ModelZoo the start script makes use of the environment variables RANK_SIZE, RANK_ID and others. Since your platform already sets these (which I see in the training log) I was trying to get those passed to the start script but they seem to be empty when passed via the "running parameters", see http://160.20.152.156/AIarts/model-training/1f830e24-eda1-4cee-a120-58c708d12b76/detail for an example of what I tried.

Answer: This is a bug in our system, we will address this issue in the future release. 


3. output from start script seems to be discarded on errors, i.e. there is little to no debug info on failure Answer:we need to know which error log you need.
What I mean is that if a start script for a model training fails I do not see the errors in the training log.

Answer: Our platform will display the platform level error log. For the algorithm level error, our platform will not display the error. 

4. job management: stopping a job causes message that is has been removed, removing a job causes message saying "successfully operated"
Answer:This is an unusual operation,If a job is stopped before it is started, the job will be removed. We recommend that you stop or delete the job after it starts. We can communicate further.
This happened to me when I stopped jobs that were already running and preventing me from running a new training job. The stop functionality worked as expected, just the displayed message does not fit the action.

Answer: Thank you for pointing this out, we will address this translation issue in the future release. 


5. upload form says that tar, tar.gz and zip files are supported but uploading a tar.gz didn't work (platform says the upload failed)
   - solution: upload zip archive instead
Answer: The community version does not support tar.gz format for now. You could choose the enterprise version.
Where can I see which version we are running on? Because I expected ours to be an enterprise edition.

Answer: The platform you use now is the community version. 


6. "running parameters" (and other fields) are vulnerable to remote code execution Answer:The remote execution problem is related to the network environment or IDE tools.
I'm not sure if I understand you correctly since I'm using your AI platform and no other IDE tool. To clarify what I mean:
- I create a new training job
- I add a new "running parameter" with "my_user" as name and "$(whoami)" as value
- Then I start the training
- When training is finished I look at the training log and see this:
cd $TMP_PATH # {{start command}} bash /home/admin/storage/1620630271469/npu_train_alt.sh --my_user root --data_path /data/dataset/storage/coco/2014/raw --output_path /home/admin/apecams & cd - Besides being able to print the current user name I can use this to install software on the docker container using apt and potentially execute docker container breakout exploits since the container seems to be running as privileged and has several capabilities enabled (e.g. CAP_SYS_ADMIN) that can be exploited for a breakout.

Answer: This is a potential security vulnerability and thank you for pointing this out. We will take proper action in the next release to address this. 


1. the original ModelZoo archive has subfolders which the AI platform is not handling correctly (files can't be found when trying to start a training)
    - solution: re-upload with all data files in the root directory of the archive
---子文件夹中的模型上传失败，客户选择直接在子文件夹中上传，客户使用问题
Modelzoo下载的模型中有子文件夹，需要优化，
暂时和客户澄清，需要将代码模型放在同一个文件夹下

2. upload form says that tar, tar.gz and zip files are supported but uploading a tar.gz didn't work (platform says the upload failed)
    - solution: upload zip archive instead
---系统提示支持的上传格式tar.gz，客户使用中不支持，产品缺陷需要完善
和客户澄清，开源版本暂不支持，答复客户商业版支持

3. one cannot edit the created model and storage path is truncated in overview
    - solution: click "evaluate" and copy path from there
---已知的偶现操作问题，需要跟踪解决，后续提供一份英文操作手册给客户
回复客户后续会提供英文操作手册

4. job management: stopping a job causes message that is has been removed, removing a job causes message saying "successfully operated"
--job runing之前stop job会导致job被删除，产品需要做提升优化，建议running之前禁用stop
建议客户运行后再stop，操作澄清

5. inference jobs and models cannot be edited, only removed
---推理任务没有编辑，只有删除，系统设计如此，需要和客户澄清
和客户澄清暂时没有编辑功能

6. model training adds --data_path and --output_path options by default which are not used by the YOLOv3 model startup script
---客户使用模型启动脚本是两个默认选项不会启动，系统预置模型是可以启动，如果是客户自己下载的modelzoo 模型是不可以直接使用，还未打通，
和客户澄清，下载的模型，数据集路径和数据输出路径以及各个参数需要在平台上修改操作

7. adding a "running parameter" doesn't allow adding environment variables and not all are exported, so some are not available to the start script
---平台创建的running parameter 没有添加进环境变量（后台没有生效），和客户澄清直接下载的模型参数需要调整，不是默认直接能用
和客户澄清，下载的模型，不是预置模型，数据集路径和数据输出路径以及各个参数需要在平台上修改操作

8. most environment variables seem to be empty, i.e. one cannot pass them to the start script (e.g. RANK_SIZE, RANK_ID, MAIN_PATH, SAVE_PATH, DEVICE_ID, RANK_TABLE_FILE)
---预置环境变量适配NPU 训练环境，需要和客户确认是训练模型具体信息（是否是基于npu的训练模型）和客户澄清直接下载的模型参数需要调整，不是默认直接能用
和客户澄清，下载的模型，不是预置模型；数据集路径和数据输出路径以及各个参数需要在平台上修改操作

9. "running parameters" (and other fields) are vulnerable to remote code execution
---远程访问，远程开发模型不稳定，
判断和客户网络环境和使用工具有关，需要客户确认网络及使用环境和开发工具

10. output from start script seems to be discarded on errors, i.e. there is little to no debug info on failure
---需要和客户具体确认错误信息，平台可直接展示框架错误以及平台运行错误的日志，算子或模型相关日志权限或者开关需要配置
询问客户需要的什么类型的错误日志


## Germany AUDI Cumtomer

这两个问题主要是预置镜像工具包没有统一管理，可能是GPU算法镜像中预置工具包，依赖包没有安装全！可以向客户了解他选用的算法镜像，我们给客户更新算法镜像来处理这个问题。

我在测试的GPU环境，atlas01 的NPU环境下复现验证，atlas01创建的代码开发环境没有这两个问题的！ GPU测试环境下GPU算法镜像较多，选择hovod-tensorflow-v2.3镜像有这两个问题，主要时unzip 等依赖工具包没有安装。

* 问题一、 zip 包上传比较快，但在上传完成后，在平台显示的上传目录中是空的，没有文件；把相同的文件打包为tar.gz 上传比较慢，在上传完成后，在平台显示的上传目录中文件成功解压出来的。

* 分析： 需要了解安装环境的镜像版本，再确认下问题。因为前天荷兰客户反馈上传zip 成功，上传 tar.gz, 平台提示上传错误！
* 复现： 
    + 在GPU测试环境使用 hovod-tensorflow-v2.3的镜像创建开发环境， zip 包可上传成功，但是解压缺少unzip工具，tar.gz可以上传成功，tar -zxvf 也可以解压成功。
    + 在测试atlas01环境使用 tensorflow-v1.15的镜像创建开发环境，zip, tar.gz 都能上传成功也能解压成功

 
**AUDIXXXX客户的问题描述详情：**

```
After the meeting yesterday, I tried to upload some Images over the XXXXXX Webinterface to the Server.

First I created a .zip package and uploaded it. The upload was fast, followed by a very short processing message. After the successful message I checked the path on the server. A folder with the corresponding name was created, but it’s empty. 

After that, I created a .tar.gz package and uploaded it. Same procedure as described above, only the processing takes more time. After the upload I checked the new folder on the server and see that all files from the .tar.gz package were successfully extracted. 

I think there might be a bug when uploading a .zip file. 


```
* 问题二、在模型开发的jupyter窗口（环境中）中使用python脚本在import opencv 时提示 libGL.so.1: cannot open shared object file: No such file or directory。

* 分析： 我们预置的算法镜像默认是安装了opencv 的，从log看opencv是安装了，有些依赖包没有安装。
* 复现： 
    + 在GPU测试环境使用 hovod-tensorflow-v2.3的镜像创建开发环境，没有预置安装opencv
    + 在测试atlas01环境使用 tensorflow-v1.15的镜像创建开发环境，opencv 是安装好的，也可以import 成功
 
**奥迪客户的问题描述详情：**

```
I will use the opencv python package in the Jupyter environment, but there is an error.
Please check the error message in opencv_error.html

I have already checked the opencv package version with pip list | grep cv -> opencv-python 4.5.1.48

Maybe some packages for the container are missing? See: https://stackoverflow.com/questions/55313610/importerror-libgl-so-1-cannot-open-shared-object-file-no-such-file-or-directo


Do you have a workaround for this problem?
```

---

## Today I wanted to upload a big dataset to the XXXXXX platform. 
Because it was so big I moved the files via SSH directly to the server and unzipped them. 
After that I created in the platform with “Add Data Set” a new entry and selected “Upload new dataset from other sources”.
After submitting I always get the error message: “File or path does not exist”

The Path via SSH is: /home/XXXXXX/dataset/coco2017/

Additionally, I saw that some dataset from you were already uploaded in the /home/XXXXXX/dataset/… directory. But when clicking on the Dataset in the Platform then I can see that the path is /data/dataset/storage/…
This is confusing. If I manually uploading files via SSH, in which folder do I have to put them? And does the path have to be on the server running the XXXXXX web application?

问题（临时）答复：
About your question, We suggest that you can upload big datasets files in `/data/dataset/storage/…` path via SSH; It is the mounted space path from the file share system such as NFS. 
    Rest assured, The datasets are not saved directly on the server machine HDD.
    We do not recommend that copy the datasets folder into  personal home path `/home/XXXXXX/dataset/`, after uploaded.         

    Thank you for your good questions, we will improve and update the operations documentation,  providing better operational experience.

问题定位：用户第一次上传的是job 容器中的当前用户目录，该目录在平台下是不可见的，或者说在NFS/CEPH系统下不可见；
                      用户第二次上传的/data/dataset/storage/ 是挂载的目录，该目录映射在文件系统，平台可以看到；但这个是公共的预置数据集路径，其实不适合开放给个人使用！
后续开发建议：1. 平台需要支持完善的文件管理，支持上传到用户个人目录。
                              2. 需要详细的操作手册

---

## I’m currently working on an use-case for object recognition. Can you show me how I can import the algorithms (e.g. YOLO V3/V4, R-CCN or SSD) from the MindSpore Model Zoo to use them as preset models on the platform? 

+ Answer
The ModelZoo pretrained models need to adapt parameters on the platform before startup；YOLO V3/V4, SSD e.g. that based on the NPU architecture， We have  already adapted as premodel-sets named model-gallery, 
You could upload this models sets, and then follow the quickly guide to startup your training. 

##  Object Detection algorithm
yesterday I saw that in the model-gallery folder, which you send me, that the yolo V3 in TensorFlow you had your own custom pictures (model-gallery\models\npu\tensorflow\yolov3). Does this version or an other algorithm for object detection work right now instead of the YoloV4? 

+ Answer

Yes, The yolo v3 model that pre-setup in the platform, you can use it directly for training and deploy inference. 
 And there are SSD-MobileNetV1 FPN, Mask-rcnn, Faster-rcnn, SSD-MobileNetV2 algorithms for object detection in the model-gallery folder (model-gallery\models\npu\mindspore),  may need to adapter the NPU driver version .

详细情况：
         跟齐博、算法组同事确认了，模型适配不区分（x86\arm）架构，不论NPU,GPU影响的只有驱动版本。
         总体上model-gallery上适配的NPU模型，奥迪环境x86-A910，如果驱动版本一致都可以直接用的，但是凌飞当时部署的记录中没有驱动版本号，不好确认。
         从Sebastian的描述我们预置了yolov3 ，这个模型支持NPU训练和推理的。
        我们是否直接回复他们使用yolov3, 还是保险期间就yolov4问题再协调远程，顺便确认后答复他们？


## Memory using for data,  Monday, June 7, 2021

Uploading data via SSH is working well. 
To put Alex’s concerns in more concrete terms: If data is uploaded via the web GUI, it is not stored on the large storage space by default, but on the partition with the operating system. Can this be adjusted?
Answer

     This question has 2 issues:
1 issue:  When you upload datasets via WEB UI `Data Management/Data Set Management/Create Datasets`  page，we inferred that you have selected the Private Permission for your datasets, We recommend that you select the Public Permission, and other members can also use this dataset.
2 issue:  No matter which permission you selected, the datasets would be upload into the storage management system such as NFS`s large storage space . The difference between the ‘Private Permission’ and ‘Public Permission’ is that the path `/home/[USERNAME]/storage/` used for current user space on the NFS.It can be accessed directly in the development  environment or training env，another user account can’t access or view it; but the path `/data/datasets/` is open to all users.
 
问题定位
这个问题是因为数据集访问权限分为“私有”和“公有”, 默认为私有，如果上传数据集选择权限为 私有，则会上传到当前用户的空间下，只有当前用户可用。
例如上传PrivatePCb 为私有数据集，上传路径为： /home/admin/storage/PrivatePcb 这是一个用户Job下的路径，都在NFS存储时上，只是其他账号不可见，并不是裸机系统下的路径。
 
如果要共享给多人使用，则要设置访问权限为 公有，会上传到公共空间。

## data storage level

for our two AI-Servers we have several SSDs. For the operating system and the software the first ones. All others habe about 5 TB memory and their purpose is to store the data for the models and the datasets. They already are connected with the path /data. We think it would make sense, that the XXXXXX platform also uses this memory to store the data.
What do you think Johnny and how can this be done?
* Answer
Your understanding is right. If you need extra storage space for data and models, you can use the worker node's 5.2T HDD directly. 
Note! Do not use the root account login to the server by SSH /FTP/SFTP etc.
We have set up NFS service with 5.2T HDD in the master node,the storage architecture of platform is based on k8s pv/pvc, mode code, datasets, database, userdatas, Job logs etc. have been stored in k8s PV.
The public datasets path: `/data /dataset/storage/`
The public pre-trained model path:  `/data/model-gallery/`
 
问题定位
       实际问题是这样的，客户环境有2台服务器，其中一台作为master既做管理也承载训练任务，每台服务器有893.8G + 5.2T HDD，其中第一个893.8G盘做了系统盘；
         Master节点的5.2T HDD 部署时用作了平台NFS存储（下表标红的地方）。
        按照他们的理解意思，5.2T的存储应该用来存储模型的数据和数据库等，我们平台也在用这块存储空间，他们看到的 the path /data 是NFS共享路径。基本上是对的，不过模型、数据库和数据集是在NFS之上的k8s 的 PV上（如下图所示）。
           

        另外：Worker节点的5.21T HDD暂时没有用到！，明天跟相关部署的同事和阿廖确认后再回复他们。


## Storage Path for Datasets,  Wednesday, May 26, 2021

Today I wanted to upload a big dataset to the XXXXXX platform. 
Because it was so big I moved the files via SSH directly to the server and unzipped them. 
After that I created in the platform with “Add Data Set” a new entry and selected “Upload new dataset from other sources”.
After submitting I always get the error message: “File or path does not exist”
The Path via SSH is: /home/XXXXXX/dataset/coco2017/
Additionally, I saw that some dataset from you were already uploaded in the /home/XXXXXX/dataset/… directory. But when clicking on the Dataset in the Platform then I can see that the path is /data/dataset/storage/…
This is confusing. If I manually uploading files via SSH, in which folder do I have to put them? And does the path have to be on the server running the XXXXXX web application?
* Answer
For this issue, We recommend that you could upload big datasets files in `/data/dataset/storage/…` path via 
Rest assured, The datasets are not saved directly on the server machine HDD.
We  recommend that do not copy the datasets folder into  personal home path `/home/XXXXXX/dataset/` after uploaded.         
Thank you for your good questions, we will improve and update the operations documentation,  providing Better operational experience.

问题定位
用户第一次上传的是job 容器中的当前用户目录，该目录在平台下是不可见的，或者说在NFS/CEPH系统下不可见；
用户第二次上传的/data/dataset/storage/ 是挂载的目录，该目录映射在文件系统，平台可以看到；但这个是公共的预置数据集路径，现在只能用这个路径上传数据集！

## Parallel training on two cards in Jupyter， Thu, May 27, 2021, 20:35 

Today I try to train a network from the official model zoo in the Jupyter environment from the XXXXXX code development.
In code development I selected 2 number of devices. 
In Jupyter I can see the two cards with the command npu-smi info.
But as described in many readme files for the distributed training you have to create a rank_table.json file first. I tried the python tool from the model zoo: python hccl_tools.py –device_num “[0,2)”, but this is not working, because in the code development environment no file /etc/hccn.conf is available. 
So, can you tell me how to create a rank_table.json file for distributed training?
Second problem: During testing the YoloV4 network I get a huge mess of warnings:
Mostly this one:
[WARNING] KERNEL(22194,python):2021-05-27-13:50:51.418.973 [mindspore/ccsrc/backend/kernel_compiler/tbe/tbe_kernel_build.cc:479] GetSocVersion] SocVerison change to Ascend910
Can you tell me the meaning of this message? I think this slows down the training process. 
Please have a look on the attached log file. 
* Anwser
 The first problem：ranck_table.json has been set at the `/home/$DLWS_USER_NAME/.npu/$DLWS_JOB_ID/hccl_ms.json`，when the platform create your job, you can use this configuration. 
Unfortunately , we are not sure the IP address for NPU cards，so you could not use the 2 cards NPU training, If you don't mind too much，we can repair  NPU IP address remotely on-line.
The second problem:  It doesn`t matter, because the Huawei Mindspore team have confirmed that mindspore  will reduce the those WARNING LOGS print on next version.
问题定位
2个问题找了算法组同事帮忙看了：
1.	要用我们平台的hccl文件，文件在/home/$DLWS_USER_NAME/.npu/$DLWS_JOB_ID/hccl_ms.json，
2.	warning日志是正常的，华为说mindspore之后的版本会减少这种日志信息
单机2卡的分布式训练要配置NPU IP，由于是新人部署的没有配置。这个需要运维支持！
 
需在裸机下执行 `cat /etc/hccl.conf`, 如果没有配置，需要使用root执行
  ```bash
  hccn_tool -i 0 -ip -s address 192.168.10.11 netmask 255.255.255.0
  hccn_tool -i 1 -ip -s address 192.168.20.11 netmask 255.255.255.0
  hccn_tool -i 2 -ip -s address 192.168.30.11 netmask 255.255.255.0
  hccn_tool -i 3 -ip -s address 192.168.40.11 netmask 255.255.255.0
  hccn_tool -i 4 -ip -s address 192.168.10.12 netmask 255.255.255.0
  hccn_tool -i 5 -ip -s address 192.168.20.12 netmask 255.255.255.0
  hccn_tool -i 6 -ip -s address 192.168.30.12 netmask 255.255.255.0
  hccn_tool -i 7 -ip -s address 192.168.40.12 netmask 255.255.255.0
  ```

