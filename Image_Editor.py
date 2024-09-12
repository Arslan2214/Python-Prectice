
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageEnhance, ImageOps
import numpy as np
import cv2

class ImageEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Image Editor")

        # Image state management
        self.image_stack = []
        self.redo_stack = []
        self.original_image = None
        self.display_image = None

        # Create UI elements
        self.canvas = tk.Canvas(root, width=600, height=400, bg='gray')
        self.canvas.pack(side=tk.RIGHT, padx=10, pady=10)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(side=tk.LEFT, padx=10, pady=10)

        # Button to upload image
        self.upload_button = tk.Button(self.button_frame, text="Upload Image", command=self.upload_image)
        self.upload_button.pack(pady=10)

        # Basic operation buttons
        self.crop_button = tk.Button(self.button_frame, text="Crop Image", command=self.crop_image)
        self.crop_button.pack(pady=10)

        self.brightness_button = tk.Button(self.button_frame, text="Increase Brightness", command=self.increase_brightness)
        self.brightness_button.pack(pady=10)

        self.temp_button = tk.Button(self.button_frame, text="Adjust Temperature", command=self.adjust_temperature)
        self.temp_button.pack(pady=10)

        self.grayscale_button = tk.Button(self.button_frame, text="Grayscale", command=self.grayscale)
        self.grayscale_button.pack(pady=10)

        # Undo and Redo buttons
        self.undo_button = tk.Button(self.button_frame, text="Undo", command=self.undo)
        self.undo_button.pack(pady=10)

        self.redo_button = tk.Button(self.button_frame, text="Redo", command=self.redo)
        self.redo_button.pack(pady=10)

    def upload_image(self):
        """Uploads an image from the file system"""
        file_path = filedialog.askopenfilename()
        if file_path:
            self.original_image = Image.open(file_path)
            self.add_image_to_stack(self.original_image)
            self.display_current_image()

    def add_image_to_stack(self, img):
        """Add the current image state to the stack for undo/redo"""
        self.image_stack.append(img.copy())
        self.redo_stack.clear()

    def display_current_image(self):
        """Displays the current image on the canvas"""
        if self.image_stack:
            img = self.image_stack[-1]
            self.display_image = ImageTk.PhotoImage(img.resize((600, 400), Image.ANTIALIAS))
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.display_image)

    def undo(self):
        """Undo the last action"""
        if len(self.image_stack) > 1:
            self.redo_stack.append(self.image_stack.pop())
            self.display_current_image()

    def redo(self):
        """Redo the last undone action"""
        if self.redo_stack:
            self.image_stack.append(self.redo_stack.pop())
            self.display_current_image()

    def crop_image(self):
        """Crop the image"""
        if self.image_stack:
            img = self.image_stack[-1]
            cropped_img = img.crop((50, 50, img.width - 50, img.height - 50))  # Example crop
            self.add_image_to_stack(cropped_img)
            self.display_current_image()

    def increase_brightness(self):
        """Increase image brightness"""
        if self.image_stack:
            img = self.image_stack[-1]
            enhancer = ImageEnhance.Brightness(img)
            bright_img = enhancer.enhance(1.5)  # Increase brightness by 50%
            self.add_image_to_stack(bright_img)
            self.display_current_image()

    def adjust_temperature(self):
        """Adjust the image temperature (simple color filter)"""
        if self.image_stack:
            img = self.image_stack[-1]
            img_np = np.array(img)
            img_np[:, :, 0] = np.clip(img_np[:, :, 0] + 50, 0, 255)  # Adding blue tone for a cooler effect
            temp_img = Image.fromarray(img_np)
            self.add_image_to_stack(temp_img)
            self.display_current_image()

    def grayscale(self):
        """Convert the image to grayscale"""
        if self.image_stack:
            img = self.image_stack[-1]
            gray_img = ImageOps.grayscale(img)
            self.add_image_to_stack(gray_img)
            self.display_current_image()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEditor(root)
    root.mainloop()
