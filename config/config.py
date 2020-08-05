from easydict import EasyDict as edict
import numpy as np
import os

config = edict()
config.dataset = edict()
config.dataset.name = 'KITTI'
config.dataset.data_path = '/media/8TB/Research/Data/KITTI_raw'
config.dataset.num_workers = 8
config.dataset.train_data_file = 'data_splits/eigen_zhou_files.txt'
config.dataset.train_transform = edict()
config.dataset.train_transform.jittering = [0.2, 0.2, 0.2, 0.05]
config.dataset.train_batchsize = 8
config.dataset.val_transform = edict()
config.dataset.val_batchsize = 1

config.input = edict()
config.input.image_shape = [192, 640]
# for ResNet with BN
config.input.mean = [0.485, 0.456, 0.406]
config.input.std = [0.229, 0.224, 0.225]
config.input.format = 'RGB' 
# for ResNet with GN
config.input.mean = [103.530/255, 116.280/255, 123.675/255]
config.input.std = [1.0/255, 1.0/255, 1.0/255]
config.input.format = 'BGR' 

# Model
config.model = edict()
config.model.norm = 'GN'

