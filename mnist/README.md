# MNIST手写数字识别

## 项目概述
本项目是一个用于识别MNIST手写数字的机器学习项目，通过使用C语言编写的神经网络来训练和测试模型，实现对手写数字的识别。

## 特别说明
本项目的部分代码取自王何宇老师在zju.git上分享的项目代码，他的url是https://git.zju.edu.cn/0098326/mathsoft.git
本项目在其基础上进行了部分修改，完成了主函数部分，并增加了分类报告，提供了更详细的信息并进行了可视化，包括每个类别的精确度、召回率、F1分数以及支持数（即每个类别的样本数），对模型最后的结果进行性能评估

## 功能特性
- **数据处理**：自动加载和处理MNIST数据集。
- **模型训练**：使用简单的神经网络进行模型训练。
- **性能评估**：评估模型在测试数据集上的准确率。
- **结果记录**：将训练过程中的损失和准确率记录到文本文件。
- **预测结果输出**：在训练结束后，输出最终的预测结果到文件。

## 环境依赖
- C编译器（如GCC）
- Python 3.x
- Python库：numpy, scikit-learn

## 文件结构
```
mnist.c                 # 主程序文件，包含神经网络的训练和测试逻辑。
neural_network.c        # 实现神经网络的基本功能。
mnist_file.c            # 处理MNIST数据文件的函数。
createBMP.c             # 用于创建和处理BMP图像的函数。
include/                # 包含所有必要的头文件。
data/                   # 存放MNIST数据集的目录（需自行下载）。
result.txt              # 存储训练过程中的损失和准确率。
final_predictions.txt   # 存储最终的预测结果。
draw_result.py          # Python脚本，用于绘制训练结果的图表。
```

## 安装指南
1. **下载项目**：
   ```
   git clone [项目URL]
   cd [项目目录]
   ```

2. **下载MNIST数据集**：
   - 下载MNIST数据文件到 `data/` 目录下。
   - 数据文件包括：`train-images-idx3-ubyte`, `train-labels-idx1-ubyte`, `t10k-images-idx3-ubyte`, `t10k-labels-idx1-ubyte`。

3. **编译项目**：
   ```
   make
   ```

## 使用方法
- 运行编译后的程序：
  ```
  ./mnist
  ```
- 绘制结果图表（确保Python及依赖库已安装）：
  ```
  python draw_result.py
  ```

## 贡献指南
如果你想为项目贡献代码，欢迎提交Pull Request或通过Issues提交功能请求和报告问题。

## 许可证
不知道，我看他们都写了，我也写一下

## 联系方式
- Email: [3230103664@zju.edu.cn]
- GitHub: [https://github.com/kkka1030]


