import pytesseract
from PIL import Image
import tkinter as tk
from tkinter import filedialog
import json

# Ensure pytesseract is pointed to the tesseract executable if needed
# Example for Windows:
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to extract text from an image
def extract_text_from_image(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img, lang='eng+urd')  # Add urdu if needed
    return text

# Function to parse the OCR text into a JSON-like format
def parse_table_to_json(text):
    # Split the OCR text into rows
    rows = text.strip().split("\n")
    
    data = []

    # Assuming the first row is header, ignore it and parse the next rows for data
    for row in rows:
        # Split row into individual entries (space-separated in OCR output)
        entries = row.split()
        
        if len(entries) >= 8:  # Ensure row has enough entries
            try:
                # Map the table structure to a JSON-like format
                entry = {
                    "Serial Number": entries[0],
                    "Child's Name": entries[1] + " " + entries[2],  # Some names are split
                    "Father's Name": entries[3],
                    "Age": entries[4] + " " + entries[5],  # Combine year/month info
                    "DTP Booster": entries[6],
                    "MR-2": entries[7],
                    "MR-1": entries[8],
                    "Penta-3": entries[9],
                    "Penta-2": entries[10],
                    "Penta-1": entries[11],
                    "Vaccination Date": entries[12],
                    "Contact Number": entries[13]
                }
                data.append(entry)
            except IndexError:
                # Handle rows that don't have enough data
                pass
    
    return data

# Function to open a file using GUI and process it
def process_image_file():
    # GUI for selecting an image file
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(
        title="Select an Image file",
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff;*.tif")]
    )
    
    if not file_path:
        print("No file selected.")
        return

    # Extract text using pytesseract
    text = extract_text_from_image(file_path)
    
    # Parse the table into JSON-like format
    parsed_data = parse_table_to_json(text)
    
    # Output the JSON-like structure
    json_output = json.dumps(parsed_data, indent=4, ensure_ascii=False)
    print(json_output)

    # Optionally, save to a file
    with open("output.json", "w", encoding="utf-8") as f:
        f.write(json_output)
    print("Data saved to output.json")

# Run the program
if __name__ == "__main__":
    process_image_file()
