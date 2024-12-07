# 本地编译Tensorflow 1.15基础镜像


1. 引用基础镜像

  `FROM apulistech/ubuntu:18.04-python375-withtools`

2. 设置工作目录

  `WORKDIR /usr/local/Ascend`

3. 拷贝依赖文件

  ```yaml
  COPY ./Ascend/  /usr/local/Ascend/
  COPY tensorflow-1.15.0-cp37-cp37m-linux_aarch64.whl .
  COPY slog.conf .
  ```

4. 安装依赖
    ```yaml
    RUN pwd && ls -la /usr/local/Ascend/
    RUN pip3.7 list
    RUN pip3.7 install  --upgrade pip
    RUN pip3.7 install  ./tfplugin/latest/arm64-linux_gcc7.3.0/tfplugin/bin/npu_bridge-1.15.0-py3-none-any.whl
    RUN pip3.7 install  ./nnae/latest/arm64-linux_gcc7.3.0/fwkacllib/lib64/hccl-0.1.0-py3-none-any.whl
    RUN pip3.7 install  ./nnae/latest/arm64-linux_gcc7.3.0/fwkacllib/lib64/te-0.4.0-py3-none-any.whl
    RUN pip3.7 install  ./nnae/latest/arm64-linux_gcc7.3.0/fwkacllib/lib64/topi-0.4.0-py3-none-any.whl
    RUN pip3.7 install  ./tensorflow-1.15.0-cp37-cp37m-linux_aarch64.whl
    ```
5. 设置环境变量
    ```yaml
    # The root directory of run package
    ENV LOCAL_ASCEND=/usr/local/Ascend

    # Lib libraries that the run package depends on
    ENV LD_LIBRARY_PATH=\
    /usr/lib/aarch64-linux-gnu/hdf5/serial:\
    ${LOCAL_ASCEND}/add-ons:\
    ${LOCAL_ASCEND}/nnae/latest/arm64-linux_gcc7.3.0/fwkacllib/lib64:\
    ${LOCAL_ASCEND}/driver/lib64/common:\
    ${LOCAL_ASCEND}/driver/lib64/driver:\
    /usr/local/lib\:\
    /usr/lib/:\
    /lib
    # Environment variables that must be configured
    # TBE operator implementation tool path
    ENV TBE_IMPL_PATH=${LOCAL_ASCEND}/ascend-toolkit/latest/arm64-linux_gcc7.3.0/opp/op_impl/built-in/ai_core/tbe

    # TBE operator compilation tool path
    ENV PATH=${LOCAL_ASCEND}/ascend-toolkit/latest/arm64-linux_gcc7.3.0/fwkacllib/ccec_compiler/bin/:${PATH}

    # Python library that TBE implementation depends on
    ENV PYTHONPATH=${TBE_IMPL_PATH}:${PYTHONPATH}
    ENV ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/arm64-linux_gcc7.3.0/opp
    ```
    
6. 执行编译

  ```bash
  # Build 
  docker build -f ./Dockerfile-tf-withtools-rc1  .  -t tf:1.15-rc1
  ```

7. 查看镜像基本信息

  ```bash
  docker inspect docker.io/mysql:5.7  # Docker 查看镜像详情 
  docker history --no-trunc docker.io/mysql:5.7 # Docker 查看镜像更新详情
  ```

8. 执行镜像，验证工具包是否可执行

  * 本地验证
    ```bash
    # docker run
    docker run -it --rm --privileged -v /dlwsdata/storage/:/data/ -v /var/log/npu/:/var/log/npu/ -v /var/log/npu/:/var/log/npu/ apulistech/tf:1.15-rc201-arm64 bash
    # 登录python3.7.5终端模拟环境
    python3.7
    # 查看关键依赖是否可以正常导入
    import tensorflow
    import npu_bridge
    ```
  * 调试常用模型验证
    
    建议参考Resnet 0.5.0 在Tensorflow 1.15环境调试实例，如果可以正常执行完模型，则证明该镜像是可以被使用的。
    ```bash
    # 需要提前配置好模型参数，有其是配置文件路径
    sudo -E bash -c 'source /pod.env && cp /data/Resnet50_HC /tmp/ && cd /tmp/Resnet50_HC/ &&  ./run_apulis_rc1.sh &&sleep infinity'

    ```


  **注意：**

    *如果依赖包导入没有问题，则说明tensorflow镜像是可用的，在调试模型的具体情况下需要确认一些依赖包或动态链接库是否配置正确*
    *例如： 在调试resnet 0.5.0 模型时需要将libpython3.7m.so.1.0 拷贝到/usr/lib下*
  
