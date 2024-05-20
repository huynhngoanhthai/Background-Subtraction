# Background Replacement

This Python script provides functionality to replace the background of an object image with two different background images based on color difference thresholding.

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- NumPy
- Matplotlib

## Download and Clone

You can clone this project using git. Open your terminal and run the following command:

```bash
git clone <repository_url>

```
After that, you can install the required packages using pip. In the root directory of the project, run the following command:

```bash
pip install -r requirements.txt

```
## Usage

1. Make sure you have the required libraries installed.
2. Organize your background and object images. The object image should have a background you want to replace.
3. Adjust the file paths in the script to point to your background and object images.
4. Run the script.

## Functionality

The script consists of the following functions:

### `computeBinaryMask(difference_single_channel, threshold=15)`

This function applies a threshold to create a binary mask based on color difference. Pixels with a color difference greater than or equal to the threshold are set to 255 (white), while others are set to 0 (black).

### `computeDifference(bg_img, input_img)`

Calculates the absolute color difference between two images. It converts the three-channel difference to a single-channel image by taking the average, reducing the difference data to a single intensity value.

### `replaceBackGround(bg_image1, bg_image2, ob_image)`

This function replaces the background of the object image. It computes the difference between the object image and the first background image, creates a binary mask based on the difference, and replaces the background pixels with the second background image.

## Example

```python
import numpy as np
import matplotlib.pyplot as plt
import cv2

# Load input images
bg_image1 = cv2.imread('images/background1.png')
bg_image2 = cv2.imread('images/background2.png')
ob_image  = cv2.imread('images/object.png')

# Resize input images
bg_image1 = cv2.resize(bg_image1, (640, 480))
bg_image2 = cv2.resize(bg_image2, (640, 480))
ob_image  = cv2.resize(ob_image,  (640, 480))

# Convert images from BGR to RGB color space
bg_image1 = cv2.cvtColor(bg_image1, cv2.COLOR_BGR2RGB)
bg_image2 = cv2.cvtColor(bg_image2, cv2.COLOR_BGR2RGB)
ob_image  = cv2.cvtColor(ob_image,  cv2.COLOR_BGR2RGB)

# Replace background
output_image = replaceBackGround(bg_image1, bg_image2, ob_image)

# Display the output image
plt.imshow(output_image)
plt.axis('off')
plt.show()
```
## License

This project is licensed under the MIT License.

