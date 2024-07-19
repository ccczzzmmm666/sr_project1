import re
import os
import matplotlib.pyplot as plt
from collections import defaultdict
#figure 8 and 9

# 定义输入文件路径
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

# 初始化存储结果的字典
results = {file: {'read': 0, 'write': 0, 'sequential_read': 0, 'non_sequential_read': 0,
                  'sequential_write': 0, 'non_sequential_write': 0} for file in input_files}
fd_positions = defaultdict(lambda: 0)

def process_trace(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            open_match = re.match(r'.*openat\([^,]+, "([^"]+)", ([^,]+)\) = (\d+)', line)
            if open_match:
                filepath = open_match.group(1)
                mode = open_match.group(2)
                fd = int(open_match.group(3))
                fd_positions[fd] = 0

            read_match = re.match(r'.*read\((\d+), .*?, (\d+)\) = (\d+)', line)
            if read_match:
                fd = int(read_match.group(1))
                count = int(read_match.group(3))
                if fd in fd_positions:
                    results[file_path]['read'] += count
                    if fd_positions[fd] == 0:
                        results[file_path]['sequential_read'] += count
                    else:
                        results[file_path]['non_sequential_read'] += count
                    fd_positions[fd] += count

            pread_match = re.match(r'.*pread64\((\d+), .*?, (\d+), (\d+)\) = (\d+)', line)
            if pread_match:
                fd = int(pread_match.group(1))
                offset = int(pread_match.group(3))
                count = int(pread_match.group(4))
                if fd in fd_positions:
                    results[file_path]['read'] += count
                    if fd_positions[fd] == offset:
                        results[file_path]['sequential_read'] += count
                    else:
                        results[file_path]['non_sequential_read'] += count
                    fd_positions[fd] = offset + count

            write_match = re.match(r'.*write\((\d+), .*?, (\d+)\) = (\d+)', line)
            if write_match:
                fd = int(write_match.group(1))
                count = int(write_match.group(3))
                if fd in fd_positions:
                    results[file_path]['write'] += count
                    if fd_positions[fd] == 0:
                        results[file_path]['sequential_write'] += count
                    else:
                        results[file_path]['non_sequential_write'] += count
                    fd_positions[fd] += count

            pwrite_match = re.match(r'.*pwrite64\((\d+), .*?, (\d+), (\d+)\) = (\d+)', line)
            if pwrite_match:
                fd = int(pwrite_match.group(1))
                offset = int(pwrite_match.group(3))
                count = int(pwrite_match.group(4))
                if fd in fd_positions:
                    results[file_path]['write'] += count
                    if fd_positions[fd] == offset:
                        results[file_path]['sequential_write'] += count
                    else:
                        results[file_path]['non_sequential_write'] += count
                    fd_positions[fd] = offset + count

            lseek_match = re.match(r'.*lseek\((\d+), (\d+), (\w+)\) = (\d+)', line)
            if lseek_match:
                fd = int(lseek_match.group(1))
                pos = int(lseek_match.group(4))
                fd_positions[fd] = pos

# 处理每个输入文件
for file_path in input_files:
    process_trace(file_path)

# 计算读操作的百分比
percentages_read = {file: {'sequential_read': 0, 'non_sequential_read': 0} for file in input_files}
for file in input_files:
    total_read = results[file]['read']
    if total_read > 0:
        percentages_read[file]['sequential_read'] = (results[file]['sequential_read'] / total_read) * 100
        percentages_read[file]['non_sequential_read'] = (results[file]['non_sequential_read'] / total_read) * 100

# 计算写操作的百分比
percentages_write = {file: {'sequential_write': 0, 'non_sequential_write': 0} for file in input_files}
for file in input_files:
    total_write = results[file]['write']
    if total_write > 0:
        percentages_write[file]['sequential_write'] = (results[file]['sequential_write'] / total_write) * 100
        percentages_write[file]['non_sequential_write'] = (results[file]['non_sequential_write'] / total_write) * 100

# 绘制读操作的柱状图
labels = [os.path.splitext(os.path.basename(file))[0] for file in input_files]
x = range(len(input_files))

fig, ax = plt.subplots(figsize=(12, 8))

bottom = [0] * len(input_files)
for category in ['sequential_read', 'non_sequential_read']:
    ax.bar(x, [percentages_read[file][category] for file in input_files], bottom=bottom, label=category.replace('_read', ''))
    bottom = [i + j for i, j in zip(bottom, [percentages_read[file][category] for file in input_files])]

for i, file in enumerate(input_files):
    total_read = results[file]['read']
    ax.text(i, bottom[i], f"{total_read / (1024*1024):.1f}MB", ha='center', va='bottom')

ax.set_xlabel('Operation')
ax.set_ylabel('Percentage')
ax.set_title('File Read Access Patterns')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.xticks(rotation=45)
plt.subplots_adjust(top=0.85)  # 调整图表的上边距
plt.tight_layout()
plt.show()

# 绘制写操作的柱状图
fig, ax = plt.subplots(figsize=(12, 8))

bottom = [0] * len(input_files)
for category in ['sequential_write', 'non_sequential_write']:
    ax.bar(x, [percentages_write[file][category] for file in input_files], bottom=bottom, label=category.replace('_write', ''))
    bottom = [i + j for i, j in zip(bottom, [percentages_write[file][category] for file in input_files])]

for i, file in enumerate(input_files):
    total_write = results[file]['write']
    ax.text(i, bottom[i], f"{total_write / (1024*1024):.1f}MB", ha='center', va='bottom')

ax.set_xlabel('Operation')
ax.set_ylabel('Percentage')
ax.set_title('File Write Access Patterns')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.xticks(rotation=45)
plt.subplots_adjust(top=0.85)  # 调整图表的上边距
plt.tight_layout()
plt.show()
