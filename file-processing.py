import os
import tarfile

# 指定tar文件所在的目录
tar_dir = "/Users/hanlin/Desktop/gpt/openwebtext"

# 指定解压后的目标目录
output_dir = "/Users/hanlin/Desktop/gpt/openwebtext/extracted"

# 创建目标目录(如果不存在)
os.makedirs(output_dir, exist_ok=True)

# 遍历目录下的所有文件
for filename in os.listdir(tar_dir):
    # 检查文件是否为tar文件
    if filename.endswith(".tar"):
        tar_path = os.path.join(tar_dir, filename)
        print(tar_path)
        # 打开tar文件
        with tarfile.open(tar_path, "r") as tar:
            # 解压tar文件到目标目录
            tar.extractall(output_dir)

print("解压完成!")