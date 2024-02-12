import os
import shutil
import random
# import argparse

def split_dataset(source_folder, train_percent, test_percent, val_percent):

    train_folder = os.path.join(source_folder, 'train')
    test_folder = os.path.join(source_folder, 'test')
    val_folder = os.path.join(source_folder, 'validation')
    for folder in [train_folder, test_folder, val_folder]:
        os.makedirs(folder, exist_ok=True)

    for file in os.listdir(source_folder):
        if file.endswith('.jpg') or file.endswith('.png') or file.endswith('.txt'):
            shutil.copy(os.path.join(source_folder, file), os.path.join(train_folder, file))

    train_files = [file for file in os.listdir(train_folder) if file.endswith('.jpg') or file.endswith('.png')]
    random.shuffle(train_files)

    total_train_files = len(train_files)
    num_test = int(total_train_files * test_percent / 100)
    num_val = int(total_train_files * val_percent / 100)

    for file in train_files[:num_test]:
        shutil.move(os.path.join(train_folder, file), os.path.join(test_folder, file))
        txt_file = file.split('.')[0] + '.txt'
        if os.path.exists(os.path.join(train_folder, txt_file)):
            shutil.move(os.path.join(train_folder, txt_file), os.path.join(test_folder, txt_file))
    for file in train_files[num_test:num_test + num_val]:
        shutil.move(os.path.join(train_folder, file), os.path.join(val_folder, file))
        txt_file = file.split('.')[0] + '.txt'
        if os.path.exists(os.path.join(train_folder, txt_file)):
            shutil.move(os.path.join(train_folder, txt_file), os.path.join(val_folder, txt_file))


source_folder_path = '/Users/daniorozco/Desktop/litebc_task/capillary_detection/split/small_dataset'
train_percent = 75
test_percent = 15
val_percent = 15

split_dataset(source_folder_path, train_percent, test_percent, val_percent)
