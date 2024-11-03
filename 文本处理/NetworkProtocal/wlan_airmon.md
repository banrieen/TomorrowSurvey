赠品资料（189云盘主要是字典和视频，因为百度网盘存字典会过期，
才使用189云盘，可以网页在线下载，登录使用vx扫描登录就可以了）
https://cloud.189.cn/t/mmqUfqNZRZRn(访问码:84we)


使用kali
kali linux：下载：https://www.mzbky.com/kali-linux-download
VMware安装kali:https://www.mzbky.com/1758.html
连接网卡到虚拟机：https://www.mzbky.com/282.html
kali监听WiFi:https://www.mzbky.com/327.html

使用8812
https://url.ms/27fd8


配置wifi
-----------------------------------------------

1. lsusb

2. iwconfig <wlan0> 或者 ip addr 查看网口

3. 添加配置文件
vim /etc/wpa_supplicant/wpa_supplicant.conf
ctrl_interface=/var/run/wpa_supplicant
ctrl_interface_group=wheel
network={
        ssid="lxnh_2020-0926_5G"
        #psk="testtest"
        psk="zymq20191018"
        key_mgmt=WPA-PSK
        scan_ssid=1
}
* 查看网络接口

iwconfig

* 搜索wifi网络

iwlist wlan0 scan

* 将wifi接口UP接口

ip link set wlan0 up

* 设置接口关联的ssid

iwconfig wlan0 essid lxnh_2020-0926_5G

* 查看wifi的接口详情

iwconfig wlan0

4. 连接

wpa_supplicant -B -Dwext -iwlan0 -c/etc/wpa_supplicant/wpa_supplicant.conf -dddt

*dhcp获取地址：* dhclient wlan0
 
5. 查看连接状态

ip addr 

* 参考连接

https://en.opensuse.org/SDB:Tracking_down_wireless_problems

监听模式
-------------------------------------------------------------------------

1. 安装网卡驱动
zypper install rtl8812au
zypper install autoconf automake libtool pkg-config libnl3-devel libopenssl-1_1-devel zlib-devel libpcap-devel sqlite3-devel pcre-devel hwloc-devel libcmocka-devel hostapd wpa_supplicant tcpdump screen iw gcc-c++ gcc
zypper install aircrack-ng

ip link set wlan0 up

2. 设置为监听模式

iwconfig wlan0 mode monitor

3. 获取监听列表

airodump-ng wlan0

airmon-ng check kill

airmon-ng start wlan0

* 如果想要切换当前监听信道, 即可执行以下语句:

iwconfig wlan0 channel 11

iwlist wlan0 channel


再次执行以下命令即可查看当前信道

iwlist wlan0 channel

* 停止

airmon-ng stop wlan0

iwconfig wlan0 mode sta

**参考：**
安装：https://github.com/aircrack-ng/aircrack-ng
手册： https://aircrack-ng.org/doku.php?id=getting_started