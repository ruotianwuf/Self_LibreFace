import os
import shutil


def split_images(source_folder, images_per_folder=2000):
    # 获取源文件夹中的所有图片文件
    image_files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]

    # 计算需要创建的目标文件夹数量
    num_folders = len(image_files) // images_per_folder
    if len(image_files) % images_per_folder > 0:
        num_folders += 1

    # 将图片分配到目标文件夹中
    for i in range(num_folders):
        folder_name = str(i + 1)
        folder_path = os.path.join(source_folder, folder_name)
        os.makedirs(folder_path, exist_ok=True)

        # 计算当前目标文件夹应包含的图片范围
        start_index = i * images_per_folder
        end_index = min((i + 1) * images_per_folder, len(image_files))

        # 将图片复制到目标文件夹
        for j in range(start_index, end_index):
            image_file = image_files[j]
            source_file_path = os.path.join(source_folder, image_file)
            destination_file_path = os.path.join(folder_path, image_file)
            shutil.move(source_file_path, destination_file_path)

        print(f"Created folder {folder_name} and moved {end_index - start_index} images.")


# 示例用法
source_folder = "D:\\Genetic Programming\\LibreFace\\img_align_celeba"  # 替换为你的图片文件夹路径
split_images(source_folder)