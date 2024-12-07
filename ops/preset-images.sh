
### 更新安装源
cp /etc/apt/sources.list /etc/apt/sources.list.bak
sed -i "s@http://.*archive.ubuntu.com@http://repo.huaweicloud.com@g" /etc/apt/sources.list
sed -i "s@http://.*security.ubuntu.com@http://repo.huaweicloud.com@g" /etc/apt/sources.list
apt update 

### Anaconda

wget https://repo.anaconda.com/archive/Anaconda3-2021.05-Linux-x86_64.sh
chmod +x Anaconda3-2021.05-Linux-x86_64.sh
bash Anaconda3-2021.05-Linux-x86_64.sh

### Dependance

cd /root/anaconda3
conda env create -f environment.yml

https://github.com/YudongGuo/AD-NeRF/blob/master/environment.yml


docker pull nvidia/cudagl:11.2.2-base-ubuntu18.04

docker run -it --rm nvidia/cudagl:11.2.2-base-ubuntu18.04 bash

docker run --rm -v /usr/bin:/usr/bin --privileged -v $(pwd)/init_user.sh:/init_user.sh nvidia/cudagl:11.2.2-base-ubuntu18.04 bash /init_user.sh


```bash
uname -ma
apt update \
   && apt install -y sudo ifconfig  ip  getent usermod    addgroup   adduser    groupadd   runuser    printenv   awk 
   # python3
```

* 初始化脚本执行问题
以初始化用户这个脚本为例 https://apulis-gitlab.apulis.cn/apulis/DLWorkspace/-/blob/develop/src/init-scripts/init_user.sh 

```bash
#/bin/bash
set -ex

#export POD_NAME=
#export DLWS_GID=
#export DLWS_UID=
#export DLWS_USER_NAME=

export ENV_FILE=/pod.env
rm -rf ${ENV_FILE}  # need to remove it if there is already one there

# install required pkgs
export DEBIAN_FRONTEND=noninteractive
# time apt-get update && time apt-get install sudo openssl -y

# setup user and group, fix permissions
if id "${DLWS_USER_NAME}" &>/dev/null;
then
    echo "User ${DLWS_USER_NAME} found, skip adding user ..."
else
    addgroup --force-badname --gid  ${DLWS_GID} domainusers
    adduser --force-badname --home /home/${DLWS_USER_NAME} --shell /bin/bash --uid ${DLWS_UID}  -gecos '' --gid ${DLWS_GID} --disabled-password ${DLWS_USER_NAME}
    usermod -p $(echo ${DLTS_JOB_TOKEN} | openssl passwd -1 -stdin) ${DLWS_USER_NAME}

    chown ${DLWS_USER_NAME} /home/${DLWS_USER_NAME}/ /home/${DLWS_USER_NAME}/.profile /home/${DLWS_USER_NAME}/.ssh || /bin/true
    chmod 700 /home/${DLWS_USER_NAME}/.ssh || /bin/true
    chmod 755 /home/${DLWS_USER_NAME} || /bin/true

    # setup sudoers
    adduser $DLWS_USER_NAME sudo
    echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
fi

# export envs
# options '-e' for exported ENVs only
compgen -e | while read line; do
        if [[ $line != HOME* ]] && [[ $line != INTERACTIVE* ]] && [[ $line != LS_COLORS* ]]  && [[ $line != PATH* ]] && [[ $line != PWD* ]]; then
            # Since bash >= 4.4 we could use
            # echo "export ${line}=${!line@Q}" >> "${ENV_FILE}" ;
            # For compatible with bash < 4.4
            printf "export ${line}=%q\n" "${!line}" >> "${ENV_FILE}" ;
        fi; done
echo "export PATH=$PATH:\${PATH}" >> "${ENV_FILE}"
echo "export LD_LIBRARY_PATH=/usr/local/nvidia/lib64/:\${LD_LIBRARY_PATH}" >> "${ENV_FILE}"

# source the envs
if [ -f /etc/bash.bashrc ]; then
  chmod 644 /etc/bash.bashrc
fi

grep -qx "^\s*. ${ENV_FILE}" /home/${DLWS_USER_NAME}/.profile || cat << SCRIPT >> "/home/${DLWS_USER_NAME}/.profile"
if [ -f ${ENV_FILE} ]; then
    . ${ENV_FILE}
fi
SCRIPT



# any command should run as ${DLWS_USER_NAME}
#runuser -l ${DLWS_USER_NAME} -c your_commands

```


### 在本地 docker run 下都可以执行,在代码开发环境下：

    + 可以执行的命令： 
    set 
    export 
    grep

    + 已安装的没有权限执行：
    cat 
    rm
    addgroup
    adduser
    usermod
    compgen 
    chmod
    没有安装的：
    sudo 
    ifconfig
    ip

## 原镜像执行初始化脚本问题

小冰提供的镜像xixiao/cudagl10.2-conda-torch:v0.4

一般会执行报错 （在apt update 时候）Download is performed unsandboxed as root as file '/var/lib/apt/lists/partial/archive.ubuntu.com_ubuntu_dists_bionic_InRelease' couldn't be accessed by user '_apt'. - pkgAcquire::Run (13: Permission denied)

执行命令可能需要加这样的配置   -o Acquire::GzipIndexes=false -o APT::Sandbox::User=root  例如  apt-get -o Acquire::GzipIndexes=false -o APT::Sandbox::User=root update 



```bash
# Basement 
## PyTorch: 21.02
## It is pre-built and installed in Conda default environment (/opt/conda/lib/python3.8/site-packages/torch/) in the container image.

## The container also includes the following:
## Ubuntu 20.04 including Python 3.8 environment
## NVIDIA CUDA 11.2.0 including cuBLAS 11.3.1
## NVIDIA cuDNN 8.1.0
## tensorflow, paddle have installed in Conda

# Install dependance
# apt install -y sudo 
sudo apt update \
  && sudo apt install -y openssh-server   iputils-ping\
  && sudo apt install -y unzip zip tar  \
  && sudo apt install -y wget curl 

# Allow PermitRootLogin prohibit-password
sudo sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
sudo service ssh reload
sudo service ssh start
update-rc.d ssh defaults

# Install python 3.8 miniconda
## cd ~
## sudo wget https://repo.anaconda.com/miniconda/Miniconda3-py38_4.10.3-Linux-x86_64.sh
## sudo chmod +x Miniconda3-py38_4.10.3-Linux-x86_64.sh
## bash Miniconda3-latest-Linux-x86_64.sh
# Install cuda 
## sudo wget https://developer.download.nvidia.com/compute/cuda/11.4.1/local_installers/cuda_11.4.1_470.57.02_linux.run
## sudo chmod +x cuda_11.4.1_470.57.02_linux.run
## sudo sh cuda_11.4.1_470.57.02_linux.run
conda install -c paddle paddlepaddle
conda install -c conda-forge tensorflow
```
