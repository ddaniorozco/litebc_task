import os

def visualize_labels(image_folder, label_folder, class_names, output_file):
    image_files = sorted(os.listdir(image_folder))
    label_files = sorted(os.listdir(label_folder))

    if len(image_folder) > len(label_folder):
        print('Error: Not the same amount of files. More images than labels.')
    elif len(image_folder) < len(label_folder):
        print('Error: Not the same amount of files. More labels than images.')
    elif len(image_folder) == len(label_folder):
        print('Processing images and labels')

    class_counts = {class_name: 0 for class_name in class_names}

    for image_file, label_file in zip(image_files, label_files):
        label_path = os.path.join(label_folder, label_file)

        with open(label_path, 'rb') as f:
            lines = f.readlines()

        image_class_counts = {class_name: 0 for class_name in class_names}

        for line in lines:
            line = line.decode('ascii', errors='ignore').strip()  # Decode as ASCII
            if not line:
                continue

            class_id, _, _, _, _ = map(float, line.split())

            class_name = class_names[int(class_id)]
            image_class_counts[class_name] += 1

        for class_name, count in image_class_counts.items():
            class_counts[class_name] += count

    with open(output_file, 'w') as report_file:
        report_file.write("Total Class Counts:\n")
        for class_name, total_count in class_counts.items():
            report_file.write(f"{class_name}: {total_count}\n")


image_folder = '/Users/daniorozco/Desktop/litebc_task/capillary_detection/images'
label_folder = '/Users/daniorozco/Desktop/litebc_task/capillary_detection/labels'
class_names = ['BLURRY', 'SHARP', 'BUBBLE']
output_file = 'report.txt'

visualize_labels(image_folder, label_folder, class_names, output_file)
