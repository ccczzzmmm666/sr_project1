import re
import pandas as pd
import matplotlib.pyplot as plt
#记录全过程的读写数据量
# 读取文件内容
file_path = r'C:\Users\chenz\Desktop\sr\sr_project1_data\the_entire_process\r_w.txt'
with open(file_path, 'r') as file:
    data = file.read()

# 定义正则表达式模式
read_pattern = re.compile(r'read\(\d+, .+?, (\d+)\) = (\d+)')
write_pattern = re.compile(r'write\(\d+, .+?, (\d+)\) = (\d+)')

# 初始化计数器
read_total = 0
write_total = 0

# 解析数据
lines = data.strip().split("\n")
for line in lines:
    read_match = read_pattern.search(line)
    write_match = write_pattern.search(line)

    if read_match:
        actual_bytes = int(read_match.group(2))
        read_total += actual_bytes

    if write_match:
        actual_bytes = int(write_match.group(2))
        write_total += actual_bytes

# 准备绘图数据
data_dict = {
    'Type': ['Read', 'Write'],
    'Data (Bytes)': [read_total, write_total]
}
df = pd.DataFrame(data_dict)

# 绘制柱状图
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(df['Type'], df['Data (Bytes)'], color='blue')

# 在每个柱的顶部标注数据总量
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords='offset points',
                ha='center', va='bottom', fontsize=10, color='black')

# 设置标签和标题
ax.set_xlabel('Type')
ax.set_ylabel('Data (Bytes)')
ax.set_title('Total Data Read and Written')

# 显示图表
plt.tight_layout()
plt.show()
