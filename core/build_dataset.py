from config.config import config
from core.build_transform import build_transform
from core.datasets import *
from torch.utils.data import DataLoader

def worker_init_fn(worker_id):                                                                                                                                     
    """Function to initialize workers"""
    time_seed = np.array(time.time(), dtype=np.int32)
    np.random.seed(time_seed + worker_id)


def build_dataset(phase):
    transform = build_transform(phase)
    data_path = config.dataset.data_path
    if phase == 'train':
        data_file = config.dataset.train_data_file
        with_context = True
        with_depth = False
        batch_size = config.dataset.train_batchsize
    elif phase == 'val':
        data_file = config.dataset.val_data_file
        with_context = False
        with_depth = True
        batch_size = config.dataset.val_batchsize

    dataset = eval(config.dataset.name)(data_path = data_path,
                                       data_file = data_file,
                                       data_transform = transform,
                                       with_context = with_context,
                                       with_depth = with_depth)
    dataset = DataLoader(dataset, 
                         batch_size = batch_size,
                         num_workers = config.dataset.num_workers,
                         shuffle = phase=='train'
                        )
    return dataset
