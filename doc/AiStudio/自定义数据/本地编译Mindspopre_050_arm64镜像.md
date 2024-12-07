# 本地编译Mindspore 0.5.0基础镜像

1. 引用基础镜像

  `FROM apulistech/ubuntu:18.04-python375-withtools`

2. 设置工作目录

  `WORKDIR /usr/local/Ascend`

3. 拷贝依赖文件

  ```yaml
  COPY ./Ascend/  /usr/local/Ascend/
  COPY slog.conf .
  ```

4. 安装依赖
    ```yaml
    RUN pwd && ls -la /usr/local/Ascend/
    RUN pip3.7 list
    RUN pip3.7 install  --upgrade pip
    RUN pip3.7 install  ./nnae/20.0.RC1/arm64-linux_gcc7.3.0/fwkacllib/lib64/hccl-0.1.0-py3-none-any.whl
    RUN pip3.7 install  ./nnae/20.0.RC1/arm64-linux_gcc7.3.0/fwkacllib/lib64/te-0.4.0-py3-none-any.whl
    RUN pip3.7 install  ./nnae/20.0.RC1/arm64-linux_gcc7.3.0/fwkacllib/lib64/topi-0.4.0-py3-none-any.whl
    RUN pip3.7 install  ./tensorflow-0.5.0.0-cp37-cp37m-linux_aarch64.whl
    RUN echo 'install mindspore'
    # 在线安装 Mindspore 0.5.0
    RUN pip3.7 install https://ms-release.obs.cn-north-4.myhuaweicloud.com/0.5.0-beta/MindSpore/ascend/ubuntu_aarch64/mindspore_ascend-0.5.0-cp37-cp37m-linux_aarch64.whl
    ```

5. 设置环境变量
    ```yaml
    # The root directory of run package
    ENV LOCAL_ASCEND=/usr/local/Ascend

    # Lib libraries that the run package depends on
    ENV LD_LIBRARY_PATH=\
    /usr/lib/aarch64-linux-gnu/hdf5/serial:\
    ${LOCAL_ASCEND}/add-ons:\
    ${LOCAL_ASCEND}/nnae/20.0.RC1/arm64-linux_gcc7.3.0/fwkacllib/lib64:\
    ${LOCAL_ASCEND}/driver/lib64/common:\
    ${LOCAL_ASCEND}/driver/lib64/driver:\
    /usr/local/lib\:\
    /usr/lib/:\
    /lib
    # Environment variables that must be configured
    # TBE operator implementation tool path
    ENV TBE_IMPL_PATH=${LOCAL_ASCEND}/ascend-toolkit/20.0.RC1/arm64-linux_gcc7.3.0/opp/op_impl/built-in/ai_core/tbe

    # TBE operator compilation tool path
    ENV PATH=${LOCAL_ASCEND}/ascend-toolkit/20.0.RC1/arm64-linux_gcc7.3.0/fwkacllib/ccec_compiler/bin/:${PATH}

    # Python library that TBE implementation depends on
    ENV PYTHONPATH=${TBE_IMPL_PATH}:${PYTHONPATH}
    ENV ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/20.0.RC1/arm64-linux_gcc7.3.0/opp
    ```

6. 执行编译

  ```bash
  # Build 
  docker build -f ./Dockerfile-ms-withtools-rc1  .  -t ms:0.5.0-rc1
  ```

7. 查看镜像基本信息

  ```bash
  docker inspect ms:0.5.0-rc1  # Docker 查看镜像详情 
  docker history --no-trunc ms:0.5.0-rc1 # Docker 查看镜像更新详情
  ```

8. 执行镜像，验证工具包是否可执行

  ```bash
  # docker run
  docker run -it --rm --privileged -v /dlwsdata/storage/:/data/ -v /var/log/npu/:/var/log/npu/ -v /var/log/npu/:/var/log/npu/ ms:101-arm64 bash
  
  # 使用配置好的resnet50_050和cifar10数据集执行实例
  source /pod.env && cd /data/resnet50_050/scripts/ && mkdir -p /var/log/npu/conf/slog/ && mkdir -p /var/log/npu/slog && cp slog.conf /var/log/npu/conf/slog/ && ./run_distribute_train_1pcs.sh resnet50 cifar10 rank_table_1pcs.json /data/resnet50_cifar10/cifar/ &&sleep infinity
  ```

9. tag , 同步镜像

  ```bash
  docker tag ms:0.5.0-rc1 apulistech/ms:0.5.0-arm-rc1
  docker push apulistech/ms:0.5.0-arm-rc1
  ```

## 示例dockerfile

```yaml
#FROM build-base:latest
FROM apulistech/ubuntu:18.04-python375-withtools
#RUN apt-get update -y

#RUN apt-get install -y build-essential libhdf5-dev pkg-config libhdf5-103 libatlas-base-dev gfortran sudo

WORKDIR /root/

COPY Ascend /usr/local/Ascend

WORKDIR /usr/local/Ascend/

RUN pip3.7 config set global.index-url https://mirrors.aliyun.com/pypi/simple/

RUN pip3.7 install ./nnae/20.0.RC1/arm64-linux_gcc7.3.0/fwkacllib/lib64/topi-0.4.0-py3-none-any.whl
RUN pip3.7 install ./nnae/20.0.RC1/arm64-linux_gcc7.3.0/fwkacllib/lib64/te-0.4.0-py3-none-any.whl
RUN pip3.7 install ./nnae/20.0.RC1/arm64-linux_gcc7.3.0/fwkacllib/lib64/hccl-0.1.0-py3-none-any.whl

RUN echo 'install mindspore'
#RUN pip3 install ./tfplugin/20.0.0.B035/arm64-linux_gcc7.3.0/tfplugin/bin/npu_bridge-0.5.0.0-py3-none-any.whl
RUN pip3.7 install https://ms-release.obs.cn-north-4.myhuaweicloud.com/0.5.0-beta/MindSpore/ascend/ubuntu_aarch64/mindspore_ascend-0.5.0-cp37-cp37m-linux_aarch64.whl
RUN apt-get install vim -y

# control log level. 0-DEBUG, 1-INFO, 2-WARNING, 3-ERROR, default level is WARNING.
ENV GLOG_v=2
# Conda environmental options
# the root directory of run package
ENV LOCAL_ASCEND=/usr/local/Ascend
# lib libraries that the run package depends on
ENV LD_LIBRARY_PATH=\
/usr/lib/aarch64-linux-gnu/hdf5/serial:\
${LOCAL_ASCEND}/add-ons:\
${LOCAL_ASCEND}/nnae/20.0.RC1/arm64-linux_gcc7.3.0/fwkacllib/lib64:\
${LOCAL_ASCEND}/driver/lib64/common:\
${LOCAL_ASCEND}/driver/lib64/driver:\
/usr/local/lib\:\
/usr/lib/
# Environment variables that must be configured
# TBE operator implementation tool path
ENV TBE_IMPL_PATH=${LOCAL_ASCEND}/ascend-toolkit/20.0.RC1/arm64-linux_gcc7.3.0/opp/op_impl/built-in/ai_core/tbe
# TBE operator compilation tool path
ENV PATH=${LOCAL_ASCEND}/ascend-toolkit/20.0.RC1/arm64-linux_gcc7.3.0/fwkacllib/ccec_compiler/bin/:${PATH}
# Python library that TBE implementation depends on
ENV PYTHONPATH=${TBE_IMPL_PATH}:${PYTHONPATH}

RUN ln -s /lib /lib64

```