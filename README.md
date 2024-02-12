# Capillary Detection

This project aims to detect capillaries in microscopy images. 
The detection system is designed to identify sharp capillaries, blurry capillaries and bubbles in images and provide bounding box coordinates for further analysis.

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Introduction

Capillary detection plays a crucial role in various medical applications, particularly in blood flow analysis and disease diagnosis. This project leverages the YOLO algorithm to detect capillaries in microscopy images, facilitating blood flow recording and analysis.

## Project Structure

Capillary Detection

notebooks -->
- capillary_detection.ipynb
- requirements.txt

├── data/
│ ├── annotations/
│ │ ├── train.txt
│ │ ├── test.txt
│ │ └── validation.txt
│ ├── images/
│ │ ├── train/
│ │ ├── test/
│ │ └── validation/
│ └── capillary.yaml
│
├── models/
│ └── random_yolo.pt
│
├── src/
│ ├── utils/
│ │ ├── data_utils.py
│ │ └── visualization_utils.py
│ └── train.py
│
├── README.md


