# Copyright(c) 2025 YiChengLin
# 保留所有权利。
# @Time    : 2025/2/3 下午4:34
# @Author  : YiChengLin
# @File    : DOA
# @Software: PyCharm


import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.lines import Line2D
import numpy as np

plt.rcParams['font.family'] = 'serif'  # 设置英文为Times New Roman
plt.rcParams['font.serif'] = ['Times New Roman']

# 数据
datasets = ['ASSIST09', 'ASSIST15', 'Junyi']
models = ['1', '2', '3', '4', '5', '6', '7', '8']

# 每个模型的改进值
DOAs = {
    '1': [1, 2, 3],
    '2': [1, 2, 3],
    '3': [1, 2, 3],
    '4': [1, 2, 3],
    '5': [1, 2, 3],
    '6': [1, 2, 3],
    '7': [1, 2, 3],
    '8': [1, 2, 3]
}
# 创建图形
plt.figure(figsize=(10, 6))

# 颜色列表（为每个数据集分配颜色）
# colors = ['#DE7833', '#F2BB6B', '#C2ABC8', '#329845', '#AED185', '#276C9E', '#A3C9D5', '#912C2C']
#1f77b4（深蓝色）
#ff7f0e（橙色）
#2ca02c（绿色）
#1f77b4（深蓝色）
#17becf（青色）
#7f7f7f（灰色）
#1f77b4（深蓝色）
#ff7f0e（橙色）
#d62728（红色）
#ff7f0e（橙色）
#d62728（红色）
#bcbd22（黄色）
# colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
# colors = ['#1f77b4', '#ff7f0e', '#d62728']
colors = ['#1f77b4', '#17becf', '#7f7f7f']
# colors = ['#ff7f0e', '#d62728', '#bcbd22']
markers = ['o', 's', '^']  # 点标记：圆形、菱形，区分线条

# 绘制每条曲线
for i, dataset in enumerate(datasets):
    # 获取每个模型的DOA值
    y_values = [DOAs[model][i] for model in models]
    plt.plot(models, y_values, label=dataset, color=colors[i], marker=markers[i], linewidth=2,  markersize=8)
    # 在每个数据点上显示数值for j, (model, y) in enumerate(zip(models, y_values)):
    for j, (model, y) in enumerate(zip(models, y_values)):
        offset = 0.005 if y == 0.7245 or y == 0.7132 else 0.004  # 根据 y 值动态调整偏移量
        if y == 0.7912:
            offset = -0.002
        plt.text(j, y + offset, f'{y:.4f}', ha='center', va='top', fontsize=10, color=colors[i])

# 设置标题和标签
plt.xlabel('Models', fontsize=18)
plt.ylabel('DOA', fontsize=18)

# 自定义图例：显示两个连续相同的点标记
legend = plt.legend(fontsize=14, title_fontsize=14, frameon=True)
ax = plt.gca()
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.4f'))

# 调整布局
plt.tight_layout()

plt.savefig("DOA.svg", format="svg", bbox_inches="tight")
# 显示图形
plt.show()