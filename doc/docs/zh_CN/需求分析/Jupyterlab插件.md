# Jupyterlab 开发插件

* JupyterLab 预置插件建议为： 
    + 代码补全： jupyterlab-kite 
    + 代码调试： debugger
    + 数据可视化：jupyterlab-plotly/keplergl-jupyter
    + （可选）查看环境变量：jupyterlab-variableInspector
    
* 参考链接： 
    + 插件功能描述： https://www.huaweicloud.com/articles/0e551ae1d0b1a09e20fdb3ee02d2e2c8.html
    + 插件安装：     https://github.com/ml-tooling/ml-workspace/blob/main/Dockerfile           

## 安装代码补全工具Jupyter-kite

```bash
# Base env: Ubuntu 18.04

# 卸载node
sudo apt-get purge --auto-remove -y nodejs
sudo apt-get purge nodejs
sudo apt-get autoremove
sudo rm /usr/local/bin/node
sudo apt -y install curl dirmngr apt-transport-https lsb-release ca-certificates
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
sudo apt update 
sudo apt install -y nodejs
sudo node --version
# Install jupyter-kite  by terminal
sudo mkdir -p /home/admin/.local/share/kite
sudo chmod 777 -R /home/admin/.local/share/kite
printf "\n\n" | bash -c "$(wget -q -O - https://linux.kite.com/dls/linux/current)" 
# Install jupyterlab-kite
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo chmod +x get-pip.py
sudo python3 get-pip.py --force-reinstall
sudo python3 -m pip install "jupyterlab-kite>=2.0.2" 
# python3 -m pip uninstall "jupyterlab-kite>=2.0.2"
```
# Install dependance

kite_installer.sh | sh  -s -- -y 

sudo pip3 install jedi==0.17.2 

# Restart jupyter
nohup /usr/bin/python3 /usr/local/bin/jupyter-lab --no-browser --ip=0.0.0.0 --notebook-dir=/ --NotebookApp.token= --port=49766 --NotebookApp.base_url=/endpoints/eyJwb3J0IjoiTXpJM01UQT0iLCJ1c2VyTmFtZSI6ImFkbWluIn0=/ --NotebookApp.allow_origin=* &

# Plugin List
debugger jupyter-matplotlib jupyterlab-drawio jupyterlab-plotly jupyterlab-spreadsheet jupyterlab-system-monitor keplergl-jupyter jupyterlab-variableInspector geojson-extension