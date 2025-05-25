# Copyright(c) 2024 YiChengLin
# 保留所有权利。   
# @Time    : 2024/7/29 22:00  
# @Author  : YiChengLin  
# @File    : curveG.py  
# @Software: PyCharm
# 适用于损失函数或者其他指标曲线图

import matplotlib.pyplot as plt
import numpy as np

# 假设的时间数据（以秒为单位），这里我们简单地生成一些随机数据
time_points = np.linspace(0, 1036800, 100)  # 生成100个时间点
# 假设有两个不同的变量或状态，每个状态随时间变化
state1 = np.sin(time_points / (1036800 / (2 * np.pi)))  # 正弦波表示一个状态
state2 = np.cos(time_points / (1036800 / (2 * np.pi))) * 0.5 + 0.5  # 余弦波调整幅度和偏移表示另一个状态

# 创建图形和轴
fig, ax = plt.subplots()

# 绘制两个状态，使用不同的颜色
ax.plot(time_points, state1, label='State 1', color='#B291B5', lw=2)
ax.plot(time_points, state2, label='State 2', color='#3BA997', lw=2)

# 设置标题和标签
ax.set_title('Knowledge State Evolution (m=1036800s)')
ax.set_xlabel('Time (s)')
ax.set_ylabel('State Value')

# 添加图例
ax.legend()

# 显示图形
plt.grid(True)  # 显示网格线
plt.show()