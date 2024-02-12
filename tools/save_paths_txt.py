import os


def save_image_paths(folder_path, output_file):
    with open(output_file, 'w') as f:
        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.endswith('.jpg') or file.endswith('.png'):
                    file_path = os.path.join(root, file)
                    f.write(file_path + '\n')
                    
folder_path = '/Users/daniorozco/Desktop/litebc_task/capillary_detection/small_test/data'
output_file = '/Users/daniorozco/Desktop/litebc_task/capillary_detection/small_test/txt_files/train.txt'
save_image_paths(folder_path, output_file)
