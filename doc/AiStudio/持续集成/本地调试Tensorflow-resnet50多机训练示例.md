1. 查看依赖安装

pip3.7 list
Package              Version
-------------------- ---------
absl-py              0.9.0
astor                0.8.1
attrs                19.3.0
certifi              2020.6.20
cffi                 1.12.3
chardet              3.0.4
Cython               0.29.21
decorator            4.4.2
gast                 0.2.2
google-pasta         0.2.0
grpcio               1.30.0
grpcio-tools         1.30.0
h5py                 2.8.0
hccl                 0.1.0
idna                 2.10
importlib-metadata   1.7.0
Keras-Applications   1.0.8
Keras-Preprocessing  1.1.2
Markdown             3.2.2
mpmath               1.1.0
npu-bridge           1.15.0
numpy                1.19.0
opt-einsum           3.2.1
pathlib2             2.3.5
pip                  19.2.3
pkgconfig            1.5.1
protobuf             3.12.2
psutil               5.7.0
pycparser            2.20
PyYAML               5.3.1
requests             2.24.0
scipy                1.5.1
setuptools           41.2.0
six                  1.15.0
sympy                1.4
te                   0.4.0
tensorboard          1.15.0
tensorflow           1.15.0
tensorflow-estimator 1.15.1
termcolor            1.1.0
topi                 0.4.0
urllib3              1.25.9
Werkzeug             1.0.1
wheel                0.34.2
wrapt                1.12.1
zipp                 3.1.0

pip3.7 install ./tfplugin/20.0.RC1/arm64-linux_gcc7.3.0/tfplugin/bin/npu_bridge-1.15.0-py3-none-any.whl
pip3.7 install ./nnae/20.0.RC1/arm64-linux_gcc7.3.0/fwkacllib/lib64/topi-0.4.0-py3-none-any.whl
pip3.7 install ./nnae/20.0.RC1/arm64-linux_gcc7.3.0/fwkacllib/lib64/te-0.4.0-py3-none-any.whl
pip3.7 install ./nnae/20.0.RC1/arm64-linux_gcc7.3.0/fwkacllib/lib64/hccl-0.1.0-py3-none-any.whl

pip3.7 install /dlwsdata/storage/Resnet50_HC/tensorflow-1.15.0-cp37-cp37m-linux_aarch64.whl

* 资源配置
    - 配置路径： /dlwsdata/storage/Resnet50_HC/hccl_8p.json
    - 资源卡（NPU）数： "device_count":"24",
    - 节点数： "instance_count":"3",
    - 节点名称与执行脚本保持一致："pod_name":"test1",
    - 节点通信内网IP:  "server_id":"192.168.100.33",
