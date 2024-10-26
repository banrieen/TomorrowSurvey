#!/bin/bash
echo -e "-------------------------------System Information----------------------------"
echo -e "Hostname:\t\t"`hostname`
echo -e "uptime:\t\t\t"`uptime | awk '{print $3,$4}' | sed 's/,//'`
echo -e "Manufacturer:\t\t"`cat /sys/class/dmi/id/chassis_vendor`
echo -e "Product Name:\t\t"`cat /sys/class/dmi/id/product_name`
echo -e "Version:\t\t"`cat /sys/class/dmi/id/product_version`
echo -e "Serial Number:\t\t"`cat /sys/class/dmi/id/product_serial`
echo -e "Machine Type:\t\t"`vserver=$(lscpu | grep Hypervisor | wc -l); if [ $vserver -gt 0 ]; then echo "VM"; else echo "Physical"; fi`
echo -e "Operating System:\t"`hostnamectl | grep "Operating System" | cut -d ' ' -f5-`
echo -e "Kernel:\t\t\t"`uname -r`
echo -e "Architecture:\t\t"`arch`
echo -e "Processor Name:\t\t"`awk -F':' '/^model name/ {print $2}' /proc/cpuinfo | uniq | sed -e 's/^[ \t]*//'`
echo -e "Active User:\t\t"`w | cut -d ' ' -f1 | grep -v USER | xargs -n1`
echo -e "System Main IP:\t\t"`hostname -I`
echo ""
echo -e "-------------------------------CPU/Memory Usage------------------------------"
locale | grep "zh_CN.UTF-8" 2>&1 > /dev/null
if [ $? -eq 0 ];then
        echo -e "Memory Usage:\t"`free | awk '/(Mem|内存)/{printf("%.2fG\t%.2f%%"), $2/1024/1024,$3/$2*100}'`
else
        echo -e "Memory Usage:\t"`free | awk '/Mem/{printf("%.2fG\t%.2f%%"), $2/1024/1024,$3/$2*100}'`
fi
# echo -e "Swap Usage:\t"`free | awk '/Swap/{printf("%.2f%%"), $3/$2*100}'`
echo -e "CPU Usage:\t"`cat /proc/stat | awk '/cpu/{printf("%.2f%%\n"), ($2+$4)*100/($2+$4+$5)}' |  awk '{print $0}' | head -1`
echo ""
echo -e "---------------------------------CPU Usage----------------------------------"
locale | grep "zh_CN.UTF-8" 2>&1 > /dev/null
if [ $? -eq 0 ];then
        lscpu | grep -E "(Thread\(s\)|Core\(s\)|Socket\(s\)|座|座的核数|核的线程数)"
else
        lscpu | grep -E "(Thread\(s\)|Core\(s\)|Socket\(s\))"
fi
echo ""
echo -e "---------------------------------Disk Usage----------------------------------"
#df -Ph | sed s/%//g | awk '{ if($5 > 80) print $0;}'
df -Ph | grep "^/dev/" | awk '{print$0}'
echo ""
echo -e "-----------------------------For Network Details-----------------------------"
for eth_dev in `ip -f inet addr | grep -E "[0-9]{1,2}:" | awk '{print$2}' | awk -F ':' '{print$1}'`
do
        ip_addr=`ip -f inet address show ${eth_dev} | grep inet | awk '{print$2}'`
        ip_speed=`ethtool ${eth_dev} | grep "Speed":`
        if [ $? -eq 0 ];then
                echo -e "${eth_dev}\t${ip_addr}${ip_speed}"
        fi
done
echo ""
echo -e "-----------------------------For LISTEN Details-----------------------------"
lsof -i:8443 2>&1 > /dev/null
if [ $? -eq 0 ];then
        echo -e "The port 8443 is been used"
fi
lsof -i:80 2>&1 > /dev/null
if [ $? -eq 0 ];then
        echo -e "The port 80 is been used"
fi
echo ""
echo -e "-------------------------------For GPU Details-------------------------------"
lshw -numeric -C display | grep -i "nvidia" > /dev/null
if [ $? -ne 0 ];then
        echo -e "There is no nvidia GPU"
else
        gpu_info=`nvidia-smi 2>&1`
        if [ $? -ne 0 ];then
                echo -e "There is no driver has been installed"
                gpu_code=`lshw -numeric -C display | grep -i "nvidia" | grep "product" | awk '{print$NF}'`
                if [ $? -eq 0 ];then
                        echo -e "The gpu code is ${gou_code}"
                fi
        else
                echo -e "${gpu_info}"
        fi
fi
echo ""
echo -e "-------------------------------For NPU Details-------------------------------"
lspci | grep -i huawei | grep -i "processing accelerators" > /dev/null
if [ $? -ne 0 ];then
        echo -e "There is no Huawei NPU"
else
        npu_info=`npu-smi info 2>&1`
        if [ $? -ne 0 ];then
                echo -e "There server has Huawei NPU but no driver has been installed"
        else
                i=0
                while [ ${i} -lt 7 ]
                do
                        npu-smi info -i ${i} -t board 2>&1 > /dev/null
                        if [ $? -ne 0 ];then
                                i=`expr $i + 1`
                        else
                                echo -e `npu-smi info -i ${i} -t board | grep "Software Version"`
                                hccn_tool -i ${i} -ip -g 2>&1 > /dev/null
                                if [ $? -ne 0 ];then
                                        echo -e "the ip of npu is not setup done"
                                else
                                        echo -e `hccn_tool -i ${i} -ip -g`
                                fi
                                i=7
                        fi
                done
                if [ $? -ne 0 ];then
                        echo -e "The NPU does not setup the ip address"
                fi
        fi
fi
echo ""
echo -e "----------------------------For Software Details----------------------------"
docker version -f {{.Server.Version}} > /dev/null 2>&1
if [ $? -eq 0 ];then
        echo -e "Docker Version:\t"`docker version -f {{.Server.Version}}`
else
        echo -e "Docker is not been installed"
fi
systemctl list-unit-files | grep kube > /dev/null
if [ $? -eq 0 ];then
        echo -e `kubelet --version`
else
        echo -e "Kubernetes is not been installed"
fi
python3 --version > /dev/null 2>&1
if [ $? -eq 0 ];then
        echo -e `python3 --version`
else
        echo -e "Python3 is not been installed"
fi
ansible --version >> /dev/null 2>&1
if [ $? -eq 0 ]; then
        echo -e `ansible --version | head -1`
else
        echo -e "Ansible is not been installed"
fi

if (( $(cat /etc/*-release | grep -w "Oracle|Red Hat|CentOS|Fedora" | wc -l) > 0 ));then
        echo -e "-------------------------------Package Updates-------------------------------"
        yum updateinfo summary | grep 'Security|Bugfix|Enhancement'
        echo -e "-----------------------------------------------------------------------------"
else
        echo -e "-------------------------------Package Updates-------------------------------"
        cat /var/lib/update-notifier/updates-available
        echo -e "-----------------------------------------------------------------------------"
fi

