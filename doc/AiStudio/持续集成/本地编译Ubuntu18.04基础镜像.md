# 本地编译Ubuntu18.04基础镜像


1. 引用基础镜像

  | OS    | Version | Arct |
  |:------|:--------|:-----|
  |Ubuntu | 18.04.1 | arm64|

  `FROM ubuntu:18.04`

2. 设置工作目录

  `WORKDIR /home/docker-build/`

3. OS基础配置

  ```bash
  # 设置时区
  cat /etc/timezone
  # 列出时区：
  timedatectl list-timezones
  timedatectl set-timezone Asia/Shanghai
  ```
  ```yaml
  RUN timedatectl set-timezone Asia/Shanghai
  RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
  ```
  * 配置log等级：control log level. 0-DEBUG, 1-INFO, 2-WARNING, 3-ERROR, default level is WARNING.

    `ENV GLOG_v=2`

4. 设置安装源，基础依赖,请参考示例
  
  * apt推荐安装源： https://repo.huaweicloud.com/ubuntu-ports/
  * pip推荐安装源： https://mirrors.aliyun.com/pypi/simple
  * 常用apt依赖安装：
  ```
  RUN apt-get update && apt-get -y  install ca-certificates
  RUN sudo apt-get -y install build-essential libhdf5-dev pkg-config  libatlas-base-dev gfortran software-properties-common  systemd apt-utils sudo  unzip --fix-missing
  RUN sudo apt-get -y install --no-install-recommends   git   mercurial   openssh-client   subversion  procps   ca-certificates   curl   netbase   wget  && rm -rf /var/lib/apt/lists/*
  RUN sudo apt-get update && apt-get -y install libhdf5-serial-dev python-tables python3-dev  zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev wget libbz2-dev
  ```
  * 安装Job Init tools， 为避免Job 创建时安装依赖包超时中断，预先将必要包安装好
  ```
  RUN ln -s /lib /lib64
  RUN apt-get update && apt-get install -y net-tools
  RUN apt-get install -y iproute2
  RUN apt-get install openssl -y
  RUN apt-get install vim -y
  ```

  * 本地编译安装python3.7.5
  *注意： 编译时加--enable-shared选项，将生成的libpython3.7m.so.1.0动态链接库拷贝到 /usr/lib下 *
  ```
  RUN  wget https://www.python.org/ftp/python/3.7.5/Python-3.7.5.tgz --no-check-certificate
  # For faster build time, modify the -j flag according to your processor. If you do not know the number of cores your processor, you can find it by typing nproc
  RUN tar -xf Python-3.7.5.tgz && cd Python-3.7.5 && ./configure --enable-shared --enable-universalsdk --enable-optimizations && make -j 192 && make altinstall
  RUN cp Python-3.7.5/libpython3.7m.so.1.0 /usr/lib
  RUN cp Python-3.7.5/libpython3.7m.so /usr/lib
  RUN cp Python-3.7.5/libpython3.so /usr/lib
  ```
  * 安装pip 依赖包，避免模型执行时超时中断
  ```
  RUN pip3.7 config set global.index-url https://mirrors.aliyun.com/pypi/simple  # 配置pip安装代理
  RUN pip3.7 install --upgrade pip
  RUN pip3.7 install tensorboard && \
      pip3.7 install numpy && \
      pip3.7 install decorator && \
      pip3.7 install sympy==1.4 && \
      pip3.7 install cffi==1.12.3 && \
      pip3.7 install pyyaml && \
      pip3.7 install pathlib2 && \
      pip3.7 install grpcio && \
      pip3.7 install grpcio-tools && \
      pip3.7 install protobuf && \
      pip3.7 install scipy && \
      pip3.7 install requests && \
      pip3.7 install jupyterlab && \
      pip3.7 install sympy && \
      pip3.7 install Cython
  ```


5. 设置环境变量
  ```yaml
  # control log level. 0-DEBUG, 1-INFO, 2-WARNING, 3-ERROR, default level is WARNING.
  ENV GLOG_v=2

  # lib libraries that the run package depends on
  ENV LD_LIBRARY_PATH=\
  /usr/lib/aarch64-linux-gnu/hdf5/serial:\
  ${LOCAL_ASCEND}/add-ons:\
  ${LOCAL_ASCEND}/driver/lib64/common:\
  ${LOCAL_ASCEND}/driver/lib64/driver:\
  /usr/local/lib\:\
  /usr/lib/

  # Python library that TBE implementation depends on
  ENV PYTHONPATH=${TBE_IMPL_PATH}:${PYTHONPATH}
  ENV ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/20.0.RC1/arm64-linux_gcc7.3.0/opp
  ```