```json
{
    "status":"completed",
    "group_count":"1",
    "group_list":[
        {
            "group_name":"training",
            "device_count":"24",
            "instance_count":"3",
            "instance_list":[
                {
                    "pod_name":"test1",
                    "server_id":"192.168.100.33",
                    "devices":[
                        {
                            "device_id":"0",
                            "device_ip":"192.168.10.1"
                        },
                        {
                            "device_id":"1",
                            "device_ip":"192.168.20.1"
                        },
                        {
                            "device_id":"2",
                            "device_ip":"192.168.30.1"
                        },
                        {
                            "device_id":"3",
                            "device_ip":"192.168.40.1"
                        },
                        {
                            "device_id":"4",
                            "device_ip":"192.168.10.2"
                        },
                        {
                            "device_id":"5",
                            "device_ip":"192.168.20.2"
                        },
                        {
                            "device_id":"6",
                            "device_ip":"192.168.30.2"
                        },
                        {
                            "device_id":"7",
                            "device_ip":"192.168.40.2"
                        }
                    ]
                },
                {
                    "pod_name":"test2",
                    "server_id":"192.168.100.13",
                    "devices":[
                        {
                            "device_id":"0",
                            "device_ip":"192.168.10.5"
                        },
                        {
                            "device_id":"1",
                            "device_ip":"192.168.20.5"
                        },
                        {
                            "device_id":"2",
                            "device_ip":"192.168.30.5"
                        },
                        {
                            "device_id":"3",
                            "device_ip":"192.168.40.5"
                        },
                        {
                            "device_id":"4",
                            "device_ip":"192.168.10.6"
                        },
                        {
                            "device_id":"5",
                            "device_ip":"192.168.20.6"
                        },
                        {
                            "device_id":"6",
                            "device_ip":"192.168.30.6"
                        },
                        {
                            "device_id":"7",
                            "device_ip":"192.168.40.6"
                        }
                    ]
                },
                {
                    "pod_name":"test3",
                    "server_id":"192.168.100.23",
                    "devices":[
                        {
                            "device_id":"0",
                            "device_ip":"192.168.10.3"
                        },
                        {
                            "device_id":"1",
                            "device_ip":"192.168.20.3"
                        },
                        {
                            "device_id":"2",
                            "device_ip":"192.168.30.3"
                        },
                        {
                            "device_id":"3",
                            "device_ip":"192.168.40.3"
                        },
                        {
                            "device_id":"4",
                            "device_ip":"192.168.10.4"
                        },
                        {
                            "device_id":"5",
                            "device_ip":"192.168.20.4"
                        },
                        {
                            "device_id":"6",
                            "device_ip":"192.168.30.4"
                        },
                        {
                            "device_id":"7",
                            "device_ip":"192.168.40.4"
                        }
                    ]
                }
            ]
        }
    ]
}

```

* 执行脚本
    - 执行路径：/dlwsdata/storage/Resnet50_HC
    - 脚本名称：./run_24p_3.sh
    - 工具包路径： /usr/local/Ascend/ascend-toolkit/`20.0.RC1` 版本更新需注意修改
    - 资源配置文件（RANK_TABLE_FILE）：/dlwsdata/storage/Resnet50_HC/hccl_24p.json
    - RANK_ID=test3： hccl_24p.json配置中的pod名称"pod_name":"test1",
    - RANK_SIZE=24：多机资源的总体数量 
```bash

#unset POD_NAME
export POD_NAME=test3
rm -rf .ckpt*
export PYTHONPATH=/usr/local/Ascend/ascend-toolkit/20.0.RC1/arm64-linux_gcc7.3.0/opp/op_impl/built-in/ai_core/tbe:
export LD_LIBRARY_PATH=/usr/lib/aarch64-linux-gnu/hdf5/serial:/usr/local/Ascend/add-ons:/usr/local/Ascend/nnae/20.0.RC1/arm64-linux_gcc7.3.0/fwkacllib/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/lib:/usr/lib/
export TBE_IMPL_PATH=/usr/local/Ascend/ascend-toolkit/20.0.RC1/arm64-linux_gcc7.3.0/opp/op_impl/built-in/ai_core/tbe
export PATH=/usr/local/Ascend/ascend-toolkit/20.0.RC1/arm64-linux_gcc7.3.0/fwkacllib/ccec_compiler/bin/:/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
export ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/20.0.RC1/arm64-linux_gcc7.3.0/opp
#export DDK_VERSION_FLAG=1.60.T17.B830
export HCCL_CONNECT_TIMEOUT=200

# user env
#export JOB_ID={JOB_ID}
#export RANK_TABLE_FILE=./hccl_8p.json
export RANK_TABLE_FILE=/dlwsdata/storage/Resnet50_HC/hccl_24p.json
#export RANK_SIZE={RANK_SIZE}
export RANK_INDEX=0
#export RANK_ID={RANK_ID}

# profiling env
#export PROFILING_MODE={PROFILING_MODE}
#export AICPU_PROFILING_MODE={AICPU_PROFILING_MODE}
#export PROFILING_OPTIONS={PROFILING_OPTIONS}
#export FP_POINT={FP_POINT}
#export BP_POINT={BP_POINT}

export JOB_ID=10086
#export DEVICE_INDEX=0
export PRINT_MODEL=1
#export RANK_ID=0
#export RANK_ID=test
#export RANK_ID=0
export RANK_ID=test3
export RANK_SIZE=24

rm -rf *.pbtxt
ulimit -c 0

execpath=${PWD}

for devcice_phy_id in {0,1,2,3,4,5,6,7}
do
    export DEVICE_ID=$devcice_phy_id
    export DEVICE_INDEX=$devcice_phy_id
    mkdir -p $execpath/$(($devcice_phy_id + 16))
    cd $execpath/$devcice_phy_id
        python3.7 $execpath/code/resnet50_train/mains/res50.py --config_file=res50_32bs_16p  --max_train_steps=5000 --iterations_per_loop=100 --debug=True --eval=False --model_dir=/home/${DLWS_USER_NAME}/tensorboard/${DLWS_JOB_ID}/logs/ckpt$(($devcice_phy_id + 16)) > $execpath/$(($devcice_phy_id + 16)).log &
 done
~
```

