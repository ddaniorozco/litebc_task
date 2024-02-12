import os


def calculate_average_bbox_size(label_file, image_width, image_height):
    total_width, total_height, total_area = 0, 0, 0
    num_bboxes = 0

    with open(label_file, 'r') as f:
        lines = f.readlines()

    for line in lines:
        class_id, x_center_norm, y_center_norm, bbox_width_norm, bbox_height_norm = map(float, line.strip().split())

        # Filter out detections for class "1"
        if int(class_id) != 1:
            continue

        # Scale normalized coordinates to pixel values
        bbox_width = bbox_width_norm * image_width
        bbox_height = bbox_height_norm * image_height

        total_width += bbox_width
        total_height += bbox_height
        total_area += bbox_width * bbox_height
        num_bboxes += 1

    if num_bboxes == 0:
        return 0, 0, 0

    average_width = total_width / num_bboxes
    average_height = total_height / num_bboxes
    average_area = total_area / num_bboxes

    # print(f"Average Bbox Width: {average_width} pixels")
    # print(f"Average Bbox Height: {average_height} pixels")
    # print(f"Average Bbox Area: {average_area} square pixels")

    return average_width, average_height, average_area


def calculate_deviation(value, average_value):
    return abs(value - average_value) / average_value


def select_best_detections(label_file, output_folder, image_width, image_height):
    average_width, average_height, average_area = calculate_average_bbox_size(label_file, image_width, image_height)

    deviation_threshold = 0.1  # You can adjust this threshold as needed

    selected_detections = []

    with open(label_file, 'r') as f:
        lines = f.readlines()

    for line in lines:
        class_id, x_center_norm, y_center_norm, bbox_width_norm, bbox_height_norm = map(float, line.strip().split())

        # Filter out detections for class "1"
        if int(class_id) != 1:
            continue

        # Scale normalized coordinates to pixel values
        # x_center = x_center_norm * image_width
        # y_center = y_center_norm * image_height
        bbox_width = bbox_width_norm * image_width
        bbox_height = bbox_height_norm * image_height

        bbox_area = bbox_width * bbox_height

        # Calculate deviation from average area
        area_deviation = calculate_deviation(bbox_area, average_area)

        if area_deviation <= deviation_threshold:
            selected_detections.append(line)

        print("Selected Detections:")
        for detection in selected_detections:
            print(detection.strip())

        return selected_detections

    # Save selected detections to a new file in the output folder
    filename = os.path.basename(label_file)
    output_file = os.path.join(output_folder, filename)
    with open(output_file, 'w') as f:
        f.writelines(selected_detections)


def process_directory(input_folder, output_folder, image_width, image_height):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    label_files = [f for f in os.listdir(input_folder) if f.endswith('.txt')]

    for label_file in label_files:
        label_file_path = os.path.join(input_folder, label_file)
        select_best_detections(label_file_path, output_folder, image_width, image_height)


input_folder = '/Users/daniorozco/Desktop/litebc_task/capillary_detection/small_test/labels_testing/'
output_folder = '/Users/daniorozco/Desktop/litebc_task/capillary_detection/small_test/results_labels_average/'
images_width = 1368  # Replace with the width of your images
images_height = 1216  # Replace with the height of your images

process_directory(input_folder, output_folder, images_width, images_height)
