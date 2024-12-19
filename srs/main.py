import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                           QHBoxLayout, QPushButton, QLabel, QSpinBox, 
                           QMessageBox, QFileDialog, QInputDialog)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap 

class ImageProcessorGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Processor")
        self.image = None
        self.setupUI()

    def setupUI(self):
        # Create main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)

        # Create image display label
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setText("No image loaded")
        layout.addWidget(self.image_label)

        # Create buttons
        button_layout = QHBoxLayout()
        
        # First row of buttons
        buttons_row1 = QHBoxLayout()
        self.createButton("Load Image", self.load_image, buttons_row1)
        self.createButton("Resize", self.resize_image, buttons_row1)
        self.createButton("Crop", self.crop_image, buttons_row1)
        self.createButton("Rotate", self.rotate_image, buttons_row1)
        layout.addLayout(buttons_row1)

        # Second row of buttons
        buttons_row2 = QHBoxLayout()
        self.createButton("Gaussian Blur", self.gaussian_blur, buttons_row2)
        self.createButton("Median Blur", self.median_blur, buttons_row2)
        self.createButton("Reduce Noise", self.reduce_noise, buttons_row2)
        self.createButton("Save Image", self.save_image, buttons_row2)
        layout.addLayout(buttons_row2)

        self.resize(800, 600)

    def createButton(self, text, slot, layout):
        button = QPushButton(text)
        button.clicked.connect(slot)
        layout.addWidget(button)

    def check_image_loaded(self):
        if self.image is None:
            QMessageBox.warning(self, "Warning", "Please load an image first!")
            return False
        return True

    def display_image(self):
        if self.image is not None:
            height, width = self.image.shape[:2]
            bytes_per_line = 3 * width
            q_image = QImage(cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB).data,
                           width, height, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(q_image)
            scaled_pixmap = pixmap.scaled(self.image_label.size(), 
                                        Qt.KeepAspectRatio,
                                        Qt.SmoothTransformation)
            self.image_label.setPixmap(scaled_pixmap)

    def load_image(self):
        try:
            file_name, _ = QFileDialog.getOpenFileName(self, "Open Image File",
                                                     "", "Images (*.png *.jpg *.jpeg *.bmp)")
            if file_name:
                self.image = cv2.imread(file_name)
                if self.image is None:
                    raise ValueError("Could not load image")
                self.display_image()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error loading image: {str(e)}")

    def resize_image(self):
        if not self.check_image_loaded():
            return
        try:
            current_height, current_width = self.image.shape[:2]
            width, ok = QInputDialog.getInt(self, "Resize Image", "Enter new width:",
                                          current_width, 1, 10000)
            if ok:
                height, ok = QInputDialog.getInt(self, "Resize Image", "Enter new height:",
                                               current_height, 1, 10000)
                if ok:
                    self.image = cv2.resize(self.image, (width, height))
                    self.display_image()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error resizing image: {str(e)}")

    def crop_image(self):
        if not self.check_image_loaded():
            return
        try:
            height, width = self.image.shape[:2]
            x, ok = QInputDialog.getInt(self, "Crop Image", "Enter x coordinate:",
                                      0, 0, width-1)
            if ok:
                y, ok = QInputDialog.getInt(self, "Crop Image", "Enter y coordinate:",
                                          0, 0, height-1)
                if ok:
                    w, ok = QInputDialog.getInt(self, "Crop Image", "Enter width:",
                                              width-x, 1, width-x)
                    if ok:
                        h, ok = QInputDialog.getInt(self, "Crop Image", "Enter height:",
                                                  height-y, 1, height-y)
                        if ok:
                            self.image = self.image[y:y+h, x:x+w]
                            self.display_image()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error cropping image: {str(e)}")

    def rotate_image(self):
        if not self.check_image_loaded():
            return
        try:
            angle, ok = QInputDialog.getDouble(self, "Rotate Image", 
                                             "Enter angle (degrees):",
                                             0, -360, 360, 1)
            if ok:
                height, width = self.image.shape[:2]
                center = (width // 2, height // 2)
                matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
                self.image = cv2.warpAffine(self.image, matrix, (width, height))
                self.display_image()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error rotating image: {str(e)}")

    def gaussian_blur(self):
        if not self.check_image_loaded():
            return
        try:
            kernel_size, ok = QInputDialog.getInt(self, "Gaussian Blur", 
                                                "Enter kernel size (odd number):",
                                                3, 1, 31, 2)
            if ok:
                if kernel_size % 2 == 0:
                    kernel_size += 1
                self.image = cv2.GaussianBlur(self.image, (kernel_size, kernel_size), 0)
                self.display_image()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error applying Gaussian blur: {str(e)}")

    def median_blur(self):
        if not self.check_image_loaded():
            return
        try:
            kernel_size, ok = QInputDialog.getInt(self, "Median Blur", 
                                                "Enter kernel size (odd number):",
                                                3, 1, 31, 2)
            if ok:
                if kernel_size % 2 == 0:
                    kernel_size += 1
                self.image = cv2.medianBlur(self.image, kernel_size)
                self.display_image()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error applying median blur: {str(e)}")

    def reduce_noise(self):
        if not self.check_image_loaded():
            return
        try:
            self.image = cv2.bilateralFilter(self.image, 9, 75, 75)
            self.display_image()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error reducing noise: {str(e)}")

    def save_image(self):
        if not self.check_image_loaded():
            return
        try:
            file_name, _ = QFileDialog.getSaveFileName(self, "Save Image File",
                                                     "", "Images (*.png *.jpg *.jpeg *.bmp)")
            if file_name:
                cv2.imwrite(file_name, self.image)
                QMessageBox.information(self, "Success", "Image saved successfully!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error saving image: {str(e)}")

def main():
    try:
        app = QApplication(sys.argv)
        window = ImageProcessorGUI()
        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"Fatal error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()