6. 执行编译

  ```bash
  # Build 
  docker build -f ./Dockerfile-ubuntu1804  .  -t ubuntu:18.04-python375-withtools
  ```

7. 查看镜像基本信息

  ```bash
  docker inspect docker.io/mysql:5.7  # Docker 查看镜像详情 
  docker history --no-trunc docker.io/mysql:5.7 # Docker 查看镜像更新详情
  ```

8. 执行镜像，验证工具包是否可执行

  ```bash
  # docker run
  docker run -it --rm --privileged -v /dlwsdata/storage/:/data/ -v /var/log/npu/:/var/log/npu/ -v /var/log/npu/:/var/log/npu/ apulistech/ubuntu:18.04-python375-withtools
  ```
9. tag , 同步镜像

  ```bash
  docker tag ubuntu:18.04-python375-withtools apulistech/ubuntu:18.04-python375-withtools
  docker push apulistech/ubuntu:18.04-python375-withtools
  ```

## 示例dockerfile

```yaml
FROM ubuntu:18.04
WORKDIR /home/docker-build/

RUN apt-get update && apt install ca-certificates -y

RUN echo "deb  https://repo.huaweicloud.com/ubuntu-ports/ bionic main restricted universe multiverse" >/etc/apt/sources.list && \
    echo "deb-src   https://repo.huaweicloud.com/ubuntu-ports/ bionic main restricted universe multiverse" >>/etc/apt/sources.list && \
    echo "deb  https://repo.huaweicloud.com/ubuntu-ports/ bionic-security main restricted universe multiverse" >>/etc/apt/sources.list && \
    echo "deb-src  https://repo.huaweicloud.com/ubuntu-ports/ bionic-security main restricted universe multiverse" >>/etc/apt/sources.list && \
    echo "deb  https://repo.huaweicloud.com/ubuntu-ports/ bionic-updates main restricted universe multiverse" >>/etc/apt/sources.list && \
    echo "deb-src  https://repo.huaweicloud.com/ubuntu-ports/ bionic-updates main restricted universe multiverse" >>/etc/apt/sources.list && \
    echo "deb  https://repo.huaweicloud.com/ubuntu-ports/ bionic-backports main restricted universe multiverse" >>/etc/apt/sources.list

# Install net-tools and anopther packages
RUN apt-get update -y && apt-get install -y systemd apt-utils sudo  --fix-missing
RUN echo "Asia/Shanghai" | tee /etc/timezone  && ln -sf /usr/share/zoneinfo/Asia/Shanghai  /etc/localtime
RUN sudo apt-get -y install build-essential libhdf5-dev pkg-config  libatlas-base-dev gfortran  software-properties-common  net-tools  iproute2  openssl  vim
RUN sudo apt-get -y install --no-install-recommends   git   mercurial   openssh-client   subversion   procps ca-certificates   curl   netbase   wget && rm -rf /var/lib/apt/lists/*
RUN sudo apt-get update && apt-get -y install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev wget libbz2-dev libhdf5-serial-dev python-tables python3-dev

# Install python3.7.5
RUN  wget https://www.python.org/ftp/python/3.7.5/Python-3.7.5.tgz --no-check-certificate
# For faster build time, modify the -j flag according to your processor. If you do not know the number of cores your processor, you can find it by typing nproc
RUN tar -xf Python-3.7.5.tgz && cd Python-3.7.5 && ./configure --enable-shared --enable-universalsdk --enable-optimizations && make -j 192 && make altinstall
RUN cp Python-3.7.5/libpython3.7m.so.1.0 /usr/lib  && cp Python-3.7.5/libpython3.7m.so /usr/lib && cp Python-3.7.5/libpython3.so /usr/lib
RUN rm -rf Python-3.7.5*

# 配置pip安装代理
RUN pip3.7 config set global.index-url https://mirrors.aliyun.com/pypi/simple

# Install py-tools
RUN sudo apt-get -y install python3.7-dev 
RUN ln -s /lib /lib64
RUN pip3.7 install --upgrade pip  && \
    pip3.7 install tensorboard && \
    pip3.7 install numpy && \
    pip3.7 install decorator && \
    pip3.7 install sympy==1.4 && \
    pip3.7 install cffi==1.12.3 && \
    pip3.7 install pyyaml && \
    pip3.7 install pathlib2 && \
    pip3.7 install grpcio && \
    pip3.7 install grpcio-tools && \
    pip3.7 install protobuf && \
    pip3.7 install scipy && \
    pip3.7 install requests && \
    pip3.7 install jupyterlab && \
    pip3.7 install sympy && \
    pip3.7 install Cython
```