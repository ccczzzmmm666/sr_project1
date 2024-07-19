import re
import os
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
#复现figure6√

# 定义文件路径
input_files = [
    r"C:\Users\chenz\Desktop\sr\sr_project1_data\s_task\delete.txt",
    r"C:\Users\chenz\Desktop\sr\sr_project1_data\s_task\setup.txt",
    r"C:\Users\chenz\Desktop\sr\sr_project1_data\s_task\save.txt",
    r"C:\Users\chenz\Desktop\sr\sr_project1_data\s_task\text_edit.txt",
    r"C:\Users\chenz\Desktop\sr\sr_project1_data\s_task\title_edit.txt",
    r"C:\Users\chenz\Desktop\sr\sr_project1_data\s_task\picture_edit.txt",
    r"C:\Users\chenz\Desktop\sr\sr_project1_data\s_task\demonstrate.txt",
    r"C:\Users\chenz\Desktop\sr\sr_project1_data\s_task\rename.txt",
]

# 定义访问模式
modes = {
    'O_RDONLY': os.O_RDONLY,
    'O_WRONLY': os.O_WRONLY,
    'O_RDWR': os.O_RDWR,
}

# 初始化存储结果的字典
results = {file: {'O_RDONLY': 0, 'O_WRONLY': 0, 'O_RDWR': 0, 'total': 0} for file in input_files}

# 处理每个文件
for file_path in input_files:
    with open(file_path, 'r') as file:
        for line in file:
            match = re.match(r'.*openat\([^,]+, "([^"]+)", ([^,]+).*', line)
            if match:
                mode = match.group(2)
                results[file_path]['total'] += 1
                if 'O_RDONLY' in mode:
                    results[file_path]['O_RDONLY'] += 1
                elif 'O_WRONLY' in mode:
                    results[file_path]['O_WRONLY'] += 1
                elif 'O_RDWR' in mode:
                    results[file_path]['O_RDWR'] += 1

# 计算百分比
percentages = {file: {'O_RDONLY': 0, 'O_WRONLY': 0, 'O_RDWR': 0} for file in input_files}
for file in input_files:
    if results[file]['total'] > 0:
        percentages[file]['O_RDONLY'] = (results[file]['O_RDONLY'] / results[file]['total']) * 100
        percentages[file]['O_WRONLY'] = (results[file]['O_WRONLY'] / results[file]['total']) * 100
        percentages[file]['O_RDWR'] = (results[file]['O_RDWR'] / results[file]['total']) * 100

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 替换为你系统中的中文字体，例如 SimHei（黑体）
plt.rcParams['axes.unicode_minus'] = False  # 解决负号无法显示的问题

# 绘制柱状图
labels = [os.path.splitext(os.path.basename(file))[0] for file in input_files]
x = range(len(input_files))

fig, ax = plt.subplots(figsize=(12, 8))

bottom = [0] * len(input_files)
for mode in ['O_RDONLY', 'O_WRONLY', 'O_RDWR']:
    ax.bar(x, [percentages[file][mode] for file in input_files], bottom=bottom, label=mode)
    bottom = [i + j for i, j in zip(bottom, [percentages[file][mode] for file in input_files])]

# 在顶部标注总次数
for i, file in enumerate(input_files):
    ax.text(i, max(bottom) + 5, f'{results[file]["total"]}', ha='center', bbox=dict(facecolor='white', alpha=0.5))

ax.set_xlabel('Operation')
ax.set_ylabel('Percentage')
ax.set_title('File Access Modes Percentage')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
