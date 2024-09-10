import tkinter as tk
from tkinter import filedialog
import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import pandas as pd
import json
import os

# Function to extract text from images using pytesseract
def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

# Function to extract text from PDF using PyMuPDF
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        text += pytesseract.image_to_string(img)
    return text

# Function to parse the extracted text and organize into key-value pairs (JSON-like format)
def parse_table_to_json(text):
    rows = text.strip().split("\n")
    
    # Assuming the first row contains column names
    columns = rows[0].split()
    data = []
    
    for row in rows[1:]:
        entries = row.split()
        if len(entries) == len(columns):
            entry = {columns[i]: entries[i] for i in range(len(columns))}
            data.append(entry)
    
    return data

# Function to select a file and analyze
def analyze_file():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(
        title="Select a PDF or Image file",
        filetypes=[("PDF files", "*.pdf"), ("Image files", "*.png;*.jpg;*.jpeg")]
    )
    
    if not file_path:
        print("No file selected.")
        return
    
    extension = os.path.splitext(file_path)[1].lower()
    
    if extension == '.pdf':
        text = extract_text_from_pdf(file_path)
    elif extension in ['.png', '.jpg', '.jpeg']:
        text = extract_text_from_image(file_path)
    else:
        print("Unsupported file type!")
        return
    
    data = parse_table_to_json(text)
    
    # Output the JSON-like format
    json_output = json.dumps(data, indent=4)
    print(json_output)
    
    # Optionally, save to a file
    with open("output.json", "w") as f:
        f.write(json_output)
    print("Data saved to output.json")

# Run the program
if __name__ == "__main__":
    analyze_file()
