# MobileViT

This repo is to implement MobileViT using MindSpore.

# Finish

@2022/10/28

优化模型结构，提高了部分精度。

openi平台打通训练，但速度很慢。

@2022/10/21

GPU平台跑通训练。

@2022/10/13

mobilevit.py -> 能够跑通main测试函数，推理结果与pytorch结果一致。

# TO DO

- ~~对einops.rearrange方法进行功能代替。~~

- ~~进行数据处理工作并测试训练脚本。~~
- ~~改进MHSA部分代码。~~
- Ascend平台测试训练。
- 新模型代码进行静态图调试。
- 差异文档分析编写。