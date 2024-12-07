## Install python
sudo zypper update 
sudo zypper install python3
sudo rm /usr/bin/python
sudo ln -s /usr/bin/python3 /usr/bin/python
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py

sudo echo >> "export PATH=$PATH:$HOME/.local/bin"
source .bashrc
pip install -U pip
pip install -r docs/requirements.ini
sourcedir=$pwd/docs/zh_CN/
builddir=build
sphinx-build -b html $sourcedir $builddir

## Nginx static html
mkdir  $HOME/nginx/

sudo podman run --name docs-nginx -d -p 8000:8000  \
    -v $HOME/nginx/nginx.conf:/etc/nginx/nginx.conf  \
    -v /mnt/c/Users/lizhen/workspace/AiStudioDocs/build:/usr/share/nginx/html:ro -d nginx

## nginx.conf
worker_processes 1;
events {
worker_connections 1024;
}

http{
  include       mime.types;
  default_type  application/octet-stream;
  sendfile on;
  keepalive_timeout  65;
  server {
       listen 8000;
         location / {
           root /usr/share/nginx/html;
           index index.html index.htm;
           }
  }
}

## 让 Git 支持 utf-8 编码
sudo git config --global core.quotepath false  		    # 显示 status 编码
sudo git config --global gui.encoding utf-8			    # 图形界面编码
sudo git config --global i18n.commit.encoding utf-8	    # 提交信息编码
sudo git config --global i18n.logoutputencoding utf-8	# 输出 log 编码
export LESSCHARSET=utf-8                           # 对 less 命令进行 utf-8 编码
git config core.filemode false                          # git 忽略文件权限或用户归属变化
git config --global core.fileMode false 

## Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
