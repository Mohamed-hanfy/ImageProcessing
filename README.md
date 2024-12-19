# Image Processing GUI Application

A user-friendly desktop application for basic image processing operations built with PyQt5 and OpenCV.

## Features

- Load and save images in multiple formats (PNG, JPG, JPEG, BMP)
- Basic image operations:
  - Resize images with custom dimensions
  - Crop images with precise coordinates
  - Rotate images at any angle
  - Apply Gaussian blur
  - Apply Median blur
  - Reduce noise using bilateral filter
- Real-time preview of changes
- Simple and intuitive graphical interface
- Comprehensive error handling

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/image-processor-gui.git
cd image-processor-gui
```

2. Install required packages:
```bash
pip install opencv-python numpy PyQt5
```

## Usage

1. Run the application:
```bash
python image_processor.py
```

2. Using the application:
   - Click "Load Image" to open an image file
   - Select any operation from the available buttons
   - Follow the dialog prompts to enter parameters
   - Click "Save Image" to save your processed image

## Operations Guide

### Resize Image
- Enter new width and height in pixels
- The image will be resized while maintaining aspect ratio

### Crop Image
- Enter X and Y coordinates for the starting point
- Specify desired width and height for the cropped area

### Rotate Image
- Enter rotation angle in degrees
- Positive angles rotate clockwise
- Negative angles rotate counter-clockwise

### Blur Effects
- Gaussian Blur: Enter kernel size (odd number)
- Median Blur: Enter kernel size (odd number)
- Larger kernel sizes create stronger blur effects

### Noise Reduction
- Automatically applies bilateral filter
- Reduces noise while preserving edges

## Error Handling

The application includes comprehensive error handling:
- Input validation for all operations
- File format validation
- Processing error detection and user notifications
- Graceful error recovery

## Troubleshooting

Common issues and solutions:

1. "Please load an image first!"
   - Solution: Load an image before attempting any operations

2. "Error loading image"
   - Check if the file exists
   - Verify the file format is supported
   - Ensure you have read permissions

3. "Error processing image"
   - Verify input parameters are within valid ranges
   - Check if the image is not corrupted
   - Ensure sufficient system memory

## System Requirements

- Operating System: Windows, macOS, or Linux
- RAM: 4GB minimum recommended
- Display Resolution: 1024x768 or higher
- Disk Space: 100MB for installation

## Dependencies

- PyQt5 (GUI framework)
- OpenCV (Image processing)
- NumPy (Array operations)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenCV for image processing capabilities
- PyQt5 for the GUI framework
- Python community for various resources and inspiration
