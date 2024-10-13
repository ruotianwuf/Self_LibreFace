import torch
import tensorflow as tf
print(torch.__version__)
print(torch.cuda.is_available())  # 应返回True
print(torch.cuda.device_count())  # 应返回大于0的数字
print(torch.cuda.get_device_name(0))  # 应显示GPU的名称
print(torch.cuda.device_count())  # 输出系统中可用的GPU数量
import os

def get_mkl_enabled_flag():
    mkl_enabled = False
    major_version = int(tf.__version__.split(".")[0])
    minor_version = int(tf.__version__.split(".")[1])
    if major_version >= 2:
        if minor_version < 5:
            from tensorflow.python import _pywrap_util_port
        elif minor_version >= 9:
            from tensorflow.python.util import _pywrap_util_port
            onednn_enabled = int(os.environ.get('TF_ENABLE_ONEDNN_OPTS', '1'))
        else:
            from tensorflow.python.util import _pywrap_util_port
            onednn_enabled = int(os.environ.get('TF_ENABLE_ONEDNN_OPTS', '0'))
        mkl_enabled = _pywrap_util_port.IsMklEnabled() or (onednn_enabled == 1)
    else:
        mkl_enabled = tf.pywrap_tensorflow.IsMklEnabled()
    return mkl_enabled

print("We are using Tensorflow version", tf.__version__)
print("MKL enabled :", get_mkl_enabled_flag())





