import torch
import os
from mobilevit import mobile_vit_xx_small
# 通过PyTorch参数文件，打印PyTorch的参数文件里所有参数的参数名和shape，返回参数字典
def pytorch_params(pth_file):
    par_dict = torch.load(pth_file, map_location='cpu')
    pt_params = {}
    pt_filepath = 'pt.txt'
    if os.path.exists(pt_filepath):
        os.remove(pt_filepath)
    for name in par_dict:
        if 'num_batches_tracked' in name:
            continue
        parameter = par_dict[name]
        with open(pt_filepath, 'a') as file0:
            print(name, parameter.numpy().shape, file=file0)
        pt_params[name] = parameter.numpy()
    return pt_params

# 通过MindSpore的Cell，打印Cell里所有参数的参数名和shape，返回参数字典
def mindspore_params(network):
    ms_params = {}
    ms_filepath = 'ms.txt'
    if os.path.exists(ms_filepath):
        os.remove(ms_filepath)
    for param in network.get_parameters():
        name = param.name
        value = param.data.asnumpy()
        with open(ms_filepath, 'a') as file0:
            print(name, value.shape, file=file0)
        ms_params[name] = value
    return ms_params

if __name__ == '__main__':
    pth_path = "pth2ckpt\mobilevit_xxs.pt"
    pt_param = pytorch_params(pth_path)
    print("="*20)
    ms_param = mindspore_params(mobile_vit_xx_small(num_classes=1000))