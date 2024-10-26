# altals服务器初始化安装指导

## 安装主机操作系统

### 通过ibmc安装ubuntu步骤

### ibmc登录WEB页面

```bash
https://xxx.xxx.xxx.xxx
# 输入账号和密码
```

### 在虚拟终端挂载iso镜像，并启动安装

1. 打开首页右侧的虚拟终端，推荐选择html5共享窗口
   选择CD的`image`挂载镜像文件，千万不要选择`file`
2. 点击`connect` 执行卸载：
3. 选boot启动为CD/DVD
4. 选择启动命令为 `restart`
5. 进入系统安装界面，执行安装即可
6. 安装完成后将启动项改回`硬盘加载`
   **注意：**
7. 安装系统前，在iBMC中查看网口连接状态，和系统基本信息
8. 任何时候都要保留iBMC的网络配置

*参考：* [官方说明](https://support.huawei.com/enterprise/en/doc/EDOC1100048786/916c5c0a/mounting-a-file-to-the-virtual-cd-rom-drive-vmm--d-connect)

## 系统要求及环境检查

- 系统版本
  [ubuntu 18.04.1](http://cdimage.ubuntu.com/ubuntu/releases/18.04/release/)


| 硬件形态 | host操作系统版本 | 软件包默认的host操作系统内核版本 |
| :- | :- | :- |
| aarch64+Atlas 800 9000 | Ubuntu 18.04.1 | 4.15.0-99-generic |

- 基础软件
  - cmake:３.５.２
  - gcc:7.3.0
  - python:3.7.5

### apt配置源

apt推荐安装源：https://mirrors.huaweicloud.com/

+ 需要区分主机是x86架构，Arm64架构的。Arm64选择Ubuntu-Ports:

```bash
sudo cp -a /etc/apt/sources.list /etc/apt/sources.list.bak
sudo wget -O /etc/apt/sources.list https://repo.huaweicloud.com/repository/conf/Ubuntu-Ports-bionic.list
sudo wget -O /etc/apt/sources.list https://repo.huaweicloud.com/repository/conf/Ubuntu-Ports-cosmic.list
sudo wget -O /etc/apt/sources.list https://repo.huaweicloud.com/repository/conf/Ubuntu-Ports-disco.list
sudo wget -O /etc/apt/sources.list https://repo.huaweicloud.com/repository/conf/Ubuntu-Ports-eoan.list
sudo wget -O /etc/apt/sources.list https://repo.huaweicloud.com/repository/conf/Ubuntu-Ports-precise.list
sudo wget -O /etc/apt/sources.list https://repo.huaweicloud.com/repository/conf/Ubuntu-Ports-trusty.list
sudo wget -O /etc/apt/sources.list https://repo.huaweicloud.com/repository/conf/Ubuntu-Ports-xenial.list
sudo apt-get update
```

* x86架构的请选择 Ubuntu镜像源

```bash
sudo cp -a /etc/apt/sources.list /etc/apt/sources.list.bak
sudo sed -i "s@http://.*archive.ubuntu.com@http://repo.huaweicloud.com@g" /etc/apt/sources.list
sudo sed -i "s@http://.*security.ubuntu.com@http://repo.huaweicloud.com@g" /etc/apt/sources.list
apt-get update
```

### 升级内核

1. 查看已经安装的内核

```
root@master:/home# ll /lib/modules
总用量 12
drwxr-xr-x  3 root root 4096 12月 16 19:17 ./
drwxr-xr-x 23 root root 4096 12月 17 14:45 ../
drwxr-xr-x  6 root root 4096 12月 17 14:46 4.15.0-29-generic/


dpkg --get-selections | grep linux-modules

root@atlas02:~# dpkg --get-selections | grep linux-modules
linux-modules-4.15.0-129-generic                install
linux-modules-4.15.0-29-generic                 deinstall
linux-modules-4.15.0-99-generic                 install
linux-modules-extra-4.15.0-129-generic          install
linux-modules-extra-4.15.0-29-generic           deinstall
linux-modules-extra-4.15.0-99-generic           install
```

2. 卸载不需要的内核

**如果apt异常，需要先修复atp,否则卸载或安装是没有执行完的**

```bash
uname -sr && apt update  && apt remove --purge  -y Linux-headers-4.15.0-29  Linux-image-4.15.0-29-generic  linux-modules-4.15.0-29-generic   Linux-modules-extra-4.15.0-29-generic   Linux-tools-4.15.0-29-generic   linux-headers-4.15.0-29-generic

sudo apt --purge autoremove
```

3. 安装指定内核

```bash
uname -sr && apt update  && apt install -y Linux-headers-4.15.0-99  Linux-image-4.15.0-99-generic  linux-modules-4.15.0-99-generic   Linux-modules-extra-4.15.0-99-generic   Linux-tools-4.15.0-99-generic   linux-headers-4.15.0-99-generic
```

4. 重启

`reboot`

* 降级(若内核版本高于要求版本，则卸载高版本的内核包，再安装指定版本内核)

```bash
sudo dpkg -l | grep 4.15.0-0415
apt remove --purge  -y xxx (dpkg --purge xxx )
```

* faq: 内核头和内核版本不一致：

`less  /var/log/ascend_seclog/ascend_install.log`
`[ERROR]driver ko vermagic(4.15.0-45-generic) is different from the os(4.15.0-99-generic), need rebuild driver`

```
# 内核版本和内核头需保持一致，否则会影响编译，内核头升级命令：apt install linux-header- 4.x.x）；
apt install -y dkms
# dpkg查询命令Ubuntu操作系统： 
dpkg-query -s linux-headers-$(uname -r) 
apt install -y linux-headers-4.15.0-99-generic
```

### cmake3.5.2编译安装

**一般情况系统已安装 cmake3.5.2 以上版本，可不更新**

```bash
apt install -y cmake
# 也可选择源码安装
wget https://cmake.org/files/v3.5/cmake-3.5.2.tar.gz --no-check-certificate
tar -zxvf cmake-3.5.2.tar.gz && cd cmake-3.5.2 && ./bootstrap --prefix=/usr && make && make install && cmake --version
```

### gcc/g++7.3.0编译安装

**一般情况系统已安装gcc 7.5.0 以上版本，可不更新**

```bash

wget https://mirrors.tuna.tsinghua.edu.cn/gnu/gcc/gcc-7.3.0/gcc-7.3.0.tar.gz
rm -rf /tmp/  --run
apt-get install bzip2
tar -zxvf gcc-7.3.0.tar.gz
cd gcc-7.3.0

wget http://gcc.gnu.org/pub/gcc/infrastructure/gmp-6.1.0.tar.bz2
wget http://gcc.gnu.org/pub/gcc/infrastructure/mpfr-3.1.4.tar.bz2
wget http://gcc.gnu.org/pub/gcc/infrastructure/mpc-1.0.3.tar.gz
wget http://gcc.gnu.org/pub/gcc/infrastructure/isl-0.16.1.tar.bz2

./contrib/download_prerequisites
./configure --enable-languages=c,c++ --disable-multilib --with-system-zlib --prefix=/usr/local/gcc7.3.0
make -j120 # 通过grep -w processor /proc/cpuinfo|wc -l查看cpu数，示例为15，用户可自行设置相应参数。
```

### python安装

#### 依赖安装

```bash
apt install -y gcc make cmake zlib1g zlib1g-dev libbz2-dev openssl libsqlite3-dev libssl-dev libxslt1-dev libffi-dev unzip pciutils net-tools libblas-dev gfortran libblas3 libopenblas-dev
```

#### python编译安装

```bash
# 可换成拷贝本地的备份文件
wget https://www.python.org/ftp/python/3.7.5/Python-3.7.5.tgz
tar -zxvf Python-3.7.5.tgz && cd Python-3.7.5
./configure --enable-shared && make && make install
```

*确认`/usr/lib64/libpython3.7m.so.1.0`或`/usr/lib/libpython3.7m.so.1.0`是否存在，不存在则执行：*

```bash
cp ./libpython3.7m.so.1.0 /usr/lib && cp ./libpython3.7m.so.1.0 /lib && ln -s /lib /lib64
```

```bash
# mv  /usr/bin/lsb_release /usr/bin/lsb_release.bak
ln -s /usr/local/python3.7.5/bin/python3 /usr/bin/python3.7 && ln -s /usr/local/python3.7.5/bin/pip3 /usr/bin/pip3.7 && ln -s /usr/local/python3.7.5/bin/python3 /usr/bin/python3.7.5 && ln -s /usr/local/python3.7.5/bin/pip3 /usr/bin/pip3.7.5 

# 在此阶段不要删除系统默认安装的python3.6
# 如果 lsb_release -a 不能执行，恢复 python3.6
rm /usr/bin/python3
ln -s /usr/local/python3.6.9/bin/python3 /usr/bin/python3 && ln -s /usr/local/python3.7.5/bin/pip3 /usr/bin/pip3

python3 --version && pip3 --version
```

#### （国内）pip源配置和依赖包安装

```bash
pip3.7 config set global.index-url https://mirrors.aliyun.com/pypi/simple
pip3.7 install numpy decorator sympy==1.0  pyyaml  pathlib2 grpcio grpcio-tools  protobuf scipy requests
```

## 创建安装和运行用户

```bash
# 创建指定用户，用户组id: 1680用户目录为 /home/HwHiAiUser
useradd -u 1680 -s /bin/bash -m HwHiAiUser 
# 删除用户
userdel -r -f HwHiAiUser
# 验证用户ID是否为1680,输出需结果如下：
uid=1680(HwHiAiUser) gid=1680(HwHiAiUser) groups=1680(HwHiAiUser)
```

## 系统环境检查

```bash
uname -mr && cat /etc/*release
```

## 安装NPU驱动、固件和工具包

### 获取安装包

1. `cd /home/HwHiAiUser && mkdir -p ascend_date && cd ascend_date`
2. 下载所有的安装包[华为开发者社区](https://developer.huaweicloud.com/tool.html),[合作方分享](https://e-share.obs-website.cn-north-1.myhuaweicloud.com/?)

   ```bash
   # 根据实际情况确认具体版本号
   A800-9000-NPU_Driver-20.0.RC1-ARM64-Ubuntu18.04.run
   A800-9000-NPU_Firmware-1.73.1005.1.b050.run
   Ascend-NNAE-20.0.RC1-arm64-linux_gcc7.3.0.run
   Ascend-NNRT-20.0.RC1-arm64-linux_gcc7.3.0.run
   Ascend-TFPlugin-20.0.RC1-arm64-linux_gcc7.3.0.run
   Ascend-Toolbox-20.0.RC1-arm64-linux_gcc7.3.0.run
   Ascend-Toolkit-20.0.RC1-arm64-linux_gcc7.3.0.run
   ```
3. 使用root用户登录到运行环境，将  *.run软件包上传至到运行环境任意路径下，如/root下; 非root用户一般在$HOME下

### 非Root安装工具包

1. 创建HwHiAiUser为指定的uid，如下：

   `useradd -u 1680 -s /bin/bash -m HwHiAiUser`
2. 仍然在root用户下安装驱动和固件

   ```bash
   root@atlas01:~/driver-build#
   ./A800-9000-NPU_Driver-20.0.RC1-ARM64-Ubuntu18.04.run  --run
   ./A800-9000-NPU_Firmware-1.73.1005.1.b050.run          --run
   ```
3. 将安装包拷贝到HwHiAiUse用户目录下，并工具包的用户权限

   ```bash
   cp -r /root/<cann包mulu> /home/HwHiAiUse/<cann包目录>
   chown -R HwHiAiUser:HwHiAiUser /home/HwHiAiUser/<cann包目录>
   ```
4. 切换到HwHiAiUse登录，并执行 cann 安装

   ```bash
   su HwHiAiUser
   # 或退出root，以HwHiAiUse登录
   cd /home/HwHiAiUse/<cann包mulu>
   ./Ascend-cann-nnae_20.1.rc1_linux-aarch64.run           --install --install-path=/home/HwHiAiUser/Ascend
   ./Ascend-cann-nnrt_20.1.rc1_linux-aarch64.run           --install --install-path=/home/HwHiAiUser/Ascend
   ./Ascend-cann-toolkit_20.1.rc1_linux-aarch64.run        --install --install-path=/home/HwHiAiUser/Ascend
   ./Ascend-fwk-tfplugin_20.1.rc1_linux-aarch64.run        --install --install-path=/home/HwHiAiUser/Ascend
   ./Ascend-mindstudio-toolbox_20.1.rc1_linux-aarch64.run  --install --install-path=/home/HwHiAiUser/Ascend
   ```
5. 再次切换root登录，安装aicpu算子(20.2驱动没有这个步骤)

   ```bash
   cd /home/HwHiAiUser/Ascend/ascend-toolkit/20.1.rc1/arm64-linux/aicpu
   ./Ascend910-aicpu_kernels-1.75.22.0.220.run --run
   ```
6. 查看安装的驱动版本号。

在软件包的安装路径下，例如root用户默认路径`/usr/local/Ascend/${package_name}`，HwHiAiUser用户默认路径`/home/HwHiAiUser/Ascend/${package_name}`执行如下命令查看所升级软件包版本是否正确。

```bash
cat version.info
Version=1.73.T105.0.B050
```

亦或：

```bash
root@atlas01:~# cat /usr/local/Ascend/driver/version.info
Version=20.1.0
ascendhal_version=2.1.0
aicpu_version=1.0
tdt_version=1.0
log_version=1.0
prof_version=2.0
dvppkernels_version=1.0
tsfw_version=1.0
mmpa_version=1.0
required_firmware_firmware_version=1.0
```

7. 执行npu-smi info查看NPU工具安装是否成功。

**须注意npu-smi工具使用 /lib64，需要配置**
`ln -s /lib /lib64`

### 驱动卸载

按照驱动安装的顺序，用执行安装程序的用户，后安装的先卸载。卸载完成可以检查`/usr/local/Ascend/`，`/home/HwHiAiUser/Ascend/`目录对应目录是否卸载。

### 检查安装状态

* 配置NPU设备IP，以单机atlas01为例

  *当多台服务器进行分布式训练时，需要通过昇腾软件中的HCCN Tool工具配置NPU板卡IP地址（device的网卡IP），用于多台训练服务器间的网络模型参数通过NPU板卡上的光口进行传输同步，确保每台训练服务器训练时网络模型的参数能同步更新。 *

  * SMP（对称多处理器）模式：

  以root用户登录到AI Server(atlas服务器)配置每个device的网卡IP。配置要求：

  + AI Server中的第0/4，1/5，2/6，3/7号网卡需处于同一网段，第0/1/2/3号网卡在不同网段，第4/5/6/7号网卡在不同网段。
  + 对于集群场景，各AI Server对应的位置的device需处于同一网段，例如AI Server1和AI Server2的0号网卡需处于同一网段，AI Server1和AI Server2的1号网卡需处于同一网段。

  * 以下是第一台atlas服务器中NPU设备的IP配置

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

  * 如果集群中有第二台 atlas服务器，其NPU设备的IP配置如下（示例）

  ```bash
  hccn_tool -i 0 -ip -s address 192.168.10.21 netmask 255.255.255.0
  hccn_tool -i 1 -ip -s address 192.168.20.21 netmask 255.255.255.0
  hccn_tool -i 2 -ip -s address 192.168.30.21 netmask 255.255.255.0
  hccn_tool -i 3 -ip -s address 192.168.40.21 netmask 255.255.255.0
  hccn_tool -i 4 -ip -s address 192.168.10.22 netmask 255.255.255.0
  hccn_tool -i 5 -ip -s address 192.168.20.22 netmask 255.255.255.0
  hccn_tool -i 6 -ip -s address 192.168.30.22 netmask 255.255.255.0
  hccn_tool -i 7 -ip -s address 192.168.40.22 netmask 255.255.255.0

  # 第3,4,5,6... 类似配置
  ```

  + 查看配置成功的IP (配置文件`/etc/hccn.conf`)

  ```bash
  cat /etc/hccn.conf
  address_0=192.168.10.11
  netmask_0=255.255.255.0
  address_1=192.168.20.11
  netmask_1=255.255.255.0
  address_2=192.168.30.11
  netmask_2=255.255.255.0
  address_3=192.168.40.11
  netmask_3=255.255.255.0
  address_4=192.168.10.12
  netmask_4=255.255.255.0
  address_5=192.168.20.12
  netmask_5=255.255.255.0
  address_6=192.168.30.12
  netmask_6=255.255.255.0
  address_7=192.168.40.12
  netmask_7=255.255.255.0
  ```

  + 检查网口配置状态是否正确 (当IP配置成功，网口连接正常状态UP为正确，否则为DOWN)

    *需注意多台atlas设备的NPU网口需接入100G光纤交换机，且交换机需启用相应端口和流控 *

    `for i in {0..7}; do hccn_tool -i ${i} -link -g; done`
  + 获取ARP表项

    ```
    root@atlas02:~# hccn_tool -i 0 -arp -g
    arp table:
    (192.168.3.193) at 10:1b:54:92:ed:06 [ether]  on end2v1
    (192.168.40.11) at ac:8d:34:54:82:17 [ether]  on eth3
    (192.168.20.11) at ac:8d:34:54:82:19 [ether]  on eth1
    (192.168.1.11) at <incomplete>  on end0v3
    (192.168.4.194) at 10:1b:54:92:ed:05 [ether]  on end1v2
    (192.168.30.11) at ac:8d:34:54:82:18 [ether]  on eth2
    (192.168.1.111) at <incomplete>  on end0v3
    (192.168.1.1) at <incomplete>  on end0v3
    (192.168.2.192) at 10:1b:54:92:ed:07 [ether]  on end3v0
    (192.168.5.195) at 10:1b:54:92:ed:04 [ether]  on end0v3
    (192.168.10.11) at ac:8d:34:54:82:1a [ether]  on eth0
    ```
  + 获取路由表

    ```
    root@atlas02:~# hccn_tool -i 0 -route -g
    route table:
    Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
    127.0.0.1       *               255.255.255.255 UH    0      0        0 lo
    192.168.1.0     *               255.255.255.0   U     0      0        0 end0v3
    192.168.1.0     *               255.255.255.0   U     0      0        0 end1v2
    192.168.1.0     *               255.255.255.0   U     0      0        0 end2v1
    192.168.1.0     *               255.255.255.0   U     0      0        0 end3v0
    192.168.2.0     *               255.255.255.0   U     0      0        0 end3v0
    192.168.3.0     *               255.255.255.0   U     0      0        0 end2v1
    192.168.4.0     *               255.255.255.0   U     0      0        0 end1v2
    192.168.5.0     *               255.255.255.0   U     0      0        0 end0v3
    192.168.10.0    *               255.255.255.0   U     0      0        0 eth0
    192.168.20.0    *               255.255.255.0   U     0      0        0 eth1
    192.168.30.0    *               255.255.255.0   U     0      0        0 eth2
    192.168.40.0    *               255.255.255.0   U     0      0        0 eth3
    ```

### 升级固件工具包

- 若用户安装软件包时指定路径，执行`<package-path>/  *.run --upgrade --install-path=<path>`命令完成升级。

其中<package-path>为软件包所在目录，<path>为用户指定的软件包安装目录，  * 表示软件包名，请根据实际目录和包名进行替换。

以软件包所在目录为“/home/package”，软件包安装目录为“/home/work”为例，命令示例为：

`/home/package/  *.run --upgrade --install-path=/home/work`

- 若用户安装软件包时未指定路径，执行`<package-path>/  *.run --upgrade`命令对默认安装路径下的软件包进行升级，默认安装路径请见表1。

以软件包所在目录为`/home/package`为例，命令示例为：

`/home/package/  *.run --upgrade`

## 安装网卡驱动(可选)

- 获取安装包

  1. 登录华为企业业务网站。
  2. 在导航栏中选择“技术支持 > 智能管理软件 > iDriver > TaiShanServer iDriver”，进入目标服务器的详细页面的软件标签下，根据要求下载对应的版本。

  [《华为TM210灵活IO卡用户指南01.PDF》](../../images/config_images/华为TM210灵活IO卡用户指南03.pdf)
- 执行安装

  1. 进入下载目录
     `cd /root/driver`
  2. 进行驱动安装

     `dpkg -i NIC-hisi_eth-Ubuntu18.04.1-hns3-1.0.2-aarch64.deb`
  3. 查看驱动是否升级到驱动配套表中的指定版本

     `modinfo hns3`
- 升级驱动

  --runTM210暂不支持固件升级。  --run

---

## FAQ

1. 包安装时提示软件已经安装，或安装Fail

   * 解决方案

   软件包不支持重复安装，需要先卸载并重启后，再安装。

   ```
   ./A800-9000-NPU_Driver-20.0.RC1-ARM64-Ubuntu18.04.run  --uninstall 
   # 如果不确定具体安装情况，建议把所有的驱动固件，工具包都卸载
   # 重启服务器
   reboot
   # 重新执行安装
   ./A800-9000-NPU_Driver-20.0.RC1-ARM64-Ubuntu18.04.run   #如果之前失败的安装提示文件不存在或找不到，建议使用 
   ```

*说明：*

- 软件包默认安装路径：/usr/local/Ascend
- 安装详细日志路径：/var/log/ascend_seclog/ascend_install.log
- 安装后软件包的安装路径、安装命令以及运行用户信息记录路径：Driver/Firmware：/etc/ascend_install.info
- 使用run安装包后，不要手动设置环境变量export LD_LIBRARY_PATH指向之前rar包的旧SO文件，否则可能会出现run安装包内工具连接到之前版本的动态库。指向第三方库文件路径、非run安装包发布库文件路径的配置不受影响。
- 查看日志时需注意：日志时间采用的是系统时间，device侧时间与host侧时间保持同步，修改host侧时间可以使用date命令。例如：执行date -s 17:55:55命令，将系统时间设定为17点55分55秒。
- run文件安装可以用参数`--run`或者`-- install`，重新执行安装需要使用`-- upgrade`，安装过程中提示缺少组件可以使用`--full`
- 执行`npu-smi info`,提示`no such file`,原因是动态链接库路径没有配置，查看`/lib64`,目录是否存在，若不存在则执行`ln -s /lib /lib64`

2. atp brokern 处理

```
apt-get update && apt-get autoremove
apt-get install -y --fix-broken
# 如果是python相关包有问题，则执行，否则不用
# apt-get purge python* && apt-get autoclean && apt-get install python*
dpkg --configure -a
apt install  -y python3.6
```

若出现lsb_release 文件不存在执行以下命令：

`  apt-get install lsb-core`

3. NPU 驱动（也称CANN框架包）安装时报内核或系统版本不对，但检查没有问题，请注意修复以下依赖包

* CANN 驱动安装过程使用 DKMS 检查内核版本是否是指定的（例如： 4.15-0.99），如果没有安装dkms 可能会误报内核不一致的ERROR，
* 使用`lsb_release -a `检查系统版本是否是指定的（例如：Ubuntu Server 18.04.1 arm/amd64）, lsb_release 依赖系统python3.6的环境，如果在一键化安装过程中损坏了系统python环境，需要重新卸载重新安装python3.6

## 参考文档

> 《Ascend 910 驱动和开发环境安装指南.chm》
> 《Atlas Data Center Solution V100R020C00 快速部署指南（A800-9000）01.pdf》
> 《华为TM210灵活IO卡用户指南03.pdf》

<style>#mermaid-1611978901959{font-family:sans-serif;font-size:16px;fill:#333;}#mermaid-1611978901959 .error-icon{fill:#552222;}#mermaid-1611978901959 .error-text{fill:#552222;stroke:#552222;}#mermaid-1611978901959 .edge-thickness-normal{stroke-width:2px;}#mermaid-1611978901959 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-1611978901959 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-1611978901959 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-1611978901959 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-1611978901959 .marker{fill:#333333;}#mermaid-1611978901959 .marker.cross{stroke:#333333;}#mermaid-1611978901959 svg{font-family:sans-serif;font-size:16px;}#mermaid-1611978901959 .label{font-family:sans-serif;color:#333;}#mermaid-1611978901959 .label text{fill:#333;}#mermaid-1611978901959 .node rect,#mermaid-1611978901959 .node circle,#mermaid-1611978901959 .node ellipse,#mermaid-1611978901959 .node polygon,#mermaid-1611978901959 .node path{fill:#ECECFF;stroke:#9370DB;stroke-width:1px;}#mermaid-1611978901959 .node .label{text-align:center;}#mermaid-1611978901959 .node.clickable{cursor:pointer;}#mermaid-1611978901959 .arrowheadPath{fill:#333333;}#mermaid-1611978901959 .edgePath .path{stroke:#333333;stroke-width:1.5px;}#mermaid-1611978901959 .flowchart-link{stroke:#333333;fill:none;}#mermaid-1611978901959 .edgeLabel{background-color:#e8e8e8;text-align:center;}#mermaid-1611978901959 .edgeLabel rect{opacity:0.5;background-color:#e8e8e8;fill:#e8e8e8;}#mermaid-1611978901959 .cluster rect{fill:#ffffde;stroke:#aaaa33;stroke-width:1px;}#mermaid-1611978901959 .cluster text{fill:#333;}#mermaid-1611978901959 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:sans-serif;font-size:12px;background:hsl(80,100%,96.2745098039%);border:1px solid #aaaa33;border-radius:2px;pointer-events:none;z-index:100;}#mermaid-1611978901959:root{--mermaid-font-family:sans-serif;}#mermaid-1611978901959:root{--mermaid-alt-font-family:sans-serif;}#mermaid-1611978901959 flowchart{fill:apa;}</style>
