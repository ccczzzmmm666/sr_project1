import re
import matplotlib.pyplot as plt
import os
#复现figure2 √
# 定义文件类型分类
file_type_categories = {
    "multimedia": [],
    "productivity": ['.txt', '.odt', '.odp', '.ttf'],
    "plist": ['.xml'],
    "sqlite": ['.db'],
    "strings": ['.dic', '.res', '.theme', '.xlb', '.xlc'],
    "others": ['.dat', '.aff', '.ht', '.tmp', '.log', '.so', '.sod', '.soe']
}

# 初始化一个字典来存储每个分类及其计数
category_counts = {category: [] for category in file_type_categories}
total_counts = []

# 获取所有文件
input_files = [
    r'C:\Users\chenz\Desktop\sr\sr_project1_data\s_task\delete.txt',
    r'C:\Users\chenz\Desktop\sr\sr_project1_data\s_task\demonstrate.txt',# 替换为实际文件路径
    r'C:\Users\chenz\Desktop\sr\sr_project1_data\s_task\picture_edit.txt',  # 替换为实际文件路径
    r'C:\Users\chenz\Desktop\sr\sr_project1_data\s_task\rename.txt', # 替换为实际文件路径
    r'C:\Users\chenz\Desktop\sr\sr_project1_data\s_task\save.txt',  # 替换为实际文件路径
    r'C:\Users\chenz\Desktop\sr\sr_project1_data\s_task\setup.txt',  # 替换为实际文件路径
    r'C:\Users\chenz\Desktop\sr\sr_project1_data\s_task\text_edit.txt', # 替换为实际文件路径
    r'C:\Users\chenz\Desktop\sr\sr_project1_data\s_task\title_edit.txt',  # 替换为实际文件路径
]

# 读取每个文件并统计文件类型计数
for file_path in input_files:
    file_name = os.path.basename(file_path)

    # 初始化计数字典
    file_counts = {category: 0 for category in file_type_categories}
    total_count = 0

    # 读取文件内容
    with open(file_path, 'r') as file:
        data = file.readlines()

    # 统计文件类型出现次数
    for line in data:
        match = re.match(r'.*openat\(.*"([^"]+)",.*', line)
        if match:
            opened_file_name = match.group(1)
            for category, extensions in file_type_categories.items():
                for extension in extensions:
                    if opened_file_name.endswith(extension):
                        file_counts[category] += 1
                        total_count += 1

    # 记录总计数和分类计数
    total_counts.append(total_count)
    for category in file_type_categories:
        category_counts[category].append(file_counts[category])

# 计算百分比
percentages = {category: [] for category in file_type_categories}
for category in file_type_categories:
    for i in range(len(input_files)):
        if total_counts[i] > 0:
            percentages[category].append((category_counts[category][i] / total_counts[i]) * 100)
        else:
            percentages[category].append(0)

# 绘制柱状图
labels = [os.path.splitext(os.path.basename(file))[0] for file in input_files]
x = range(len(input_files))

fig, ax = plt.subplots(figsize=(10, 6))

bottom = [0] * len(input_files)
for category in file_type_categories:
    ax.bar(x, percentages[category], bottom=bottom, label=category)
    bottom = [i + j for i, j in zip(bottom, percentages[category])]

for i in range(len(input_files)):
    ax.text(i, bottom[i], str(total_counts[i]), ha='center', va='bottom')

ax.set_xlabel('operation')
ax.set_ylabel('Percentage')
ax.set_title('File Type Access Percentage')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.show()
