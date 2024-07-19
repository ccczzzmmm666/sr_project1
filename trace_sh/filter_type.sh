#!/bin/bash

# 定义输入和输出文件路径
input_files=(
	"$HOME/project1/trace_data/s_task/delete.txt"
	"$HOME/project1/trace_data/s_task/demonstrate.txt"
	"$HOME/project1/trace_data/s_task/picture_edit.txt"
	"$HOME/project1/trace_data/s_task/rename.txt"
	"$HOME/project1/trace_data/s_task/save.txt"
	"$HOME/project1/trace_data/s_task/setup.txt"
	"$HOME/project1/trace_data/s_task/text_edit.txt"
	"$HOME/project1/trace_data/s_task/title_edit.txt"
)

# 定义文件类型分类
declare -A file_type_categories
file_type_categories=(
	["multimedia"]=""
	["productivity"]=".txt .odt .odp .ttf"
	["plist"]=".xml"
	["sqlite"]=".db"
	["strings"]=".dic .res .theme .xlb .xlc"
	["others"]=".dat .aff .ht .tmp .log .so .sod .soe"
)

# 初始化字典来存储每个分类及其计数
declare -A category_counts
for category in "${!file_type_categories[@]}"; do
	category_counts[$category]=0
done

# 读取每个文件并统计文件类型计数和大小
output_file="file_sizes_and_categories.txt"
>"$output_file"

for file_path in "${input_files[@]}"; do
	if [[ -f "$file_path" ]]; then
		file_name=$(basename "$file_path")
		declare -A seen_files # 用于跟踪已经处理过的文件
		while IFS= read -r line; do
			if [[ "$line" =~ openat\([0-9]+,\"([^\"]+)\",.* ]]; then
				opened_file_name="${BASH_REMATCH[1]}"
				if [[ ! -v seen_files["$opened_file_name"] ]]; then
					seen_files["$opened_file_name"]=1
					for category in "${!file_type_categories[@]}"; do
						for extension in ${file_type_categories[$category]}; do
							if [[ "$opened_file_name" == *"$extension" ]]; then
								file_size=$(stat -c %s "$opened_file_name" 2>/dev/null)
								if [[ $? -eq 0 ]]; then
									category_counts[$category]=$((category_counts[$category] + 1))
									echo "$file_name $opened_file_name $file_size $category" >>"$output_file"
									echo "Recorded: $file_name $opened_file_name $file_size $category" # 调试输出
								else
									echo "Error getting size for: $opened_file_name" # 调试输出
								fi
							fi
						done
					done
				fi
			fi
		done <"$file_path"
	else
		echo "Error: $file_path not found."
	fi
done

echo "Results saved to $output_file"
