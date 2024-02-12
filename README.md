# Capillary Detection

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)

## Introduction

This project aims to detect capillaries in microscopy images. 
The detection system is designed to identify sharp capillaries, blurry capillaries and bubbles in images and provide bounding box coordinates.
Furthermore allows to filter and select the best detections of sharp cappilaries based on a confidence threshold and a size for further analysis.

## Project Structure

Capillary Detection

notebooks -->
- capillary_detection.ipynb
- requirements.txt

data -->
  annotations -->
  - train.txt
  - test.txt
  - validation.txt
  images -->
  - train
  - test
  - validation
capillary.yaml
    
models -->
- random_yolo.pt

runs -->
  detect -->
predict -->
- labels
- images
train -->
- weights
- training metrics
val -->
- validation metrics

src -->
  utils -->
  - split_train_test_val.py
  - save_best_detections.py
  - check_labels.py
  - save_paths.py

README.md

## Installation

To run the code, you need to install the required dependencies listed in the `notebooks/requirements.txt` file. You can install them using pip:

pip install -r notebooks/requirements.txt


## Usage

1. **Check Dataset**: Clean and go over the images and annotations using check_labels.py or https://github.com/HumanSignal/labelImg
   
2. **Data Preparation**: Split and annotate the images and annotations using the YOLO format using split_train_test_val.py and save_paths.py. Update the `data/capillary.yaml` file with dataset information.

3. **Training**: Run the training scripts in `notebooks/capillary_detection.ipynb` to train the YOLO model using the provided data.

4. **Inference**: Use the trained model to perform inference on new images. Also use (`notebooks/capillary_detection.ipynb`) for inference and visualization.

5. **Evaluation**: The output of the inference and visualization will be saved in a directory with the format shown in `runs`. Evaluate the performance of the trained model analyzing those metrics.



