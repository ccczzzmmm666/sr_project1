#复现figure4√
import pandas as pd
import matplotlib.pyplot as plt
import glob

# 文件路径列表（假设文件路径中包含特定的模式，例如全部在同一个文件夹内）
file_paths = glob.glob(r'C:\Users\chenz\Desktop\sr\sr_project1_data\file_sizes\*.txt')

# 定义文件大小分类
categories = ['<4KB', '<64KB', '<1MB', '<10MB', '>=10MB']
bins = [0, 4*1024, 64*1024, 1024*1024, 10*1024*1024, float('inf')]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# 创建一个 DataFrame 用于存储所有文件的结果
results = pd.DataFrame(columns=categories)

# 处理每个文件
total_lines = {}  # 用于存储每个文件的总行数
for file_path in file_paths:
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

    # 根据文件大小分类
    df['category'] = pd.cut(df['size'], bins, labels=categories, right=False)

    # 统计每个分类的文件访问次数
    category_counts = df['category'].value_counts().reindex(categories, fill_value=0)

    # 计算每个分类的百分比
    total_accesses = category_counts.sum()
    category_percentages = (category_counts / total_accesses) * 100

    # 将结果存储到 DataFrame 中
    file_name = file_path.split('\\')[-1].replace('.txt', '')
    results.loc[file_name] = category_percentages

    # 存储每个文件的总行数
    total_lines[file_name] = len(df)

# 绘制图表
plt.figure(figsize=(12, 8))

# 绘制每个文件的柱子
bottom = [0] * len(results)
for i, category in enumerate(categories):
    plt.bar(results.index, results[category], bottom=bottom, color=colors[i], edgecolor='black', label=category)
    bottom += results[category]

# 添加总行数标签
for i, file_name in enumerate(results.index):
    total_lines_str = f'Total accesses: {total_lines[file_name]}'
    plt.text(i, 105, total_lines_str, ha='center', va='bottom', fontsize=8, weight='bold')

plt.xlabel('Operation')
plt.ylabel('Percentage (%)')
plt.title('File Size Distribution by Percentage for Each Operation')
plt.legend(title='File Size Category')
plt.xticks(rotation=45)
plt.tight_layout()

# 保存和显示图表
output_image_path = r'C:\Users\chenz\Desktop\sr\sr_project1_data\file_size_distribution_percentage_multiple_files_times.png'
plt.savefig(output_image_path)
plt.show()
