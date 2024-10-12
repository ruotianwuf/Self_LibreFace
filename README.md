conda create -n libreface_env python=3.8

conda activate libreface_env

pip install --upgrade libreface

# CUDA 11.8 一定要下载！！！！
pip install torch==2.0.0 torchvision==0.15.1 torchaudio==2.0.1 --index-url https://download.pytorch.org/whl/cu118
