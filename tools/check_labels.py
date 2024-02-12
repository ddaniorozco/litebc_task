import cv2
import os


def visualize_labels(image_folder, label_folder, class_names):
    image_files = sorted(os.listdir(image_folder))
    label_files = sorted(os.listdir(label_folder))

    assert len(image_files) == len(label_files), "Number of images and labels do not match"

    for image_file, label_file in zip(image_files, label_files):
        image_path = os.path.join(image_folder, image_file)
        label_path = os.path.join(label_folder, label_file)

        image = cv2.imread(image_path)
        height, width, _ = image.shape

        image_name = os.path.splitext(image_file)[0]
        print(f"Image: {image_name}")

        with open(label_path, 'rb') as f:
            lines = f.readlines()

        for line in lines:
            line = line.decode('ascii', errors='ignore').strip()  # Decode as ASCII
            if not line:
                continue  # Skip empty lines

            class_id, x_center, y_center, bbox_width, bbox_height = map(float, line.split())

            # Convert YOLO format to pixel coordinates
            x_center *= width
            y_center *= height
            bbox_width *= width
            bbox_height *= height

            # Calculate top-left corner coordinates
            x_min = int(x_center - bbox_width / 2)
            y_min = int(y_center - bbox_height / 2)
            x_max = int(x_center + bbox_width / 2)
            y_max = int(y_center + bbox_height / 2)

            # Draw bounding box
            color = (0, 255, 0)  # Green color
            thickness = 2
            cv2.rectangle(image, (x_min, y_min), (x_max, y_max), color, thickness)

            # Add class name
            class_name = class_names[int(class_id)]
            cv2.putText(image, class_name, (x_min, y_min - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        # Display image with bounding boxes
        cv2.imshow(f'Image: {image_name}', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


image_folder_path = '/Users/daniorozco/Desktop/litebc_task/capillary_detection/images'
label_folder_path = '/Users/daniorozco/Desktop/litebc_task/capillary_detection/labels'
classes_names = ['BLURRY', 'SHARP', 'BUBBLE']

visualize_labels(image_folder_path, label_folder_path, classes_names)