* 模型配置
- 配置路径：/dlwsdata/storage/Resnet50_HC/code/resnet50_train/configs/res50_32bs_16p.py
- 数据集路径：'data_url': '/dlwsdata/storage/Resnet50_HC_data/data/resnet50/imagenet_TF'
```python
import tensorflow as tf

import os
log_dir = './resnet50_train/results/'+os.path.basename(__file__).split('.')[0]

#256
config = {
    # ============ for testing =====================
    'accelerator': '1980',    # 'gpu', '1980'
    'shuffle_enable': 'yes',
    'shuffle_buffer_size': 10000,
    'rank_size': 16,
    'shard': True,

    # ======= basic config ======= #
    'mode':'train',                                         # "train","evaluate","train_and_evaluate"
    'epochs_between_evals': 4,                              #used if mode is "train_and_evaluate"
    'stop_threshold': 80.0,                                 #used if mode is "train_and_evaluate"
    'data_dir':'/opt/npu/resnet_data_new',
    'data_url': '/dlwsdata/storage/Resnet50_HC_data/data/resnet50/imagenet_TF',
    'data_type': 'TFRECORD',
    'model_name': 'resnet50',
    'num_classes': 1001,
    'num_epochs': None,
    'height':224,
    'width':224,
    'dtype': tf.float32,
    'data_format': 'channels_last',
    'use_nesterov': True,
    'eval_interval': 1,
    'loss_scale': 1024,                                #could be float or string. If float, static loss scaling is applied.
                                                            #If string, the corresponding automatic loss scaling algorithm is used.
                                                            #Must be one of 'Backoff' of 'LogMax' (case insensitive).
    'use_lars': False,
    'label_smoothing':0.1,                                  #If greater than 0 then smooth the labels.
    'weight_decay': 0.0001,
    'batch_size':32,                                        #minibatch size per node, total batchsize = batch_size*hvd.size()*itersize

    'momentum': [0.9],

    #=======  data processing config =======
    'min_object_covered': 0.1,                              #used for random crop
    'aspect_ratio_range':[3. / 4., 4. / 3.],
    'area_range':[0.08, 1.0],
    'max_attempts': 100,

    #=======  data augment config =======
    'increased_aug': False,
    'brightness':0.3,
    'saturation': 0.6,
    'contrast': 0.6,
    'hue': 0.13,
    'num_preproc_threads': 22,

    #=======  initialization config =======
    'conv_init': tf.variance_scaling_initializer(),
    'bn_init_mode': 'adv_bn_init',                         # "conv_bn_init" or "adv_bn_init",initializer the gamma in bn in different modes
                                                            # "adv_bn_init" means initialize gamma to 0 in each residual block's last bn, and initialize other gamma to 1
                                                            # "conv_bn_init" means initialize all the gamma to a constant, defined by "bn_gamma_initial_value"
    'bn_gamma_initial_value': 1.0,

    #======== model architecture ==========
    'resnet_version': 'v1.5',
    'arch_type': 'original',                                   # ------ input -------
                                                            # C1,C2,C3: input block, stride in different layer
                                                            # ------ shortcut ------
                                                            # D1: average_pooling + conv1*1 in shortcut  in downsample block
                                                            # D2: conv3*3,stride=2 in shortcut in downsample block
                                                            # D3: conv1*1 +average_pooling in shortcut  in downsample block
                                                            # ------ mainstream ----
                                                            # E1: average_pooling + conv3*3 in mainstream in downsample block
                                                            # E2: conv3*3 + average_pooling in mainstream in downsample block

    #=======  logger config =======
    'display_every': 10,
    'log_name': 'resnet50.log',
    'log_dir': '/d_solution/ckpt0',

    #=======  Learning Rate Config =======
    'lr_warmup_mode': 'linear',                             # "linear" or "cosine"
    'warmup_lr': 0.0,
    'warmup_epochs': 5,
    'learning_rate_maximum': 0.2,

    'lr_decay_mode': 'cosine',                              # "steps", "poly", "poly_cycle", "cosine", "linear_cosine", "linear_twice", "constant" for 1980 only
    'learning_rate_end': 0.00001,

    'decay_steps': '10,20,30',                              #for "steps"
    'lr_decay_steps': '6.4,0.64,0.064',

    'ploy_power': 2.0,                                      #for "poly" and "poly_cycle"

    'cdr_first_decay_ratio': 0.33,                          #for "cosine_decay_restarts"
    'cdr_t_mul':2.0,
    'cdr_m_mul':0.1,

    'lc_periods':0.47,                                      #for "linear_consine"
    'lc_beta':0.00001,

    'lr_mid': 0.5,                                          #for "linear_twice"
    'epoch_mid': 80,

    'bn_lr_scale':1.0,

  }

def res50_config():
    config['global_batch_size'] = config['batch_size'] * config['rank_size']
    config['do_checkpoint'] = True

    return config
                                                
```

