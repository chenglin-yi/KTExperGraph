# Copyright(c) 2024 YiChengLin
# 保留所有权利。   
# @Time    : 2024/7/29 10:55  
# @Author  : YiChengLin  
# @File    : KSEvolution.py  
# @Software: PyCharm
# 30个时刻的知识点状态演变热力图

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


plt.rcParams['font.family'] = 'serif'  # 设置英文为Times New Roman
plt.rcParams['font.serif'] = ['Times New Roman']
# 配置数学符号字体（确保下标等符号也使用新罗马）
plt.rcParams['mathtext.fontset'] = 'custom'  # 使用自定义数学字体
plt.rcParams['mathtext.rm'] = 'Times New Roman'  # 常规字体
plt.rcParams['mathtext.it'] = 'Times New Roman:italic'  # 斜体
plt.rcParams['mathtext.bf'] = 'Times New Roman:bold'  # 粗体
# plt.rcParams['font.sans-serif'] = ['SimSun']  # 显示中文

data = np.array([[0.1,     0.2,     0.3,     0.4,     0.5],
        [0.1,     0.2,     0.3,     0.4,     0.5],
        [0.1,     0.2,     0.3,     0.4,     0.5],
        [0.1,     0.2,     0.3,     0.4,     0.5],
        [0.1,     0.2,     0.3,     0.4,     0.5],
        [0.1,     0.2,     0.3,     0.4,     0.5],
        [0.1,     0.2,     0.3,     0.4,     0.5],
        [0.1,     0.2,     0.3,     0.4,     0.5],
        [0.1,     0.2,     0.3,     0.4,     0.5],
        [0.1,     0.2,     0.3,     0.4,     0.5],
        [0.1,     0.2,     0.3,     0.4,     0.5],
        [0.1,     0.2,     0.3,     0.4,     0.5],
        [0.1,     0.2,     0.3,     0.4,     0.5],
        [0.1,     0.2,     0.3,     0.4,     0.5],
        [0.1,     0.2,     0.3,     0.4,     0.5],
        [0.1,     0.2,     0.3,     0.4,     0.5],
        [0.1,     0.2,     0.3,     0.4,     0.5],
        [0.1,     0.2,     0.3,     0.4,     0.5],
        [0.1,     0.2,     0.3,     0.4,     0.5],
        [0.1,     0.2,     0.3,     0.4,     0.5],
        [0.1,     0.2,     0.3,     0.4,     0.5],
        [0.1,     0.2,     0.3,     0.4,     0.5],
        [0.1,     0.2,     0.3,     0.4,     0.5],
        [0.1,     0.2,     0.3,     0.4,     0.5],
        [0.1,     0.2,     0.3,     0.4,     0.5],
        [0.1,     0.2,     0.3,     0.4,     0.5],
        [0.1,     0.2,     0.3,     0.4,     0.5],
        [0.1,     0.2,     0.3,     0.4,     0.5],
        [0.1,     0.2,     0.3,     0.4,     0.5],
        [0.1,     0.2,     0.3,     0.4,     0.5]])

# 检查数据中是否包含非数值类型
if np.any(np.isnan(data)):
    print("数据中包含 NaN，需要处理")
    data = np.nan_to_num(data)  # 将 NaN 替换为 0

# 确保数据是浮点数类型
data = data.astype(float)
# 确保 annot 是数值数据
# annot_data = np.array(data, dtype=float)
data = data.T
annot_data = np.array(data, dtype=float)

labels = ['$c_1$', '$c_2$', '$c_3$', '$c_4$', '$c_5$']  # 假设有5个知识点

# 设置顶部和底部的标签信息
top_labels = ['\u221A', '\u00D7', '\u221A', '\u00D7', '\u00D7', '\u221A', '\u221A', '\u221A','\u221A', '\u221A', '\u221A', '\u221A',
              '\u00D7', '\u00D7', '\u00D7', '\u221A', '\u221A', '\u221A', '\u00D7', '\u00D7','\u221A', '\u221A', '\u221A', '\u00D7',
              '\u221A', '\u221A', '\u221A', '\u221A', '\u221A', '\u00D7']
bottom_labels = ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '2', '2', '2', '2', '2', '2', '2', '3', '4', '4',
                 '4', '4', '4', '4', '4', '4', '5', '5', '5']  # 底部标签

# 绘制热力图
fig, ax = plt.subplots(figsize=(18, 5))  # 调整画布大小以适应标签
sns.heatmap(annot_data, fmt=".4f", annot=True,  cmap='viridis_r', linewidths=0, ax=ax, vmax=1, vmin=0)
ax.set_yticklabels(labels, rotation=0, fontsize='20')
ax.set_xlabel('Knowledge State Evolution', labelpad=10, fontsize='20')

# 添加顶部标签
for i, label in enumerate(top_labels):
    ax.text(i + 0.5, -0.2, label, ha='center', va='center', fontsize=20, color='black')

# 添加底部标签
# for i, label in enumerate(bottom_labels):
#     ax.text(i + 0.5, data.shape[0] + 0.5, label, ha='center', va='center', fontsize=10, color='black')
for i, label in enumerate(bottom_labels):
    ax.text(i + 0.5, -0.6, label, ha='center', va='center', fontsize=20, color='black')
# 添加左侧标签说明
ax.text(-0.19, -0.2, '$a_t$', ha='right', va='center', fontsize=20, color='black')
ax.text(-0.19, -0.6, '$c_t$', ha='right', va='center', fontsize=20, color='black')

# 调整布局
plt.tight_layout()
plt.savefig("KS3.svg", format="svg", bbox_inches="tight")
plt.show()