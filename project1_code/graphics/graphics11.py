import re
import os
import matplotlib.pyplot as plt
#复现figure7√
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

# 初始化存储结果的字典
byte_counts = {'read_only': [], 'write_only': [], 'both_reads': [], 'both_writes': []}
total_bytes = []

# 处理每个文件
for file_path in input_files:
    fd_usage = {}  # 文件描述符的使用情况
    read_bytes = {}
    write_bytes = {}
    total = 0

    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        # 解析 openat 系统调用
        match_open = re.match(r'.*openat\(.*"([^"]+)",.*O_([^,]+).*=\s*(\d+)', line)
        if match_open:
            filename, mode, fd = match_open.groups()
            fd = int(fd)
            if 'RDONLY' in mode:
                fd_usage[fd] = 'read_only'
            elif 'WRONLY' in mode:
                fd_usage[fd] = 'write_only'
            elif 'RDWR' in mode:
                fd_usage[fd] = 'both'

        # 解析 read 系统调用
        match_read = re.match(r'.*read\((\d+),.*=\s*(\d+)', line)
        if match_read:
            fd, bytes_read = map(int, match_read.groups())
            if fd in fd_usage:
                read_bytes[fd] = read_bytes.get(fd, 0) + bytes_read

        # 解析 write 系统调用
        match_write = re.match(r'.*write\((\d+),.*=\s*(\d+)', line)
        if match_write:
            fd, bytes_written = map(int, match_write.groups())
            if fd in fd_usage:
                write_bytes[fd] = write_bytes.get(fd, 0) + bytes_written

    # 计算每种访问类型的字节数
    read_only_bytes = sum(bytes for fd, bytes in read_bytes.items() if fd_usage.get(fd) == 'read_only')
    write_only_bytes = sum(bytes for fd, bytes in write_bytes.items() if fd_usage.get(fd) == 'write_only')
    both_reads_bytes = sum(bytes for fd, bytes in read_bytes.items() if fd_usage.get(fd) == 'both')
    both_writes_bytes = sum(bytes for fd, bytes in write_bytes.items() if fd_usage.get(fd) == 'both')
    total = read_only_bytes + write_only_bytes + both_reads_bytes + both_writes_bytes

    byte_counts['read_only'].append(read_only_bytes)
    byte_counts['write_only'].append(write_only_bytes)
    byte_counts['both_reads'].append(both_reads_bytes)
    byte_counts['both_writes'].append(both_writes_bytes)
    total_bytes.append(total)

# 计算百分比
percentages = {key: [value[i] / total_bytes[i] * 100 if total_bytes[i] > 0 else 0 for i in range(len(input_files))]
               for key, value in byte_counts.items()}

# 绘制柱状图
labels = [os.path.splitext(os.path.basename(file))[0] for file in input_files]
x = range(len(input_files))

fig, ax = plt.subplots(figsize=(12, 8))

bottom = [0] * len(input_files)
for key in ['read_only', 'both_reads', 'both_writes', 'write_only']:
    ax.bar(x, percentages[key], bottom=bottom, label=key.replace('_', ' ').title())
    bottom = [i + j for i, j in zip(bottom, percentages[key])]


def format_size(size):
    """格式化字节大小为易读的格式"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024


for i in range(len(input_files)):
    ax.text(i, 105, format_size(total_bytes[i]), ha='center')

ax.set_xlabel('Operation')
ax.set_ylabel('Percentage')
ax.set_title('Read/Write Distribution By Bytes')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
