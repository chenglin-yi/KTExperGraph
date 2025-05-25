# Copyright(c) 2024 YiChengLin
# 保留所有权利。
# @Time    : 2024/7/29 10:55
# @Author  : YiChengLin
# @File    : Acc.py
# @Software: PyCharm
# ACC对比图

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker  # 新增导入

plt.rcParams['font.family'] = 'serif'  # 设置英文为Times New Roman
plt.rcParams['font.serif'] = ['Times New Roman']

# 实验数据
datasets = ['ASSIST09', 'ASSIST15', 'Junyi']
models = ['1', '2', '3', '4', '5', '6', '7', '8']

improvements_1 = [1, 2, 3]
improvements_2 = [1, 2, 3]
improvements_3 = [1, 2, 3]
improvements_4 = [1, 2, 3]
improvements_5 = [1, 2, 3]
improvements_6 = [1, 2, 3]
improvements_7 = [1, 2, 3]
improvements_8 = [1, 2, 3]

# 设置图表宽度和高度
plt.figure(figsize=(15, 7))
#设置网格线
plt.grid(True, axis='y', linestyle='--', color='gray', alpha=0.4)
plt.ylim(0.7, 0.9)  # 纵坐标范围为 [0.7, 0.9]

# 绘制models上的柱状图
index = np.arange(len(datasets))
bar_width = 0.09
opacity = 0.8
# colors = [
#     '#2B558E',  # 皇家蓝
#     '#D65D2A',  # 赤陶色
#     '#4E9A4E',  # 松柏绿
#     '#904A90',  # 葡萄紫
#     '#E18727',  # 琥珀色
#     '#648FFF',  # 科技蓝（新增）
#     '#785EF0',  # 靛蓝色（新增）
#     '#DC267F'   # 玫红色（新增）
# ]
colors = [
    '#4E79A7',  # 深蓝（主推）
    '#F28E2C',  # 亮橙
    '#E15759',  # 珊瑚红
    '#76B7B2',  # 青绿色
    '#59A14F',  # 橄榄绿
    '#EDC949',  # 亮黄色
    '#AF7AA1',  # 薰衣草紫
    '#FF9DA7'   # 浅粉色（新增）
]
# colors = [
#     '#2B558E',  # 1. 对比模型1 - 皇家蓝
#     '#D65D2A',  # 2. 对比模型2 - 赤陶色
#     '#4E9A4E',  # 3. 对比模型3 - 松柏绿
#     '#904A90',  # 4. 对比模型4 - 葡萄紫
#     '#648FFF',  # 5. 对比模型5 - 科技蓝
#     '#785EF0',  # 6. 对比模型6 - 靛蓝色
#     '#969696',  # 7. 对比模型7 - 中性灰（对照组专用）
#     '#DC267F'   # 8. 自研模型 - 玫红色（Nature期刊强调色）
# ]
# colors = [
#     '#2B558E',  # 1. 对比模型1 - 皇家蓝（主推色）
#     '#1B9E77',  # 2. 对比模型2 - 翡翠绿
#     '#D95F02',  # 3. 对比模型3 - 琥珀橙
#     '#7570B3',  # 4. 对比模型4 - 薰衣草紫
#     '#66A61E',  # 5. 对比模型5 - 橄榄绿
#     '#E6AB02',  # 6. 对比模型6 - 芥末黄
#     '#A6761D',  # 7. 对比模型7 - 焦糖棕
#     '#E7298A'   # 8. 自研模型 - 珊瑚粉（高亮强调色）
# ]
rects1 = plt.bar(index, improvements_1, bar_width, alpha=opacity, color=colors[0], label='1')
rects2 = plt.bar(index + bar_width, improvements_2, bar_width, alpha=opacity, color=colors[1], label='2')
rects3 = plt.bar(index + 2*bar_width, improvements_3, bar_width, alpha=opacity, color=colors[2], label='3')
rects4 = plt.bar(index + 3*bar_width, improvements_4, bar_width, alpha=opacity, color=colors[3], label='4')
rects5 = plt.bar(index + 4*bar_width, improvements_5, bar_width, alpha=opacity, color=colors[4], label='5')
rects6 = plt.bar(index + 5*bar_width, improvements_6, bar_width, alpha=opacity, color=colors[5], label='6')
rects7 = plt.bar(index + 6*bar_width, improvements_7, bar_width, alpha=opacity, color=colors[6], label='7')
rects8 = plt.bar(index + 7*bar_width, improvements_8, bar_width, alpha=opacity, color=colors[7], label='8')

# 添加横纵坐标描述
plt.xlabel('Datasets', fontsize=18)
plt.ylabel('ACC', fontsize=18)

plt.xticks(index + 3.5*bar_width, datasets, fontsize=14)
plt.yticks(fontsize=14)
plt.legend(ncol=8, loc='upper left', fontsize=14)

ax = plt.gca()
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.4f'))
# ax.ticklabel_format(axis='y', style='plain')  # 防止科学计数法

# 添加图上的文本标签和值
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.annotate('{:.4f}'.format(height),
                     xy=(rect.get_x() + rect.get_width() / 2, height),
                     xytext=(0, 3),  # 3 points vertical offset
                     fontsize=10,
                     textcoords="offset points",
                     ha='center', va='bottom')
autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)
autolabel(rects5)
autolabel(rects6)
autolabel(rects7)
autolabel(rects8)

# 显示图表
plt.tight_layout()
plt.savefig("ACC.svg", format="svg", bbox_inches="tight")
plt.show()