9. tag , 同步镜像

  ```bash
  docker tag tf:1.15-rc1 apulistech/tf:1.15-arm-rc1
  docker push apulistech/tf:1.15-arm-rc1
  ```

## 示例dockerfile

```yaml
FROM apulistech/ubuntu:18.04-python375-withtools
WORKDIR /usr/local/Ascend

COPY ./Ascend/  /usr/local/Ascend/
COPY tensorflow-1.15.0-cp37-cp37m-linux_aarch64.whl .
COPY slog.conf .

RUN pwd && ls -la /usr/local/Ascend/
RUN pip3.7 list
RUN pip3.7 install  --upgrade pip
RUN pip3.7 install  ./tfplugin/latest/arm64-linux_gcc7.3.0/tfplugin/bin/npu_bridge-1.15.0-py3-none-any.whl
RUN pip3.7 install  ./nnae/latest/arm64-linux_gcc7.3.0/fwkacllib/lib64/hccl-0.1.0-py3-none-any.whl
RUN pip3.7 install  ./nnae/latest/arm64-linux_gcc7.3.0/fwkacllib/lib64/te-0.4.0-py3-none-any.whl
RUN pip3.7 install  ./nnae/latest/arm64-linux_gcc7.3.0/fwkacllib/lib64/topi-0.4.0-py3-none-any.whl
RUN pip3.7 install  ./tensorflow-1.15.0-cp37-cp37m-linux_aarch64.whl

# The root directory of run package
ENV LOCAL_ASCEND=/usr/local/Ascend

# Lib libraries that the run package depends on
ENV LD_LIBRARY_PATH=\
/usr/lib/aarch64-linux-gnu/hdf5/serial:\
${LOCAL_ASCEND}/add-ons:\
${LOCAL_ASCEND}/nnae/latest/arm64-linux_gcc7.3.0/fwkacllib/lib64:\
${LOCAL_ASCEND}/driver/lib64/common:\
${LOCAL_ASCEND}/driver/lib64/driver:\
/usr/local/lib\:\
/usr/lib/:\
/lib
# Environment variables that must be configured
# TBE operator implementation tool path
ENV TBE_IMPL_PATH=${LOCAL_ASCEND}/ascend-toolkit/latest/arm64-linux_gcc7.3.0/opp/op_impl/built-in/ai_core/tbe

# TBE operator compilation tool path
ENV PATH=${LOCAL_ASCEND}/ascend-toolkit/latest/arm64-linux_gcc7.3.0/fwkacllib/ccec_compiler/bin/:${PATH}

# Python library that TBE implementation depends on
ENV PYTHONPATH=${TBE_IMPL_PATH}:${PYTHONPATH}
ENV ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/arm64-linux_gcc7.3.0/opp

```


## 非root 用户编译镜像


以下目录需要改为 777 ,在平台使用普通用户模型训练调用npu的时候，编译镜像的时候。

/dev/devmm_svm
crwxrwxrwx 1 HwHiAiUser HwHiAiUser 235, 0 Nov 23 10:28 /dev/devmm_svm
/dev/hisi_hdc
crwxrwxrwx 1 HwHiAiUser HwHiAiUser 511, 0 Nov 23 10:28 /dev/hisi_hdc
root@atlas01:~/driver_arm64/docker# ll /dev/davinci
davinci0         davinci2         davinci4         davinci6         davinci_manager
davinci1         davinci3         davinci5         davinci7

海思环境数据备份： 目前主要备份是master节点 l21.37.54.27 
数据目录在： /mnt/local 
平台用户的数据在: /mnt/local/work/

目录数据总体大概1.2T； 


李博您好：
DLWorkspace稳定的环境仅有海思南京高校环境：（预计下周二2020-12-1会下电合并到算子众筹环境中）
http://121.37.54.27/ 账号： haiyuan 密码： Apulis@2020

openlab部署的AIArts环境：
http://183.129.171.130:8461/  账号： apulis 密码： 123456

算法组使用GPU集群部署的是AIArts:
http://china-gpu02.sigsus.cn/ 账号：admin  密码： Apulis12#$