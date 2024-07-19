import re
import math
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
from collections import defaultdict
#figure1 with notes
# 起始时间
start_time = datetime.strptime('10:08:03', '%H:%M:%S')

# 读取文件内容
with open(r'C:\Users\chenz\Desktop\sr\sr_project1_data\the_entire_process\r_w.txt', 'r') as file:
    file1_data = file.read()

with open(r'C:\Users\chenz\Desktop\sr\sr_project1_data\the_entire_process\rename.txt', 'r') as file:
    file2_data = file.read()

with open(r'C:\Users\chenz\Desktop\sr\sr_project1_data\the_entire_process\fsync.txt', 'r') as file:
    file3_data = file.read()

# 解析日志数据
pattern = re.compile(r'(\d+)\s+(\d{2}:\d{2}:\d{2})\s+([a-zA-Z_]+)\(')

def parse_log_data(file_data):
    timestamps = []
    syscalls = []
    for line in file_data.strip().split('\n'):
        match = pattern.match(line)
        if match:
            pid, timestamp, syscall = match.groups()
            timestamp = datetime.strptime(timestamp, "%H:%M:%S")
            if timestamp >= start_time:
                seconds = (timestamp - start_time).total_seconds()
                timestamps.append(seconds)
                syscalls.append(syscall)
    return timestamps, syscalls

file1_timestamps, file1_syscalls = parse_log_data(file1_data)
file2_timestamps, file2_syscalls = parse_log_data(file2_data)
file3_timestamps, file3_syscalls = parse_log_data(file3_data)

# 准备绘图数据
all_timestamps = file1_timestamps + file2_timestamps + file3_timestamps
all_syscalls = file1_syscalls + file2_syscalls + file3_syscalls
all_sizes = [math.log(all_syscalls.count(syscall) + 5, 1.2) for syscall in all_syscalls]

# 获取所有唯一的系统调用
unique_syscalls = sorted(set(all_syscalls))

# 绘图
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制文件1的数据
sc1 = ax.scatter(file1_timestamps, [unique_syscalls.index(s) for s in file1_syscalls], s=all_sizes[:len(file1_syscalls)], c=all_sizes[:len(file1_syscalls)], cmap='Blues', marker='o')

# 用红色星星绘制文件2的数据
sc2 = ax.scatter(file2_timestamps, [unique_syscalls.index(s) for s in file2_syscalls], s=[size*2 for size in all_sizes[len(file1_syscalls):len(file1_syscalls)+len(file2_syscalls)]], c='red', marker='*', label='rename')

# 用绿色加号绘制文件3的数据
sc3 = ax.scatter(file3_timestamps, [unique_syscalls.index(s) for s in file3_syscalls], s=[size*2 for size in all_sizes[len(file1_syscalls)+len(file2_syscalls):]], c='green', marker='+', label='fsync')

# 插入时间节点
events = {
    "begin": "10:08:03",
    "title_edit begin": "10:08:11",
    "save": "10:08:37",
    "picture_edit": "10:08:48",
    "text_edit": "10:09:23",
    "demonstrate": "10:10:11",
    "rename": "10:10:15",
    "delete": "10:10:27"
}

for event, time_str in events.items():
    event_time = datetime.strptime(time_str, '%H:%M:%S')
    event_seconds = (event_time - start_time).total_seconds()
    ax.axvline(x=event_seconds, color='gray', linestyle='--')
    ax.text(event_seconds, len(unique_syscalls), event, rotation=90, verticalalignment='center', fontsize=8, color='black')

# 设置横坐标格式为秒数
ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))

# 设置y轴标签
plt.yticks(range(len(unique_syscalls)), unique_syscalls)

# 添加图例和标题
plt.title('Syscall Frequency Over Time')
plt.xlabel('Time (seconds since 10:08:03)')
plt.ylabel('Syscall')
plt.legend(scatterpoints=1, loc='upper left', ncol=3, fontsize=8)
plt.colorbar(sc1, label='Number of syscalls')

plt.tight_layout()
plt.show()
