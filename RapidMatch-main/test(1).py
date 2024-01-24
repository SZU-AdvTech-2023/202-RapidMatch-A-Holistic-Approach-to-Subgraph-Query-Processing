import csv

csv_file_path = 'result_output_4_vertex_youtube.csv'
# =SUM(A2:A101)
# =SUM(B2:B101)
# =SUM(C2:C101)
# =SUM(A2:A51)
# =SUM(B2:B51)
# =SUM(C2:C51)
# =SUM(A52:A101)
# =SUM(B52:B101)
# =SUM(C52:C101)
# 指定文件路径
file_path = './output_4_vertex_youtube.txt'

data = []
# 使用 'utf-8' 编码打开文件，以确保正确处理中文字符
with open(file_path, 'r', encoding='utf-8') as file:
    # 逐行读取文件
    for line in file:
        # print(line)
        if line.startswith("Query time (seconds)"):
            row_data = []
            # print(line)
            split_parts = line.split()
            print(split_parts[3])
            # ss = split_parts[5].split(":")
            # print(ss[1])
            row_data.append(split_parts[3])
            # row_data.append(ss[1])
        if line.startswith("#Embeddings"):
            # print(line)
            split_parts = line.split()
            print(split_parts[1])
            # ss = split_parts[5].split(":")
            # print(ss[1])
            row_data.append(split_parts[1])
            # row_data.append(ss[1])
            data.append(row_data)

# 写入 CSV 文件
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    # 写入表头
    csv_writer.writerow(["Query time cost (s)","#Embeddings"])
    # 写入数据
    csv_writer.writerows(data)
print("aa".startswith("a"))