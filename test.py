from tensorflow.python.client import device_lib
import torch

print(device_lib.list_local_devices(), torch.cuda.is_available())
