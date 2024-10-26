# GPU02 build horovod container


* connect and upload file

ssh -i  /mnt/c/Users/Admin/.ssh/yunxia-gpu01-id_rsa -p 50025 root@119.147.212.166

scp -i  /mnt/c/Users/Admin/.ssh/yunxia-gpu01-id_rsa -P 50025 /mnt/d/workspace/nni-1.9-py3-none-manylinux1_x86_64.whl root@119.147.212.166:/home/docker-build/

scp -i  /mnt/c/Users/Admin/.ssh/yunxia-gpu01-id_rsa -P 50025  /mnt/d/workspace/Diamond/dockerfiles/Dockerfile_horovod_basement.yaml root@119.147.212.166:/home/docker-build/


```offical mindspore docker python env

root@ed8ee1a9006a:/usr/bin# ll | grep python
lrwxrwxrwx 1 root root        23 Jul 17 12:50 pdb3.6 -> ../lib/python3.6/pdb.py*
lrwxrwxrwx 1 root root        23 Nov  7  2019 pdb3.7 -> ../lib/python3.7/pdb.py*
lrwxrwxrwx 1 root root        31 Oct 25  2018 py3versions -> ../share/python3/py3versions.py*
lrwxrwxrwx 1 root root        18 Sep  4 17:05 python -> /usr/bin/python3.7*
lrwxrwxrwx 1 root root         9 Oct 25  2018 python3 -> python3.6*
-rwxr-xr-x 2 root root   4526456 Jul 17 12:50 python3.6*
-rwxr-xr-x 2 root root   4526456 Jul 17 12:50 python3.6m*
-rwxr-xr-x 2 root root   4873376 Nov  7  2019 python3.7*
lrwxrwxrwx 1 root root        33 Nov  7  2019 python3.7-config -> x86_64-linux-gnu-python3.7-config*
-rwxr-xr-x 2 root root   4873376 Nov  7  2019 python3.7m*
lrwxrwxrwx 1 root root        34 Nov  7  2019 python3.7m-config -> x86_64-linux-gnu-python3.7m-config*
lrwxrwxrwx 1 root root        10 Oct 25  2018 python3m -> python3.6m*
lrwxrwxrwx 1 root root        34 Nov  7  2019 x86_64-linux-gnu-python3.7-config -> x86_64-linux-gnu-python3.7m-config*
-rwxr-xr-x 1 root root      3055 Nov  7  2019 x86_64-linux-gnu-python3.7m-config*
```

* sync docker

`docker tag harbor.sigsus.cn:8443/sz_gongdianju/apulistech/horovod-nni:0.20.0-tf2.3.0-torch1.6.0-mxnet1.6.0.post0-py3.7-cuda10.1 harbor.sigsus.cn:8443/sz_gongdianju/apulistech/horovod:0.20.0-tf2.3.0-torch1.6.0-mxnet1.6.0.post0-py3.7-cuda10.1-nni1.9
`

* horovod 分布式模型训练

```tensorflow
# 分布式
horovodrun  --network-interface ib0 -np 2 -hostfile /job/hostfile python /examples/tensorflow2_keras_mnist.py
horovodrun  --network-interface ib0 -np 16 -hostfile /job/hostfile python /examples/tensorflow2_keras_mnist.py
# 单机
horovodrun  -np 2 -H localhost:2 python /examples/tensorflow2_keras_mnist.py
```


```pytorch
horovodrun  --network-interface ib0 -np 16 -hostfile /job/hostfile python /examples/pytorch_mnist.py
# 单机
horovodrun  -np 2 -H localhost:2 python  python /examples/pytorch_mnist.py
```

```oppo 示例
bash /home/thomas/code/pytorch_imagenet2012/scripts/run_two_nodes.sh

 # 依赖 /home/thomas/code/pytorch_imagenet2012/imagenet/scripts/single_node_train.sh
```

```mindspore nature 多级多卡
cd /home/thomas/code/resnet_mindspore 
 bash ./run.sh

# 在master节点执行
cd /home/thomas/code/resnet_mindspore
ulimit -u unlimited 
rm -rf ./train_parallel 
mkdir ./train_parallel 
cp ./*.py ./train_parallel 
cp *.sh ./train_parallel 
cp -r ./src ./train_parallel 
cd ./train_parallel || exit mpirun --allow-run-as-root -v -n $(($DLWS_NUM_GPU_PER_WORKER*$DLWS_NUM_WORKER)) \ --output-filename log_output --hostfile /job/hostfile -mca btl_tcp_if_include ib0 --merge-stderr-to-stdout bash distribute_run.sh
```
GPU02环境上 测试账号密码修改了 thomas Apulis18c