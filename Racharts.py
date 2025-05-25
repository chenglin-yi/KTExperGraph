# Copyright(c) 2024 YiChengLin
# 保留所有权利。   
# @Time    : 2024/7/30 21:31  
# @Author  : YiChengLin  
# @File    : Racharts.py  
# @Software: PyCharm
# import numpy as np
# import matplotlib.pyplot as plt
# plt.rcParams['font.sans-serif'] = ['SimSun']  # 显示中文
# # 定义雷达图的各个维度（即雷达图的各个“角”）
# # 定义雷达图的各个维度（五个维度）
# labels = np.array(['维度1', '维度2', '维度3', '维度4', '维度5'])
# #
# # 第一组数据
# stats1 = np.array([20, 34, 30, 35, 27])
# # 第二组数据
# stats2 = np.array([25, 30, 35, 40, 32])
#
# # 数据总数（维度数量）
# N = len(labels)
#
# # 角度（五个等分点）
# angles = np.linspace(0, 2 * np.pi, N, endpoint=False)
#
# # 绘制雷达图
# fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(polar=True))
# ax.plot(angles, stats1, color='blue', linewidth=2, label='组1')
# ax.plot(angles, stats2, color='red', linewidth=2, label='组2')
# # 填充区域（如果需要的话）
# # 注意：这里不需要闭合点，因为 fill 会自动闭合
# # ax.fill(np.append(angles, angles[0]), np.append(stats1, stats1[0]), color='blue', alpha=0.25, label='组1填充')
# # ax.fill(np.append(angles, angles[0]), np.append(stats2, stats2[0]), color='red', alpha=0.25, label='组2填充')
#
# # 设置雷达图的标签
# ax.set_thetagrids(np.degrees(angles), labels)
#
# # 设置图例
# ax.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
#
# # 设置标题
# plt.title("两组数据的五边形雷达图示例")
# # 显示图形
# plt.show()

# labels = np.array(['C1', 'c2', 'c3', 'c4', 'c5'])
#
# # 第一组数据
# stats1 = np.array([20, 34, 30, 35, 40])
# # 第二组数据
# stats2 = np.array([30, 35, 40, 32, 45])
#
# # 数据总数
# N = len(labels)
#
# # 角度
# angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
#
# # 闭合雷达图
# stats1 = np.concatenate((stats1, [stats1[0]]))
# stats2 = np.concatenate((stats2, [stats2[0]]))
# angles += angles[:1]
#
# # 绘制雷达图
# fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
# # ax.fill(angles, stats1, color='blue', alpha=0.25, label='组1')
# ax.plot(angles, stats1, color='blue', linewidth=2)
# # ax.fill(angles, stats2, color='red', alpha=0.25, label='组2')
# ax.plot(angles, stats2, color='red', linewidth=2)
#
# # 设置雷达图的标签（不包括闭合点）
# ax.set_thetagrids(np.degrees(angles[:-1]), labels)
#
# # 添加图例
# ax.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
# # ax.set_thetagrids(np.degrees(angles), labels)
#
# # 设置标题
# plt.title("两组数据的雷达图示例")
#
# # 显示图形
# plt.show()
# 但实际上，对于绘图，我们不需要闭合点
# angles = angles[:-1]

# 绘制雷达图
# fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
# ax.plot(angles, stats1, color='blue', linewidth=2, label='组1')
# ax.plot(angles, stats2, color='red', linewidth=2, label='组2')

# 填充区域（如果需要的话，但通常线条图不填充）
# ax.fill(angles, stats1, color='blue', alpha=0.25)
# ax.fill(angles, stats2, color='red', alpha=0.25)

# 设置雷达图的标签
# ax.set_thetagrids(np.degrees(angles), labels)

# 尝试设置图例的线条长度（但效果可能有限）
# 注意：matplotlib的图例默认是为点设计的，对于线条图例可能需要额外自定义
# legend = ax.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
# for line in legend.get_lines():
#     line.set_linewidth(4)  # 增加线条宽度以模拟更长的线条
#
# # 设置标题
# plt.title("两组数据的五边形雷达图示例（线条式）")
#
# # 显示图形
# plt.show()


# 数据
# labels = np.array(['维度1', '维度2', '维度3', '维度4', '维度5'])
# stats = np.array([20, 34, 30, 35, 27])
# stats = stats / np.max(stats) * 1.0  # 归一化数据以便更好地可视化
#
# # 角度（五个等分点）
# angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
#
# # 绘制雷达图
# fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
# ax.plot(angles, stats, color='blue', linewidth=2, linestyle='-')
# ax.fill(np.append(angles, angles[0]), np.append(stats, stats[0]), color='blue', alpha=0.25)
#
# # 绘制正五边形的边框
# # 首先，计算正五边形的顶点角度（从水平方向开始）
# # 正五边形每个内角为108度，外角为360/5=72度
# # 因此，顶点角度为0, 72, 144, 216, 288（或-72，与0等价）
# polygon_angles = np.deg2rad([0, 72, 144, 216, 288])
# # 假设五边形的半径为1（你可以根据需要调整它）
# polygon_radii = np.ones(len(polygon_angles))
#
# # 绘制五边形的边框
# ax.plot(polygon_angles, polygon_radii, 'r--')  # 使用红色虚线绘制边框
#
# # 为了使五边形看起来更完整，我们可以在每个顶点之间绘制线段
# # 但由于极坐标图的特性，直接这样做可能会有些复杂
# # 一种更简单的方法是绘制从中心到每个顶点的线段，但这在视觉上可能不够完美
# # 或者，你可以考虑在外部使用另一个绘图库（如PIL或OpenCV）来绘制完整的五边形，并将其作为图像叠加到Matplotlib图表上
#
# # 设置雷达图的标签
# ax.set_thetagrids(np.degrees(angles), labels)
#
# # 显示图形
# plt.show()

# 注意：上面的代码实际上并没有绘制一个完美的闭合五边形边框，
# 因为极坐标图的特性使得直接在轴上绘制这样的形状变得复杂。
# 一种可能的解决方案是在图表上叠加一个预先绘制的五边形图像。
import numpy as np
import matplotlib.pyplot as plt

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimSun']

# 定义雷达图的各个维度
labels = np.array(['维度1', '维度2', '维度3', '维度4', '维度5'])

# 数据
stats1 = np.array([20, 34, 30, 35, 27])
stats2 = np.array([25, 30, 35, 40, 32])

# 角度
N = len(labels)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()  # 转换为列表以添加第一个角度
angles += angles[:1]  # 显式地添加第一个角度作为最后一个角度以模拟闭合（但实际上不是必需的）

# 但请注意，对于绘图来说，我们实际上不需要这样做，因为plot会自动闭合

# 绘制雷达图
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.plot(angles[:-1], stats1, color='blue', linewidth=2, label='组1')  # 注意这里我们没有添加stats1的最后一个点
ax.plot(angles[:-1], stats2, color='red', linewidth=2, label='组2')  # 同样，也没有添加stats2的最后一个点

# 设置雷达图的标签（注意：我们不需要为闭合的“点”设置标签）
ax.set_thetagrids(np.degrees(angles[:-1]), labels)  # 同样，只设置到最后一个有效角度之前的标签

# 设置图例
ax.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

# 设置标题
plt.title("两组数据的雷达图示例")

# 显示图形
plt.show()
