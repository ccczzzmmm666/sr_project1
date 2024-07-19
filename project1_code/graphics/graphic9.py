import matplotlib.pyplot as plt
import pandas as pd
#复现figure3
# 读取数据
data = pd.read_csv(r'C:\Users\chenz\Desktop\sr\sr_project1_data\the_entire_process\file_sizes_and_categories.txt', sep=' ', header=None, names=['file', 'path', 'size', 'category'])

# 定义文件类型分类
file_type_categories = {
    "multimedia": [],
    "productivity": ['.txt', '.odt', '.odp', '.ttf'],
    "plist": ['.xml'],
    "sqlite": ['.db'],
    "strings": ['.dic', '.res', '.theme', '.xlb', '.xlc'],
    "others": ['.dat', '.aff', '.ht', '.tmp', '.log', '.so', '.sod', '.soe']
}

# 创建一个新的列 'input_file' 来表示输入文件名
data['input_file'] = data['file'].apply(lambda x: x.split('/')[-1])

# 计算百分比
category_counts = data.groupby(['input_file', 'category']).size().unstack(fill_value=0)
total_counts = category_counts.sum(axis=1)
percentages = category_counts.divide(total_counts, axis=0) * 100

# 绘制柱状图
fig, ax = plt.subplots(figsize=(12, 8))

bottom = pd.DataFrame(0, index=percentages.index, columns=percentages.columns)
for category in file_type_categories.keys():
    ax.bar(percentages.index, percentages[category], bottom=bottom[category], label=category)
    bottom = bottom.add(percentages[category], axis=0)

for i in range(len(percentages.index)):
    ax.text(i, bottom.iloc[i].max(), str(total_counts[i]), ha='center', va='bottom')

ax.set_xlabel('Input Files')
ax.set_ylabel('Percentage')
ax.set_title('File Type Access Percentage by Input File')
ax.legend()

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
