# MobileViT

This repo is to implement MobileViT using MindSpore.

# Finish

@2023/3/20

使用dynamiclossscale精度大幅提升，450epochs三个规格精度全部达到论文，并使用validate对checkpoint文件进行验证。

@2023/3/6

拉取新的mindcv仓库。

做了dynamiclossscale。

@2023/2/23

做了O0的优化，精度无提升。

@2023/1/13

调整权重初始化。

@2022/11/28

进行单元测试，与torch模型对比输出，一致。

@2022/11/1

调整权重初始化。

打通openi ascend八卡训练。

@2022/10/28

修改模型文件，优化模型结构，提高了部分精度。

openi平台打通训练，但速度很慢。

@2022/10/21

GPU平台跑通训练。

@2022/10/13

完成mobilevit模型文件的编写，能够跑通main测试函数。

# TO DO

- ~~对einops.rearrange方法进行功能代替。~~

- ~~进行数据处理工作并测试训练脚本。~~
- ~~改进MHSA部分代码。~~
- ~~Ascend平台测试训练。~~
- ~~新模型代码进行静态图调试。~~
- 运行PyTorch源码测试训练性能。
- 310推理脚本编写。
- 差异文档分析编写。