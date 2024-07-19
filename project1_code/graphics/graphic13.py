import re
import pandas as pd
import matplotlib.pyplot as plt


# 解析日志文件并提取`rename`操作的记录
def parse_rename_logs(log_file_path):
    with open(r'C:\Users\chenz\Desktop\sr\sr_project1_data\the_entire_process\openoffice_final.txt', 'r') as file:
        data = file.read()

    # 解析rename操作的正则表达式
    rename_pattern = re.compile(r'(\d+)\s+(\d+:\d+:\d+)\s+rename\("(.+?)",\s+"(.+?)"\)\s+=\s+0')
    # 解析stat和fstat操作的正则表达式
    stat_pattern = re.compile(r'(\d+)\s+(\d+:\d+:\d+)\s+(stat|fstat|lstat)\("(.+?)",\s+\{st_mode=.+?, st_size=(\d+),')

    rename_operations = []
    stat_operations = []

    for line in data.strip().split('\n'):
        rename_match = rename_pattern.match(line)
        if rename_match:
            pid, time, old_path, new_path = rename_match.groups()
            rename_operations.append((pid, time, old_path, new_path))

        stat_match = stat_pattern.match(line)
        if stat_match:
            pid, time, syscall, file_path, file_size = stat_match.groups()
            stat_operations.append((pid, time, syscall, file_path, int(file_size)))

    return rename_operations, stat_operations


# 计算涉及的数据量
def calculate_data_amount(rename_operations, stat_operations):
    data_amounts = []
    for pid, time, old_path, new_path in rename_operations:
        # 找到与old_path匹配的文件大小
        file_size = None
        for stat_pid, stat_time, syscall, file_path, size in stat_operations:
            if file_path == old_path and stat_pid == pid:
                file_size = size
                break

        if file_size is not None:
            data_amounts.append((pid, time, old_path, new_path, file_size))

    return data_amounts


# 读取日志文件
log_file_path = r'C:\Users\chenz\Desktop\sr\sr_project1_data\the_entire_process\strace.log'
rename_operations, stat_operations = parse_rename_logs(log_file_path)
data_amounts = calculate_data_amount(rename_operations, stat_operations)

# 输出结果
df = pd.DataFrame(data_amounts, columns=['PID', 'Time', 'Old Path', 'New Path', 'Data Amount'])
print(df)

# 将结果保存到CSV文件
df.to_csv('rename_data_amounts.csv', index=False)

# 可视化结果
fig, ax = plt.subplots(figsize=(12, 8))
bars = ax.bar(range(len(df)), df['Data Amount'], color='blue')

# 设置标签和标题
ax.set_xlabel("Rename Operation Index")
ax.set_ylabel("Data Amount (bytes)")
ax.set_title("Data Amount Involved in Rename Operations")
ax.set_xticks(range(len(df)))
ax.set_xticklabels(df['Time'], rotation=90)

# 在柱状图上标注数据量
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

plt.tight_layout()
plt.show()
