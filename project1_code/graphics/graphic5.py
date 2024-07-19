#这个是一个过程的不同数据量对应不同的柱子
# import pandas as pd
# import matplotlib.pyplot as plt
# #仿照figure 5
# # 加载文件
# file_path = r'C:\Users\chenz\Desktop\sr\sr_project1_data\s_task\save_file_sizes.txt'
#
# # 读取文件并处理异常行
# data = []
# with open(file_path, 'r') as file:
#     for line in file:
#         parts = line.strip().split(' ')
#         if len(parts) >= 2:
#             try:
#                 size = int(parts[0])
#                 filename = ' '.join(parts[1:])
#                 data.append([size, filename])
#             except ValueError:
#                 # 跳过无法解析的行
#                 continue
#
# # 创建 DataFrame
# df = pd.DataFrame(data, columns=['size', 'filename'])
#
# # 去重，只保留单个文件的最大数据量
# df = df.drop_duplicates(subset='filename', keep='first')
#
# # 定义文件大小分类
# categories = ['<4KB', '<64KB', '<1MB', '<10MB', '>=10MB']
# bins = [0, 4*1024, 64*1024, 1024*1024, 10*1024*1024, float('inf')]
#
# # 根据文件大小分类
# df['category'] = pd.cut(df['size'], bins, labels=categories, right=False)
#
# # 统计每个分类的文件数量
# category_counts = df['category'].value_counts().reindex(categories, fill_value=0)
#
# # 计算每个分类的百分比
# total_files = len(df)
# category_percentages = (category_counts / total_files) * 100
#
# # 计算总数据量并选择合适的单位
# total_size = df['size'].sum()
# units = ['B', 'KB', 'MB', 'GB', 'TB']
# unit_index = 0
# while total_size >= 1024 and unit_index < len(units) - 1:
#     total_size /= 1024
#     unit_index += 1
# total_size_str = f'{total_size:.2f} {units[unit_index]}'
#
# # 绘制条形图
# plt.figure(figsize=(10, 6))
# colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
# bars = plt.bar(categories, category_percentages, color=colors)
#
# # 在每个柱的顶部添加数据标签
# for bar in bars:
#     yval = bar.get_height()
#     plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, f'{yval:.2f}%', ha='center', va='bottom')
#
# # 添加总数据量，调整位置以避免重叠
# plt.text(2, max(category_percentages) + 10, f'Total size: {total_size_str}', ha='center', va='bottom', fontsize=12, weight='bold')
#
# plt.xlabel('File Size Category')
# plt.ylabel('Percentage (%)')
# plt.title('File Size Distribution by Percentage')
# plt.xticks(rotation=45)
# plt.tight_layout()
#
# # 保存和显示图表
# output_image_path = r'C:\Users\chenz\Desktop\sr\sr_project1_data\file_size_distribution_percentage(save).png'
# plt.savefig(output_image_path)
# plt.show()


# 这个是一个过程合成一个柱子 且只包括一个过程
import pandas as pd
import matplotlib.pyplot as plt

# 加载文件
file_path = r'C:\Users\chenz\Desktop\sr\sr_project1_data\s_task\delete_file_sizes.txt'

# 读取文件并处理异常行
data = []
with open(file_path, 'r') as file:
    for line in file:
        parts = line.strip().split(' ')
        if len(parts) >= 2:
            try:
                size = int(parts[0])
                filename = ' '.join(parts[1:])
                data.append([size, filename])
            except ValueError:
                # 跳过无法解析的行
                continue

# 创建 DataFrame
df = pd.DataFrame(data, columns=['size', 'filename'])

# 去重，只保留单个文件的最大数据量
df = df.drop_duplicates(subset='filename', keep='first')

# 定义文件大小分类
categories = ['<4KB', '<64KB', '<1MB', '<10MB', '>=10MB']
bins = [0, 4*1024, 64*1024, 1024*1024, 10*1024*1024, float('inf')]

# 根据文件大小分类
df['category'] = pd.cut(df['size'], bins, labels=categories, right=False)

# 统计每个分类的文件数量
category_counts = df['category'].value_counts().reindex(categories, fill_value=0)

# 计算每个分类的百分比
total_files = len(df)
category_percentages = (category_counts / total_files) * 100

# 计算总数据量并选择合适的单位
total_size = df['size'].sum()
units = ['B', 'KB', 'MB', 'GB', 'TB']
unit_index = 0
while total_size >= 1024 and unit_index < len(units) - 1:
    total_size /= 1024
    unit_index += 1
total_size_str = f'{total_size:.2f} {units[unit_index]}'

# 绘制一个柱形图，显示所有分类的百分比
plt.figure(figsize=(10, 6))
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
bars = plt.bar(['File Size Distribution'], [100], color='white', edgecolor='black')

# 在柱子内部绘制各个分类的百分比
bottom = 0
for i, category in enumerate(categories):
    height = category_percentages[i]
    plt.bar(['File Size Distribution'], [height], bottom=bottom, color=colors[i], edgecolor='black', label=f'{category} ({height:.2f}%)')
    bottom += height

# 添加总数据量
plt.text(0, 105, f'Total size: {total_size_str}', ha='center', va='bottom', fontsize=12, weight='bold')

plt.xlabel('')
plt.ylabel('Percentage (%)')
plt.title('File Size Distribution by Percentage')
plt.legend()
plt.tight_layout()

# 保存和显示图表
output_image_path = r'C:\Users\chenz\Desktop\sr\sr_project1_data\file_size_distribution_percentage_single_bar(delete).png'
plt.savefig(output_image_path)
plt.show()
