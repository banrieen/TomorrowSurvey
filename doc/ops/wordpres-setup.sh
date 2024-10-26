

# Add user to particular group
USERNAME=$(whoami)
# sudo usermod -a -G sudo $USERNAME
sudo usermod -a -G root $USERNAME
sudo usermod -a -G docker $USERNAME
# Add to sudoers without passwd
sudo echo '$USERNAME  ALL=(ALL)  NOPASSWD: ALL' >> /etc/sudoers
sudo echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# Run Wordpress
## Refer: https://hub.docker.com/_/wordpress/
Wordpress_DIR=$HOME/wordpress
mkdir -p $Wordpress_DIR
## Load tutorial by Sphinx
Turoial=/mnt/c/Users/lizhen/workspace/AiStudioDocs/build/html
sudo podman run --name local-wordpress02 -v $Turoial:/var/www/html/tutorial -v $Wordpress_DIR:/var/www/html -p 8080:80 -d wordpress
sudo podman run --name local-wordpress -v $Wordpress_DIR:/var/www/html -p 8080:80 -d wordpress
# sudo podman run --name local-wordpress -e WORDPRESS_DEBUG=1 -v $Wordpress_DIR:/var/www/html -p 8080:80 -d wordpress

# Run DB Mysql
Mysql_DIR=$HOME/mysql/data
Mysql_Conf=$HOME/mysql/conf.d
mkdir -p $Mysql_DIR
mkdir -p $Mysql_Conf
ROOT_PASSWORD=mysql
sudo podman run -v $Mysql_DIR:/var/lib/mysql -v $Mysql_Conf:/etc/mysql/conf.d -p 3306:3306 --user 1000:1000 --name local-mysql -e MYSQL_ROOT_PASSWORD=$ROOT_PASSWORD -d mysql:latest

## Create database for wordpress
Container_Name=mysql
CONTAIER_ID=`sudo podman ps | grep $Container_Name | awk  '{print $1;}'`
sudo podman exec -it $CONTAIER_ID bash
mysql -uroot -p$ROOT_PASSWORD
Database_Name=wordpress
CREATE DATABASE $Database_Name DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
show databases;

## Create the ueser
CREATE USER 'wordpress_admin'@'%' identified with mysql_native_password by 'press_2025';
# delete from mysql.user where user='wordpress_admin';
GRANT ALL PRIVILEGES  ON wordpress.*  TO 'wordpress_admin'@'%';
FLUSH PRIVILEGES;

# phpadmin
sudo podman run --name myadmin -d -e PMA_HOST=localhost  -p 8082:80 phpmyadmin/phpmyadmin

sudo podman start local-wordpress local-mysql local-postgres
## Reload wordpress in WSL container
Mysql_NewPort=3306
Mysql_conf=wordpress/wp-config.php
Mysql_ContainerID=`sudo podman ps -a |grep mysql | awk '{print $1}'`
Postgres_ContainerID=`sudo podman ps -a |grep postgres | awk '{print $1}'`
Wordpress_ContainerID=`sudo podman ps -a |grep wordpress | awk '{print $1}'`
Mysql_NewIP=`sudo podman inspect $Mysql_ContainerID | grep IPAddress |awk 'NR==2 {print $2}'|tr -d '",'`
Wordpress_OldIP=`cat $Mysql_conf | grep WORDPRESS_DB_HOST | awk '{print $4}' | tr -d "')"`
sudo sed -i "s/'WORDPRESS_DB_HOST', '$Wordpress_OldIP'/'WORDPRESS_DB_HOST', '$Mysql_NewIP:$Mysql_NewPort'/g" $Mysql_conf
sudo podman start $Wordpress_ContainerID

## 教程页面链接ReadTheDoc
<div class="tab-pane fade in active" id="depart">
    <iframe src="https://apulis-ai-platform-doc.readthedocs.io/zh_CN/latest/" frameborder="0" width="1920px" height="1080px"></iframe>
</div>

# Run DB postgress
## Refer: https://mehmetozanguven.github.io/container/2021/12/15/running-postgresql-with-podman.html
## Secrets
Postgres_PASSWD=postgres
postgres_DIR=$HOME/postgres
mkdir -p $postgres_DIR
sudo podman run -dt --name local-postgres -e POSTGRES_PASSWORD=$Postgres_PASSWD -v "$postgres_DIR:/var/lib/postgresql/data:Z" -p 5432:5432 postgres
podman exec -it my-postgres bash
psql -U postgres

# FAQ
## podman ， k8s 不同pod container之间网络访问。

"""
haiyuan.bian@apulis.com
/data/tutorial/index.html
https://apulis-ai-platform-doc.readthedocs.io/zh_CN/latest/

<div class="tab-pane fade in active" id="depart">
    <IFRAME SRC="https://apulis-ai-platform-doc.readthedocs.io/zh_CN/latest/" frameborder="0"  width="1920px" height="1080px"></IFRAME>
</div>

"""
## 代理 traefik （不支持静态html）

mkdir traefik
curl https://raw.githubusercontent.com/traefik/traefik/v2.7/traefik.sample.toml -o $HOME/traefik/traefik.yml

sudo podman run -d -p 8000:8000 -p 80:80 \
    -v /mnt/c/Users/lizhen/workspace/AiStudioDocs/build:/www/html/sphinx  \
    -v $HOME/traefik/traefik.yml:/etc/traefik/traefik.yml traefik:v2.7

