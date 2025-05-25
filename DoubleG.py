# Copyright(c) 2024 YiChengLin
# 保留所有权利。
# @Time    : 2024/7/29 10:55
# @Author  : YiChengLin
# @File    : DoubleG.py
# @Software: PyCharm
# 适用于双柱图对比

import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.family'] = 'serif'  # 设置英文为Times New Roman
plt.rcParams['font.serif'] = ['Times New Roman']

# 实验数据
models = ['DCKT-FRC', 'DCKT-ORC', 'DCKT-GRC', 'DCKT-ERC', 'DCKT-IRC']
means_kct = [1, 1, 1, 1, 1]
means_kmn = [2, 2, 2, 2, 2]

# 创建图形和子图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# 绘制左边的图
bar_width = 0.35
index = np.arange(len(models))
bars1 = ax1.bar(index, means_kct, bar_width, label='ACC', alpha=0.7, color='#1f77b4')
ax1.set_xlabel('Models', fontsize=12)
ax1.set_ylabel('Improvement on ACC(%)', fontsize=12)
ax1.set_xticks(index + bar_width/8)
ax1.set_xticklabels(models)
ax1.set_ylim(0.40)
# 设置图例
ax1.legend(fontsize=12, frameon=False)

# 在左边图的柱子上显示数值
for bar in bars1:
    height = bar.get_height()
    ax1.text(
        bar.get_x() + bar.get_width() / 2,  # x 位置：柱子中心
        height + 0.01,  # y 位置：柱子顶部上方
        f'{height:.2f}',  # 显示的数值，保留两位小数
        ha='center',  # 水平居中
        va='bottom',  # 垂直对齐到柱子顶部
        fontsize=10
    )

#1f77b4（深蓝色）
#ff7f0e（橙色）
# 绘制右边的图
bars2 = ax2.bar(index + bar_width, means_kmn, bar_width, label='AUC', alpha=0.7, color='#ff7f0e')
# ax2.bar(index + bar_width, means_kmn, bar_width, label='', alpha=0.7)
ax2.set_xlabel('Models', fontsize=12)
ax2.set_ylabel('Improvement on AUC(%)', fontsize=12)
# ax2.set_title('DCKT-FRC Performance')
ax2.set_xticks(index + bar_width)
ax2.set_xticklabels(models)  # 因为与左边的图共享x轴标签，所以这里不显示
ax2.set_ylim(0.70)

# 在右边图的柱子上显示数值
for bar in bars2:
    height = bar.get_height()
    ax2.text(
        bar.get_x() + bar.get_width() / 2,  # x 位置：柱子中心
        height + 0.01,  # y 位置：柱子顶部上方
        f'{height:.2f}',  # 显示的数值，保留两位小数
        ha='center',  # 水平居中
        va='bottom',  # 垂直对齐到柱子顶部
        fontsize=10
    )

# 设置图例
ax2.legend(fontsize=12, frameon=False)
# 显示图形
plt.tight_layout(w_pad=2)  # 控制间距
plt.savefig("Variant.svg", format="svg", bbox_inches="tight")

plt.show()