#!bin/bash

## bash tools 
# 查找并中断进程
TARGET=mindinsight
sudo ps -ef | grep ${TARGET} | grep -v grep | awk '{print $2}' | xargs kill -9

## 安装过程中使用旋转线来表示进度

#!/bin/bash

function KILLPROC(){
	echo $1 | xargs kill -9 &> /dev/null
}

function PROC_NAME(){
    printf "%-45s" ${1}
    tput sc
    while true
    do
        for ROATE in '-' "\\" '|' '/'
        do
            tput rc && tput ed
            printf "\033[1;36m%-s\033[0m" ${ROATE}
            sleep 0.5
        done
    done
}

function CHECK_STATUS(){
    if [ $? == 0 ];then
        KILLPROC ${1} &> /dev/null
        tput rc && tput ed
        printf "\033[1;36m%-7s\033[0m\n" 'SUCCESS'
    else
        KILLPROC ${1} &> /dev/null
        tput rc && tput ed
        printf "\033[1;31m%-7s\033[0m\n" 'FAILED'
    fi
}

function NGINX_INSTALL(){
    PROC_NAME Nginx_Service &
    PROC_PID=$!

    apt-get install nginx -y &> /dev/null
    CHECK_STATUS ${PROC_PID}
}

NGINX_INSTALL
