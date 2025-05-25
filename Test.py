# Copyright(c) 2024 YiChengLin
# 保留所有权利。   
# @Time    : 2024/7/30 11:40  
# @Author  : YiChengLin  
# @File    : Test.py  
# @Software: PyCharm
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# 数据和标签
data = np.random.rand(5, 30)
labels = ['c1', 'c2', 'c3', 'c4', 'c5']

# 创建图形和坐标轴
fig, ax = plt.subplots(figsize=(20, 5))

# 绘制热力图
sns.heatmap(data, annot=True, cmap='viridis_r', linewidths=.5, ax=ax, cbar=False)  # 禁用颜色条以更清晰地看到正方形

# 定义正方形的宽度和高度（相对于坐标轴的比例）
square_width = 0.02
square_height = 1 / len(data)  # 正方形的高度与热力图的一行相同

# 定义颜色列表（与行数相同数量的颜色）
colors = ['red', 'green', 'blue', 'purple', 'orange']

# 在热力图每行的最左侧放置一个正方形
# for i, color in enumerate(colors):
#     # 计算正方形的y位置（中心位置）
#     y_center = i / len(data) + square_height / 2
#
#     # 由于我们要将正方形放置在坐标轴的左侧，x位置需要是一个负数（相对于坐标轴的比例）
#     # 注意：这里的偏移量可能需要根据你的具体需求进行调整
#     x_offset = -0.01
#
#     # 创建一个Rectangle对象，并将其添加到坐标轴上
#     rect = Rectangle(xy=(x_offset, y_center - square_height / 2),  # 注意：y位置是中心减去高度的一半
#                      width=square_width, height=square_height,
#                      color=color, angle=0, transform=ax.transAxes)
#     ax.add_patch(rect)
for i, color in enumerate(colors):
    y_center = i / len(data) + square_height / 2 - square_height * 0.1  # 向下调整0.1的比例
    x_offset = -0.05 # 相对于坐标轴左侧的偏移量

    rect = Rectangle(xy=(x_offset, y_center - square_height / 2),
                     width=square_width, height=square_height,
                     color=color, angle=0, transform=ax.transAxes)
    ax.add_patch(rect)
# plt.subplots_adjust(left=0.2)  # 例如，增加左侧的边距
# 调整坐标轴的标签（如果需要）
# 注意：由于我们添加了正方形，y轴的标签可能会被遮挡
# 你可以通过调整y轴的标签位置或添加一些额外的空间来避免这个问题
# 例如：ax.set_yticks(np.arange(len(data)) + 0.5, labels=labels)  # 这可能不是必要的，取决于你的具体需求

# 显示图形
plt.show()