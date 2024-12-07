Linux bash sheel tips
================================


## 使用python socket.gethostname() 获取系统的hostname
Use socket and its gethostname() functionality. This will get the hostname of the computer where the Python interpreter is running:
```````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
import socket
print(socket.gethostname())
```````````````````````````
## bash 获取文件或重定向的第一行
````````````````````
$ head -n1 file
$ sed -n 1p file
$ awk 'NR == 1' file
````````````````````
## 注意文件系统编码，和特殊的格式要求

+ 在编码前，确认配置IDE（eclipse，操作系统的文本编码为 UTF-8，或GBK
+ Jenkins 环境变量或构建参数 赋值不能有空格

+ python 随机生成电话号码
`````````````````
random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8))
```````````````````````````````````````````````````````````````````````````````````````````````````````````

## 第一次使用SSH 连接 Centos 需要验证的密钥host-key
+ 参考链接：https://en.wikibooks.org/wiki/OpenSSH%2FCookbook%2FPublic_Key_Authentication
```````````````````````````````````````````````````````````````````````````````````
$ ssh -l fred server.example.org
The authenticity of host 'server.example.org (192.0.32.10)' can't be established.
ECDSA key fingerprint is SHA256:LPFiMYrrCYQVsVUPzjOHv+ZjyxCHlVYJMBVFerVCP7k.
Are you sure you want to continue connecting (yes/no)?
``````````````````````````````````````````````````````
默认使用base64 encoded SHA256， 可指定MD5编码
```````````````````````````````````
$ ssh -o FingerprintHash=md5 host.example.org
The authenticity of host 'host.example.org (192.0.32.203)' can't be established.
RSA key fingerprint is MD5:10:4a:ec:d2:f1:38:f7:ea:0a:a0:0f:17:57:ea:a6:16.
Are you sure you want to continue connecting (yes/no)?
``````````````````````````````````````````````````````
下载签名的host-key
`````````````
#例如：ssh-keyscan 172.19.6.177
$ ssh-keyscan host.example.org
# host.example.org SSH-2.0-OpenSSH_7.2
host.example.org ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBLC2PpBnFrbXh2YoK030Y5JdglqCWfozNiSMjsbWQt1QS09TcINqWK1aLOsNLByBE2WBymtLJEppiUVOFFPze+I=
# host.example.org SSH-2.0-OpenSSH_7.2
host.example.org ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC9iViojCZkcpdLju7/3+OaxKs/11TAU4SuvIPTvVYvQO32o4KOdw54fQmd8f4qUWU59EUks9VQNdqf1uT1LXZN+3zXU51mCwzMzIsJuEH0nXECtUrlpEOMlhqYh5UVkOvm0pqx1jbBV0QaTyDBOhvZsNmzp2o8ZKRSLCt9kMsEgzJmexM0Ho7v3/zHeHSD7elP7TKOJOATwqi4f6R5nNWaR6v/oNdGDtFYJnQfKUn2pdD30VtOKgUl2Wz9xDNMKrIkiM8Vsg8ly35WEuFQ1xLKjVlWSS6Frl5wLqmU1oIgowwWv+3kJS2/CRlopECy726oBgKzNoYfDOBAAbahSK8R
# host.example.org SSH-2.0-OpenSSH_7.2
host.example.org ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDDOmBOknpyJ61Qnaeq2s+pHOH6rdMn09iREz2A/yO2m
`````````````````````````````````````````````````````````````````````````````````````````````````

## Linux 中 iptables 的设置

1. 将iptables 配置保存在``/etc/sysconfig/iptables``

    ```
    service iptables save
    ````
2. 配置iptables文件，注意不能restart iptables，可以执行start 或 reload

    ```
    service iptables reload #或
    service iptables start  #如果在修改配置之前stop 了iptables

    ```
    恢复iptables 备份配置：
    复制`xtcAuto\doc\deployment\iptables.conf`即可得到最基本的配置，允许 docker,jenkins，saltstack,java,nginx 业务。

## python 将字符串列表或字典 转换未 列表或字典
`````````````````````````````
import ast
ast.literal_eval("{'x':1, 'y':2}")
=> {'y': 2, 'x': 1}
```````````````````
All the solutions based in eval() are dangerous, malicious code could be injected inside the string and get executed.

According to the documentation the expression gets evaluated safely. Also, according to the source code, literal_eval parses the string to a python AST (source tree), and returns only if it is a literal. The code is never executed, only parsed, so there is no reason for it to be a security risk.

Nmap 用法
------------------------------------------------------------------
    1. 扫描网段
    nmap -sP -PR 192.168.0.*

Npm Registry
------------------------------------------------------------------

淘宝可选，但是不可靠
If you're in China, maybe you should install it from our China mirror:
$ npm install cnpm -g --registry=https://registry.npm.taobao.org