* 执行LOG
    - log路径： `tail -n 100 /var/log/npu/slog/device-0/device-0_20200803200804121.log`

```yaml
# hccl_8p.json
{
"group_count": "1",
"group_list": [
{
    "group_name": "worker",
    "device_count": "8",
    "instance_count": "1",
    "instance_list": [{"devices":[ 
    {"device_id":"0","device_ip":"192.168.10.3" },
    {"device_id":"1","device_ip":"192.168.20.3" },
    {"device_id":"2","device_ip":"192.168.30.3" },
    {"device_id":"3","device_ip":"192.168.40.3" },
    {"device_id":"4","device_ip":"192.168.10.4" },
    {"device_id":"5","device_ip":"192.168.20.4" },
    {"device_id":"6","device_ip":"192.168.30.4" },
    {"device_id":"7","device_ip":"192.168.40.4" } ],
    "pod_name":"another","server_id":"127.0.0.1"}]
}
],
"status": "completed"
}
```

```bash

docker run -it -v /root/sample_tf:/data/ 
--device=/dev/davinci0 
--device=/dev/davinci1 
--device=/dev/davinci2 
--device=/dev/davinci3 
--device=/dev/davinci4 
--device=/dev/davinci5 
--device=/dev/davinci6 
--device=/dev/davinci7 
--device=/dev/davinci_manager 
--device=/dev/devmm_svm 
-v /var/log/npu/conf/slog/slog.conf:/var/log/npu/conf/slog/slog.conf 
-v /var/log/npu/slog/container/7:/var/log/npu/slog 
-v /var/log/npu/profiling/container/7:/var/log/npu/profiling 
-v /var/log/npu/dump/container/7:/var/log/npu/dump 
-v /var/log/npu/docker_slog_7:/usr/slog 
--device=/dev/hisi_hdc 
-w /data/Resnet50_HC tf:1.15-0728 bash
```
