# Copyright(c) 2024 YiChengLin
# 保留所有权利。
# @Time    : 2024/7/29 17:21
# @Author  : YiChengLin
# @File    : linechart
# @Software: PyCharm


# import matplotlib.pyplot as plt
# import matplotlib.ticker as ticker
#
# plt.rcParams['font.family'] = 'serif'  # 设置英文为Times New Roman
# plt.rcParams['font.serif'] = ['Times New Roman']
# # 横轴数据
# x = [1, 2, 3, 4, 5, 6]
#
# # 纵轴数据
# y2 = [0.7740, 0.7803, 0.7919, 0.7763, 0.7734, 0.7702]
# y1 = [0.7751, 0.7819, 0.7806, 0.7800, 0.7772, 0.7721]
#
# # 创建图形和子图
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
# # 调整子图之间的间隔
# # plt.subplots_adjust(wspace=0.5)  # 增加水平间距，默认值为 0.2
#
# # 绘制第一张图：ACC
# ax1.plot(x, y1, label='ACC', color='#1f77b4', marker='o')
# # ax1.set_title('ACC Curve')
# ax1.set_xlabel('L',  fontsize=16)
# ax1.set_ylabel('ACC', fontsize=16)
# ax1.legend(fontsize=12)
# # ax = plt.gca()
# # ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.4f'))
# ax1.grid(True, linestyle='--', linewidth=1.5, alpha=0.2)  # 添加网格线
# # ax1.grid(True)
# # ax1.legend(frameon=False)  # 去掉图例外边框
# # 新增：设置ACC子图纵坐标格式
# ax1.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.4f'))
#
# # ax1.ticklabel_format(axis='y', style='plain')  # 禁用科学计数法（可选）
#
#
# # 绘制第二张图：AUC
# ax2.plot(x, y2, label='AUC', color='#ff7f0e', marker='s', linestyle='--')
# # ax2.set_title('AUC Curve')
# ax2.set_xlabel('L',  fontsize=16)
# ax2.set_ylabel('AUC',  fontsize=16)
# ax2.legend(fontsize=12)
#
# ax2.grid(True, linestyle='--', linewidth=1.5, alpha=0.2)  # 添加网格线
# # ax2.grid(True)
# # ax2.legend(frameon=False)  # 去掉图例外边框
# # 新增：设置ACC子图纵坐标格式
# ax2.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.4f'))
# # ax2.ticklabel_format(axis='y', style='plain')  # 禁用科学计数法（可选）
# # 调整布局
# plt.tight_layout()
#
# # 手动调整子图之间的间隔
# plt.subplots_adjust(wspace=0.2)  # 增加水平间距
# plt.savefig("L1.svg", format="svg", bbox_inches="tight")
# # 显示图形
# plt.show()


import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

plt.rcParams['font.family'] = 'serif'  # 设置英文为Times New Roman
plt.rcParams['font.serif'] = ['Times New Roman']
# 横轴数据
x = [0.00, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30]

# 纵轴数据
y2 = [1, 1, 1, 1, 1, 1, 1]
y1 = [2, 2, 2, 2, 2, 2, 2]

# 创建图形和子图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# 绘制第一张图：ACC
ax1.plot(x, y1, label='ACC', color='#1f77b4', marker='o')
# ax1.set_title('ACC Curve')
ax1.set_xlabel('Threshold',  fontsize=16)
ax1.set_ylabel('ACC', fontsize=16)
ax1.legend(fontsize=12)
# ax1.grid(True)
ax1.grid(True, linestyle='--', linewidth=1.5, alpha=0.2)  # 添加网格线
# ax1.legend(frameon=False)  # 去掉图例外边框
ax1.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.4f'))


# 绘制第二张图：AUC
ax2.plot(x, y2, label='AUC', color='#ff7f0e', marker='s', linestyle='--')
# ax2.set_title('AUC Curve')
ax2.set_xlabel('Threshold',  fontsize=16)
ax2.set_ylabel('AUC',  fontsize=16)
ax2.legend(fontsize=12)
# ax2.grid(True)
ax2.grid(True, linestyle='--', linewidth=1.5, alpha=0.2)  # 添加网格线
# ax2.legend(frameon=False)  # 去掉图例外边框
ax2.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.4f'))
plt.tight_layout()

# 手动调整子图之间的间隔
plt.subplots_adjust(wspace=0.2)  # 增加水平间距
# 显示图形
plt.savefig("Threshold.svg", format="svg", bbox_inches="tight")
plt.show()
